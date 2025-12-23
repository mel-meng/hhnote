# Database Reference Tables
ID Lookup Guide for Manual Subcatchment.csv Updates

## How to Use This Reference
When manually updating `subcatchment.csv`, use the following ID columns:
- **soil_id**: Use values from the *Horton Infiltration* table below
- **perv_landcover_id**: Use values from the *Pervious Landcover* table below
- **imp_landcover_id**: Use values from the *Impervious Landcover* table below

> Note: The ID columns show the values to use in subcatchment.csv. The description columns show what each ID represents.

## 1. Horton Infiltration Parameters (soil_id reference)

| soil_id | soil_description | Max. Infil. Rate (in/hr) | Min. Infil. Rate (in/hr) | Decay Const. (1/hr) | Drying Time (days) | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | sand | 5 | 1 | 4 | 3 | [1][2][3] |
| 2 | loamy_sand | 4 | 0.75 | 3.5 | 4 | [1][2][3] |
| 3 | sandy_loam | 3.5 | 0.4 | 3 | 5 | [1][2][3] |
| 4 | loam | 3 | 0.25 | 3 | 5 | [1][2][3] |
| 5 | silt_loam | 2.5 | 0.25 | 2.5 | 6 | [1][2][3] |
| 6 | sandy_clay_loam | 2 | 0.1 | 2.5 | 7 | [1][2][3] |
| 7 | clay_loam | 1.5 | 0.05 | 2.5 | 7 | [1][2][3] |
| 8 | silty_clay_loam | 1.5 | 0.05 | 2.5 | 8 | [1][2][3] |
| 9 | sandy_clay | 1 | 0.03 | 2 | 9 | [1][2][3] |
| 10 | silty_clay | 1 | 0.03 | 2 | 10 | [1][2][3] |
| 11 | clay | 0.5 | 0.01 | 2 | 10 | [1][2][3] |

For detailed parameter descriptions and selection guidance, see: [Horton Infiltration Parameters](docs/horton_infiltration_parameters.md)

## 2. Pervious Landcover Parameters (perv_landcover_id reference)

| perv_landcover_id | perv_landcover_description | Manning's n (dimensionless) | Depression Storage (in) | Source |
| :--- | :--- | :--- | :--- | :--- |
| 1 | fallow_soil | 0.05 | 0.2 | [1] |
| 2 | cultivated_low | 0.06 | 0.2 | [1] |
| 3 | cultivated_high | 0.17 | 0.2 | [1] |
| 4 | range_natural | 0.13 | 0.2 | [1] |
| 5 | grass_short | 0.15 | 0.2 | [1] |
| 6 | grass_dense | 0.24 | 0.2 | [1] |
| 7 | grass_bermuda | 0.41 | 0.25 | [1] |
| 8 | woods_light | 0.4 | 0.3 | [1] |
| 9 | woods_dense | 0.8 | 0.4 | [1] |

For detailed parameter descriptions and selection guidance, see: [Pervious Landcover Parameters](docs/pervious_landcover_parameters.md)

## 3. Impervious Landcover Parameters (imp_landcover_id reference)

| imp_landcover_id | imp_landcover_description | Manning's n (dimensionless) | Depression Storage (in) | Source |
| :--- | :--- | :--- | :--- | :--- |
| 1 | smooth_asphalt | 0.011 | 0.05 | [1][2] |
| 2 | smooth_concrete | 0.012 | 0.05 | [1][2] |
| 3 | ordinary_concrete | 0.013 | 0.06 | [1][2] |
| 4 | asphalt | 0.016 | 0.06 | [1][2] |
| 5 | brick_masonry | 0.014 | 0.06 | [1][2] |
| 6 | roof | 0.012 | 0 | [1][3] |
| 7 | roof_parapet | 0.012 | 0.1 | [1][3] |
| 8 | corrugated_metal | 0.024 | 0.08 | [1][2] |
| 9 | cement_rubble | 0.024 | 0.1 | [1][2] |

For detailed parameter descriptions and selection guidance, see: [Impervious Landcover Parameters](docs/impervious_parameters.md)

Generated on 2025-12-23 12:22:22
