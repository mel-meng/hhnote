# Create ODEC `.cfg` files (fields to export)

The exporter script relies on two **Open Data Export Center (ODEC)** configuration files:
- `node.cfg` for **Nodes**
- `link.cfg` for **Links** (ODEC table is typically **All Links / Conduit**)

These `.cfg` files define **which fields** are included in the export.

## Steps
1. Open **simulation results** in **GeoPlan**.
2. Go to **Network → Export → Open Data Export Center**.
3. **Nodes**:
   - Set format to **Shapefile**
   - Choose your desired export fields
   - Click **Save Configuration** → save as `node.cfg`
4. **Links / All Links**:
   - Switch data type to **All Links** (or the link table you export from)
   - Choose your desired export fields
   - Click **Save Configuration** → save as `link.cfg`

## Using the configs with the script
When you run [`scripts/export_results_to_shp.rb`](../scripts/export_results_to_shp.rb), it prompts you to select:
- the Node `.cfg`
- the Link `.cfg`
- the output folder

For the full manual workflow, see [`docs/workflow.md`](workflow.md).


