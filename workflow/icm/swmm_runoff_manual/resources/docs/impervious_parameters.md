# Impervious Surface Parameters

## Parameter Descriptions

| Parameter | Description | Units | Source |
|-----------|-------------|-------|--------|
| **Manning's n** | Manning's roughness coefficient for overland flow on impervious surfaces. Controls flow velocity and timing. | dimensionless | [1] |
| **Depression Storage** | Depth of water that must accumulate before runoff begins. Represents surface irregularities and ponding. | in or mm | [2] |

---

## Typical Values by Surface Type

| Surface Type | Manning's n | Depression Storage (in) | Depression Storage (mm) | Source |
|--------------|-------------|------------------------|-------------------------|--------|
| Smooth asphalt | 0.011 | 0.05 | 1.3 | [1][2] |
| Smooth concrete | 0.012 | 0.05 | 1.3 | [1][2] |
| Ordinary concrete | 0.013 | 0.06 | 1.5 | [1][2] |
| Asphalt (typical) | 0.016 | 0.06 | 1.5 | [1][2] |
| Brick/masonry | 0.014 | 0.06 | 1.5 | [1][2] |
| Roof (smooth) | 0.012 | 0.00 | 0.0 | [1][3] |
| Roof (with parapet) | 0.012 | 0.10 | 2.5 | [1][3] |
| Corrugated metal | 0.024 | 0.08 | 2.0 | [1][2] |
| Cement rubble | 0.024 | 0.10 | 2.5 | [1][2] |

---

## Manning's n Selection Guidance [1]

### Impervious Surfaces

| Surface Condition | Manning's n Range | Recommended |
|-------------------|-------------------|-------------|
| New smooth pavement | 0.011 - 0.012 | 0.011 |
| Typical urban pavement | 0.012 - 0.016 | 0.014 |
| Rough/aged pavement | 0.016 - 0.024 | 0.020 |

### Calibration Range [2]

| Bound | Value | Notes |
|-------|-------|-------|
| Lower | 0.005 | Very smooth surfaces |
| Upper | 0.015 | Rough surfaces, conservative |
| Typical calibrated | 0.010 - 0.013 | Most urban applications |

---

## Depression Storage Selection Guidance [2][3]

| Surface Type | Depression Storage (in) | Notes |
|--------------|------------------------|-------|
| Smooth impervious | 0.05 | New pavement, roofs without parapets |
| Typical pavement | 0.05 - 0.10 | General urban surfaces |
| Rough impervious | 0.10 | Aged pavement, textured surfaces |
| Rooftops with parapets | 0.10 - 0.25 | Ponding on flat roofs |

### Factors Affecting Depression Storage [3]

- **Surface slope**: Steeper slopes → less ponding → lower storage
- **Surface condition**: Rougher surfaces → more ponding → higher storage
- **Drainage features**: Curbs, gutters affect effective storage
- **Roof design**: Parapet walls can significantly increase storage

---

## %Zero-Imperv Guidance [2]

The percentage of impervious area with **no depression storage** (directly connected):

| Condition | %Zero-Imperv | Description |
|-----------|--------------|-------------|
| All imperv has storage | 0% | Rooftops with parapets, graded parking |
| Mixed conditions | 25-50% | Typical urban development |
| Directly connected | 75-100% | Crowned roads, sloped pavement |

---

## Sources

| Ref | Citation | Used For |
|-----|----------|----------|
| [1] | McCuen, R. et al. (1996), *Hydrology*, FHWA-SA-96-067, Federal Highway Administration, Washington, DC | Manning's n values |
| [2] | EPA/600/R-17/111, *Storm Water Management Model Reference Manual Volume I – Hydrology*, U.S. EPA | Depression storage, calibration ranges |
| [3] | Professional practice / EPA SWMM defaults | Roof considerations, %Zero-Imperv guidance |

---

## See Also

- [horton_infiltration_parameters.md](horton_infiltration_parameters.md) - Soil infiltration parameters (Horton method)
- [pervious_landcover_parameters.md](pervious_landcover_parameters.md) - Pervious surface parameters
- [swmm5_manning_n_overland_flow.md](../reference/ref_values/swmm5/swmm5_manning_n_overland_flow.md) - Complete Manning's n reference

---

*Last updated: December 2024*

