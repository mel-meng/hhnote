# Pervious Landcover Parameters

## Parameter Descriptions

| Parameter | Description | Units | Source |
|-----------|-------------|-------|--------|
| **Manning's n** | Manning's roughness coefficient for overland flow on pervious surfaces. Controls flow velocity and timing based on vegetation/surface cover. | dimensionless | [1] |
| **Depression Storage** | Depth of water that must accumulate before runoff begins. Represents surface irregularities and ponding in pervious areas. | in or mm | [2] |

---

## Typical Values by Landcover Type

| Landcover Type | Manning's n | Depression Storage (in) | Depression Storage (mm) | Source |
|----------------|-------------|------------------------|-------------------------|--------|
| Fallow soils (no residue) | 0.05 | 0.20 | 5.1 | [1][2] |
| Cultivated (residue < 20%) | 0.06 | 0.20 | 5.1 | [1][2] |
| Cultivated (residue > 20%) | 0.17 | 0.20 | 5.1 | [1][2] |
| Range (natural) | 0.13 | 0.20 | 5.1 | [1][2] |
| Grass (short, prairie) | 0.15 | 0.20 | 5.1 | [1][2] |
| Grass (dense) | 0.24 | 0.20 | 5.1 | [1][2] |
| Bermuda grass | 0.41 | 0.25 | 6.4 | [1][2] |
| Woods (light underbrush) | 0.40 | 0.30 | 7.6 | [1][2] |
| Woods (dense underbrush) | 0.80 | 0.40 | 10.2 | [1][2] |

---

## Manning's n Selection Guidance [1]

### Pervious Surfaces

| Surface Condition | Manning's n Range | Notes |
|-------------------|-------------------|-------|
| Bare/fallow soil | 0.05 - 0.06 | Smooth, compacted surfaces |
| Cultivated fields | 0.06 - 0.17 | Depends on residue cover |
| Grass/turf | 0.15 - 0.41 | Varies with grass height/density |
| Wooded areas | 0.40 - 0.80 | Depends on underbrush density |

### Key Factors Affecting Manning's n

- **Vegetation density**: Denser vegetation → higher n values
- **Vegetation height**: Taller vegetation → higher n values
- **Surface irregularity**: Rougher surfaces → higher n values
- **Flow depth**: Shallow flows affected more by surface roughness

---

## Depression Storage Selection Guidance [2]

| Landcover Type | Depression Storage (in) | Notes |
|----------------|------------------------|-------|
| Bare/cultivated soil | 0.20 | Standard pervious default |
| Grass/turf | 0.20 - 0.25 | Denser grass may pond more |
| Wooded areas | 0.30 - 0.40 | Leaf litter and debris increase storage |

### Factors Affecting Depression Storage

- **Vegetation**: More vegetation → more surface irregularity → higher storage
- **Leaf litter**: Wooded areas accumulate organic debris
- **Soil type**: Does not directly affect depression storage (handled separately by infiltration)
- **Slope**: Steeper slopes → less ponding → lower storage

---

## Sources

| Ref | Citation | Used For |
|-----|----------|----------|
| [1] | McCuen, R. et al. (1996), *Hydrology*, FHWA-SA-96-067, Federal Highway Administration, Washington, DC | Manning's n values |
| [2] | EPA/600/R-17/111, *Storm Water Management Model Reference Manual Volume I – Hydrology*, U.S. EPA | Depression storage guidance |

---

## See Also

- [horton_infiltration_parameters.md](horton_infiltration_parameters.md) - Soil infiltration parameters (separate from landcover)
- [impervious_parameters.md](impervious_parameters.md) - Impervious surface parameters
- [swmm5_manning_n_overland_flow.md](../reference/ref_values/swmm5/swmm5_manning_n_overland_flow.md) - Complete Manning's n reference

---

*Last updated: December 2024*

