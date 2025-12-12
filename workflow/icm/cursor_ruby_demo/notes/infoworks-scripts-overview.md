# InfoWorks ICM Ruby Scripts Overview

The `reference/01 Ruby/01 InfoWorks` folder contains **73+ Ruby scripts** for automating InfoWorks ICM (Integrated Catchment Modeling). These scripts provide automation capabilities for hydraulic modeling workflows.

## Script Categories

| Category | Description |
|----------|-------------|
| **Network Data** | Read, write, export, and import network model data (nodes, conduits, subcatchments, river reaches) |
| **Database Operations** | Navigate database tree, find model groups, export database objects |
| **Simulations** | Run simulations, check status, query results, export results to CSV |
| **Network Analysis** | Trace networks, calculate upstream areas, check conditions like reverse slopes |
| **RTC (Real-Time Control)** | Import/export RTC configurations |
| **Developer Tools** | Utilities for learning and building Ruby scripts |

## Script Execution Types

- **UI** - Run from InfoWorks ICM user interface
- **EX** - Run from ICM Exchange (headless/automation)
- **UI & EX** - Works in both environments

## Key Capabilities

- Subcatchment management (connect to nodes, runoff surfaces, SUDS)
- River reach operations (Manning's n, cross sections, bank levels)
- Conduit operations (inverts, headloss, geometry)
- Selection list creation from SQL queries or CSV
- Scenario management (create, delete, modify)
- Results extraction (timesteps, binary export, CSV export)
- GIS integration (geodatabase export, MIF format)

