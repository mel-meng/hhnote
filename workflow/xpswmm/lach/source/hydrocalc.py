"""
Extract and merge time series from hydrocalc output CSV files.
"""

import argparse
import polars as pl
from pathlib import Path
from typing import Dict, List, Optional
import io
from functools import reduce
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

TIME_COL = "Time (min)"
FLOW_COL = "Clear Peak Flow Rate (cfs)"


def compute_stats(df: pl.DataFrame, time_col: str, flow_col: str) -> Dict[str, float]:
    """Compute statistics for a time/flow series."""
    # Cast columns to Float64 to handle string inputs from CSV
    valid_df = df.select([
        pl.col(time_col).cast(pl.Float64, strict=False),
        pl.col(flow_col).cast(pl.Float64, strict=False)
    ]).filter(pl.col(time_col).is_not_null() & pl.col(flow_col).is_not_null())
    
    if valid_df.height == 0:
        return {"peak": 0.0, "mean": 0.0, "duration": 0.0}
    
    stats = valid_df.select([
        pl.col(flow_col).max().alias("peak"),
        pl.col(flow_col).mean().alias("mean"),
        (pl.col(time_col).max() - pl.col(time_col).min()).alias("duration")
    ]).row(0)
    
    return {"peak": float(stats[0] or 0), "mean": float(stats[1] or 0), "duration": float(stats[2] or 0)}


def _print_stats_comparison(
    source_stats: Dict[str, Dict[str, float]],
    compare_stats: Dict[str, Dict[str, float]],
    subareas: List[str],
    title: str,
    compare_label: str = "Compare",
    warn_on_peak_diff: bool = False
) -> List[str]:
    """
    Print a comparison table between source and comparison statistics.
    
    Returns list of warning messages if warn_on_peak_diff is True.
    """
    print(f"\n=== {title} ===")
    print(f"{'Subarea':<12} {'Metric':<10} {'Source':>12} {compare_label:>12} {'Diff %':>10}")
    print("-" * 60)
    
    warnings = []
    for subarea in subareas[:5]:  # Show first 5 for brevity
        for metric in ["peak", "mean", "duration"]:
            src_val = source_stats.get(subarea, {}).get(metric, 0)
            cmp_val = compare_stats.get(subarea, {}).get(metric, 0)
            diff_pct = ((cmp_val - src_val) / src_val * 100) if src_val != 0 else 0
            warning_flag = ""
            if warn_on_peak_diff and metric == "peak" and abs(diff_pct) > 5:
                warning_flag = " !"
                warnings.append(f"  - {subarea}: peak differs by {diff_pct:.2f}%")
            print(f"{subarea:<12} {metric:<10} {src_val:>12.2f} {cmp_val:>12.2f} {diff_pct:>9.2f}%{warning_flag}")
    
    if len(subareas) > 5:
        print(f"... and {len(subareas) - 5} more subareas")
    
    return warnings


