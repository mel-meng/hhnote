# Hydrocalc CLI Tool

This tool extracts and merges time series data from hydrocalc output CSV files and converts them into a gauged inflow format suitable for XPSWMM.

## Features

- **Merge Time Series:** Combines multiple hydrocalc output CSVs into a single merged time series file.
- **Gauged Inflow Conversion:** Converts the merged data into a long-format CSV (`gauged_inflow.csv`) compatible with XPSWMM, including resampling to a regular time interval.

## Requirements

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management) or standard Python with `polars` installed.

## Installation

1.  Unzip the source code.
2.  Navigate to the code folder:

    ```bash
    cd <code_folder>
    ```

3.  Install [uv](https://github.com/astral-sh/uv).
4.  Sync dependencies:

    ```bash
    uv sync
    ```

## Quick Start

After installation, run this command from the project folder:

```bash
uv run hydrocalc.py --csv_folder data/proj_a/CSV_Results --subarea_csv data/proj_a/proj_a.csv --output_folder data/proj_a/output --start_date "2023-01-01 00:00" --resample_interval 1 --check-plot "all"
```

**What each part means:**

| Part | Description |
|------|-------------|
| `uv run hydrocalc.py` | Runs the script using uv |
| `--csv_folder data/proj_a/CSV_Results` | Folder containing your hydrocalc CSV files (e.g., `proj - 64.csv`) |
| `--subarea_csv data/proj_a/proj_a.csv` | Your mapping file that lists which project goes with which subarea |
| `--output_folder data/proj_a/output` | Where to save the results |
| `--start_date "2023-01-01 00:00"` | When the time series starts (use your actual storm event date) |
| `--resample_interval 1` | Resample to 1-minute intervals (optional, default is 1) |
| `--check-plot "all"` | Generate comparison plots for all subareas (optional, use `"64,87"` for specific ones) |

**Result:** The tool creates `gauged_inflow.csv` in your output folder, ready to import into XPSWMM.

## Usage

1.  **Prepare Script**: Ensure the source code is unzipped and you are inside the project folder.

2.  **Prepare Data**: Identify the paths to your data files, or copy them into the project folder for convenience:
    *   **Hydrocalc Output Folder**: The directory containing the generated CSV files.
    *   **Subarea Mapping CSV**: The CSV file mapping projects to subareas.

3.  **Run the Tool**: Execute the script using `uv`. Replace the placeholders with your actual paths:

    ```bash
    uv run hydrocalc.py --csv_folder <path_to_csv_folder> --subarea_csv <path_to_mapping_csv> --output_folder <path_to_output_folder> --start_date "YYYY-MM-DD HH:MM"
    ```

### Arguments

-   `--csv_folder` (Required): Path to the folder containing the hydrocalc output CSV files (e.g., `proj - 64.csv`).
-   `--subarea_csv` (Required): Path to the input CSV file mapping projects to subareas (must contain `project` and `subarea` columns).
-   `--output_folder` (Required): Directory where the output files will be saved.
-   `--start_date` (Required): The start date and time for the time series in `"YYYY-MM-DD HH:MM"` format.
-   `--resample_interval` (Optional): Interval in minutes to resample the data (default is `1`).
-   `--check` / `--no-check` (Optional): Enable or disable validation by comparing statistics and generating plots (default: enabled).
-   `--check-plot` (Optional): Comma-separated list of subareas to generate check plots for. Use `'all'` to plot all subareas. If not specified, plots first and last subareas.

### Examples

Basic usage:
```bash
uv run hydrocalc.py --csv_folder data/proj_a/CSV_Results --subarea_csv data/proj_a/proj_a.csv --output_folder data/proj_a/output --start_date "2023-01-01 00:00"
```

Skip validation (faster):
```bash
uv run hydrocalc.py --csv_folder data/proj_a/CSV_Results --subarea_csv data/proj_a/proj_a.csv --output_folder data/proj_a/output --start_date "2023-01-01 00:00" --no-check
```

Generate plots for specific subareas:
```bash
uv run hydrocalc.py --csv_folder data/proj_a/CSV_Results --subarea_csv data/proj_a/proj_a.csv --output_folder data/proj_a/output --start_date "2023-01-01 00:00" --check-plot "64,87"
```

Generate plots for all subareas:
```bash
uv run hydrocalc.py --csv_folder data/proj_a/CSV_Results --subarea_csv data/proj_a/proj_a.csv --output_folder data/proj_a/output --start_date "2023-01-01 00:00" --check-plot "all"
```

## Output

The tool generates the following files in the specified output folder:

1.  `merged_timeseries.csv`: A wide-format CSV containing the raw merged time series data.
2.  `gauged_inflow.csv`: A long-format CSV with columns `DATE`, `TIME`, `FLOW`, and `STATION`, resampled to the specified interval.

When validation is enabled (`--check`, the default):
3.  `source_stats.csv`: Statistics (peak, mean, duration) for each subarea from the source data.
4.  `check_plot_<subarea>.png`: Comparison plots showing source vs resampled data for selected subareas.

