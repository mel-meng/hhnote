# Export InfoWorks ICM Results to Shapefile (Nodes + Links)

This repo is a short demo of **AI-assisted Ruby scripting** for **InfoWorks ICM**—turning a repetitive, manual results export into a **one-click** Shapefile exporter for **Nodes** and **Links (Conduits)** via **ODEC**. Watch the [YouTube demo](https://www.youtube.com/watch?v=ODPs28BVHD4).

## What it does
- Exports **Nodes** and **Links (Conduits)** results to ESRI **Shapefiles** using the **Open Data Export Center (ODEC)**.
- Names outputs using a **Prefix** that defaults to the **current run name** (derived from the results you have open):  
  - `{run_name}_node.shp`  
  - `{run_name}_link.shp`

## How to run (UI)
1. Open **simulation results** in **GeoPlan**.
2. In InfoWorks ICM: Create a new script
3. Paste: [`scripts/export_results_to_shp.rb`](scripts/export_results_to_shp.rb)
4. In the dialog, choose:
   - **Node** `.cfg` (field selection config `Node`)
   - **Link** `.cfg` (field selection config for `Conduit`)
   - **Output folder**
   - **Prefix** (defaults to the opened results **Run** name)

## Create the `.cfg` files
See: [`docs/create_cfg_files.md`](docs/create_cfg_files.md)

## Demo materials
- Manual workflow: [`docs/workflow.md`](docs/workflow.md)
- Takeaways / conclusion: [`docs/Takeaways.md`](docs/Takeaways.md)
- [LinkedIn post](https://www.linkedin.com/posts/melmeng_infoworks-icm-ruby-scripting-with-ai-activity-7404990589148233728-aDRf?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAE1ZywBDB2oL3LiCUeq7X1DCaSUShAPYWs)

## Reference examples (not included)
This repo intentionally does **not** include the large library of example scripts used as AI “reference material”.  
See: [`reference/references.md`](reference/references.md)



