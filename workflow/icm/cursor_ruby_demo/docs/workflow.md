# Export Simulation Results to Shapefile - Requirements

## Purpose

Document the manual workflow for exporting simulation results (nodes and links) to ESRI Shapefiles using the Open Data Export Center in ICM.

---

## Prerequisites

- Simulation results already open in GeoPlan
- Saved configuration files for nodes and links (`.cfg` files defining which fields to export)

---

## Manual Workflow Steps

### Step 1: Access the Open Data Export Center

1. With simulation results open in the GeoPlan
2. Go to **Network** menu
3. Select **Export**
4. Choose **Open Data Export Center**

### Step 2: Export Nodes

1. In the Open Data Export Center, select **Nodes** as the data type
2. Set the export format to **Shapefile**
3. Browse to select the output folder
4. Set the filename prefix using the run name: `{run_name}_node`
5. Click **Load Configuration** and select the saved node configuration file
   - The configuration file contains only the required fields for export
6. Click **Export**

### Step 3: Export Links

1. Switch to **All Links** as the data type
2. Keep the same output folder
3. Set the filename prefix using the run name: `{run_name}_link`
4. Click **Load Configuration** and select the saved link configuration file
5. Click **Export**

---

## Scripted workflow note

When using [`scripts/export_results_to_shp.rb`](../scripts/export_results_to_shp.rb), the dialog includes a **Prefix** field that **defaults to the opened results Run name** and is used to build `{prefix}_node` / `{prefix}_link`.

---

## Output Files

After completing the export, the following files will be created:

| Element Type | Output File Pattern |
|--------------|---------------------|
| Nodes        | `{run_name}_node.shp` (with .dbf, .shx, .prj) |
| Links        | `{run_name}_link.shp` (with .dbf, .shx, .prj) |

---

## Key Details

| Item | Description |
|------|-------------|
| **Naming Convention** | `{run_name}_{element_type}` where run name is derived from the currently opened simulation results |
| **Export Format** | ESRI Shapefile (SHP) |
| **Configuration Files** | Pre-saved `.cfg` files that define which fields to include in the export |
| **Starting Point** | Results must already be open in GeoPlan |

---

## Configuration Files

The configuration files (`.cfg`) are created by:
1. Opening the Open Data Export Center
2. Selecting the desired fields for export
3. Using **Save Configuration** to save the field mapping

This allows consistent exports with only the required fields, reducing file size and complexity.