def read_hydrocalc_csv(file_path: Path) -> pl.DataFrame:
    """
    Read a hydrocalc output CSV file, handling the variable header location.
    Returns a DataFrame with 'Time (min)' and 'Clear Peak Flow Rate (cfs)' columns.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
        
    # Read the file as text first to find the header line index
    with open(file_path, 'rb') as f:
        lines = f.readlines()
    
    header_idx = -1
    for i, line in enumerate(lines):
        # Decode line to check for header
        try:
            line_str = line.decode('utf-8')
        except UnicodeDecodeError:
            line_str = line.decode('latin-1')  # Fallback
            
        if line_str.startswith("Time (min)"):
            header_idx = i
            break
    
    if header_idx == -1:
        raise ValueError(f"Could not find header row starting with 'Time (min)' in {file_path}")
        
    # Create a BytesIO object with the relevant lines
    csv_content = b"".join(lines[header_idx:])
    
    # Read CSV from the memory buffer
    df = pl.read_csv(
        io.BytesIO(csv_content),
        has_header=True,
        null_values=[""],
        infer_schema_length=10000
    )
    
    # Filter out any rows that are completely null (empty quoted lines)
    df = df.filter(pl.col("Time (min)").is_not_null())
    
    return df


def extract_and_merge_timeseries(
    input_csv_path: str,
    csv_folder_path: str,
    output_filename: str,
    check: bool = True,
    output_folder: Optional[Path] = None
) -> Dict[str, Dict[str, float]]:
    """
    Extract time series data from multiple CSV files and merge them into a single CSV.
    
    Returns Dict mapping subarea ID to source statistics (if check=True), empty dict otherwise.
    """
    input_df = pl.read_csv(input_csv_path)
    csv_folder = Path(csv_folder_path)
    
    timeseries_data: Dict[str, pl.DataFrame] = {}
    source_stats: Dict[str, Dict[str, float]] = {}
    
    # Process each file
    for project, subarea in zip(input_df["project"].to_list(), input_df["subarea"].to_list()):
        file_path = csv_folder / f"{project} - {subarea}.csv"
        df = read_hydrocalc_csv(file_path)
        
        # Verify required columns exist
        for col in [TIME_COL, FLOW_COL]:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' not found in {file_path}")
        
        extracted = df.select([TIME_COL, FLOW_COL])
        
        # Compute source stats while we have the data
        if check:
            source_stats[str(subarea)] = compute_stats(extracted, TIME_COL, FLOW_COL)
        
        # Rename flow column to subarea ID for merging
        timeseries_data[str(subarea)] = extracted.rename({FLOW_COL: str(subarea)})
    
    # Merge all time series using reduce
    merged_df = reduce(
        lambda left, right: left.join(right, on=TIME_COL, how="full", coalesce=True),
        timeseries_data.values()
    ).sort(TIME_COL).fill_null(0.0)
    
    merged_df.write_csv(output_filename)
    print(f"Successfully merged {len(timeseries_data)} time series to {output_filename}")
    
    # Check: Compare source stats with merged stats
    if check and output_folder:
        all_subareas = [col for col in merged_df.columns if col != TIME_COL]
        merged_stats = {
            subarea: compute_stats(merged_df, TIME_COL, subarea)
            for subarea in all_subareas
        }
        
        _print_stats_comparison(source_stats, merged_stats, all_subareas, 
                                "Source vs Merged Statistics", "Merged")
        
        # Save source stats to CSV
        stats_df = pl.DataFrame([
            {"subarea": sub, "peak": s["peak"], "mean": s["mean"], "duration": s["duration"]}
            for sub, s in source_stats.items()
        ])
        stats_file = output_folder / "source_stats.csv"
        stats_df.write_csv(str(stats_file))
        print(f"\nSource statistics saved to {stats_file}")
    
    return source_stats


def to_gauged_inflow(
    input_csv_path: str, 
    output_csv_path: str, 
    start_datetime_str: str,
    resample_interval_min: int = 1,
    check: bool = True,
    source_stats: Optional[Dict[str, Dict[str, float]]] = None,
    output_folder: Optional[Path] = None,
    check_plot_subareas: Optional[list] = None
) -> None:
    """
    Convert the merged timeseries CSV to the long format required for XPSWMM Gauged Inflow.
    Resamples the data to a regular interval using linear interpolation.
    
    Reference: https://mel-meng-pe.medium.com/how-to-use-gauged-inflow-in-xpswmm-ad41f77dca29
    """
    df = pl.read_csv(input_csv_path)
    start_dt = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M")
    
    # Ensure time column is float and clean
    df = df.with_columns(pl.col(TIME_COL).cast(pl.Float64, strict=False)).drop_nulls(subset=[TIME_COL])
    
    # Keep original for plotting before transformation
    merged_df_for_plot = df.clone() if check else None
    
    # Convert Time (min) to datetime
    df = df.with_columns(
        (start_dt + pl.duration(microseconds=pl.col(TIME_COL) * 60 * 1_000_000)).alias("datetime")
    )
    
    station_cols = [col for col in df.columns if col not in [TIME_COL, "datetime"]]
    df = df.select(["datetime"] + station_cols).sort("datetime")
    
    # Create regular time grid and resample via interpolation
    min_dt, max_dt = df["datetime"].min(), df["datetime"].max()
    target_df = pl.DataFrame(
        pl.datetime_range(start=min_dt, end=max_dt, interval=f"{resample_interval_min}m", eager=True).alias("datetime")
    )
    
    # Join, interpolate, and keep only target grid points
    resampled_df = (
        df.join(target_df, on="datetime", how="full", coalesce=True)
        .sort("datetime")
        .with_columns([pl.col(col).interpolate() for col in station_cols])
        .join(target_df, on="datetime", how="semi")
        .with_columns([
            pl.col("datetime").dt.strftime("%d/%m/%y").alias("DATE"),
            pl.col("datetime").dt.strftime("%H:%M").alias("TIME")
        ])
    )
    
    # Melt to long format and write
    final_df = resampled_df.unpivot(
        index=["DATE", "TIME"],
        on=station_cols,
        variable_name="STATION",
        value_name="FLOW"
    ).select(["DATE", "TIME", "FLOW", "STATION"])
    
    final_df.write_csv(output_csv_path)
    print(f"Successfully converted to gauged inflow format: {output_csv_path} (resampled to {resample_interval_min} min)")
    
    # Check: Compare source stats with gauged stats
    if not (check and source_stats and output_folder):
        return
    
    # Compute gauged stats directly from resampled_df
    duration = (resampled_df["datetime"].max() - resampled_df["datetime"].min()).total_seconds() / 60
    gauged_stats = {
        station: {
            "peak": float(resampled_df[station].max() or 0),
            "mean": float(resampled_df[station].mean() or 0),
            "duration": duration
        }
        for station in station_cols
    }
    
    warnings = _print_stats_comparison(
        source_stats, gauged_stats, station_cols,
        f"Source vs Gauged Statistics (resampled to {resample_interval_min} min)",
        "Gauged", warn_on_peak_diff=True
    )
    
    if warnings:
        print("\nWarnings (peak differs > 5%):")
        for w in warnings:
            print(w)
    
    # Generate check plots
    if check_plot_subareas == ['all']:
        subareas_to_plot = station_cols
    elif check_plot_subareas:
        subareas_to_plot = check_plot_subareas
    else:
        subareas_to_plot = [station_cols[0]] + ([station_cols[-1]] if len(station_cols) > 1 else [])
    for subarea in subareas_to_plot:
        _plot_comparison(merged_df_for_plot, resampled_df, subarea, start_dt, output_folder)


def _plot_comparison(
    merged_df: pl.DataFrame,
    resampled_df: pl.DataFrame,
    subarea: str,
    start_dt: datetime,
    output_folder: Path
) -> None:
    """Generate a comparison plot for a specific subarea."""
    # Prepare merged data
    merged_data = merged_df.select([TIME_COL, subarea]).sort(TIME_COL)
    merged_datetimes = [start_dt + timedelta(minutes=float(t)) for t in merged_data[TIME_COL].to_list()]
    
    # Prepare resampled data
    resampled_data = resampled_df.select(["datetime", subarea]).sort("datetime")
    
    # Create plot
    plt.figure(figsize=(12, 6))
    plt.plot(merged_datetimes, merged_data[subarea].to_list(), 
             label='Source (Original)', marker='o', markersize=3, linestyle='-', alpha=0.7, color='blue')
    plt.plot(resampled_data["datetime"].to_list(), resampled_data[subarea].to_list(),
             label='Gauged (Resampled)', marker='x', markersize=2, linestyle='--', alpha=0.7, color='red')
    
    plt.title(f"Time Series Comparison - Subarea {subarea}")
    plt.xlabel("Date Time")
    plt.ylabel("Flow Rate (cfs)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    output_plot = output_folder / f"check_plot_{subarea}.png"
    plt.savefig(str(output_plot))
    print(f"Plot saved to {output_plot}")
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge hydrocalc CSV files and convert to gauged inflow format.")
    parser.add_argument("--csv_folder", required=True, help="Path to the folder containing output CSV files")
    parser.add_argument("--subarea_csv", required=True, help="Path to the subarea mapping CSV file")
    parser.add_argument("--output_folder", required=True, help="Path to the output directory")
    parser.add_argument("--start_date", required=True, help="Start date and time string in 'YYYY-MM-DD HH:MM' format")
    parser.add_argument("--resample_interval", type=int, default=1, help="Interval in minutes to resample the data to (default: 1)")
    parser.add_argument("--check", action=argparse.BooleanOptionalAction, default=True, 
                        help="Validate data by comparing statistics and generating plots (default: True, use --no-check to disable)")
    parser.add_argument("--check-plot", type=str, default=None, metavar="SUBAREAS",
                        help="Comma-separated list of subareas to generate check plots for (e.g., --check-plot '64,87' or --check-plot 'Area 1,Area 2')")

    args = parser.parse_args()
    
    # Parse check-plot subareas from comma-separated string
    check_plot_subareas = [s.strip() for s in args.check_plot.split(",")] if args.check_plot else None

    # Create output folder if it doesn't exist
    output_path = Path(args.output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    # Define intermediate and final output filenames
    merged_timeseries_file = output_path / "merged_timeseries.csv"
    gauged_inflow_file = output_path / "gauged_inflow.csv"

    print(f"Processing files from {args.csv_folder} using mapping from {args.subarea_csv}...")
    
    # 1. Merge time series (and compute source stats if check=True)
    source_stats = extract_and_merge_timeseries(
        input_csv_path=args.subarea_csv,
        csv_folder_path=args.csv_folder,
        output_filename=str(merged_timeseries_file),
        check=args.check,
        output_folder=output_path
    )

    # 2. Convert to gauged inflow (and validate if check=True)
    print(f"\nConverting to gauged inflow format starting from {args.start_date}...")
    to_gauged_inflow(
        input_csv_path=str(merged_timeseries_file),
        output_csv_path=str(gauged_inflow_file),
        start_datetime_str=args.start_date,
        resample_interval_min=args.resample_interval,
        check=args.check,
        source_stats=source_stats,
        output_folder=output_path,
        check_plot_subareas=check_plot_subareas
    )
    
    print("\nDone.")
