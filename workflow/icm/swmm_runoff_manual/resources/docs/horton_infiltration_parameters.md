# Horton Infiltration Parameters

## Parameter Descriptions

| Parameter | Description | Source |
|-----------|-------------|--------|
| **Max. Infil. Rate** | Maximum infiltration rate on the Horton curve (in/hr or mm/hr). See table below for typical values by soil type. | [1] |
| **Min. Infil. Rate** | Minimum infiltration rate on the Horton curve (in/hr or mm/hr). Equivalent to the saturated hydraulic conductivity. See the Soil Characteristics Table for typical values. | [2] |
| **Decay Const.** | Infiltration rate decay constant for the Horton curve (1/hours). Typical values range between 2 and 7 hr⁻¹. | [1][3] |
| **Drying Time** | Time in days for a fully saturated soil to dry completely. Typical values range from 2 to 14 days. | [3] |
| **Max. Infil. Vol.** | Maximum infiltration volume possible (inches or mm, 0 if not applicable). It can be estimated as the difference between a soil's porosity and its wilting point times the depth of the infiltration zone. | [1] |

---

## Representative Values for Max. Infiltration Rate (f₀)

### A. DRY soils (with little or no vegetation) [1]

| Soil Type | Rate (in/hr) | Rate (mm/hr) |
|-----------|--------------|--------------|
| Sandy soils | 5 | 127 |
| Loam soils | 3 | 76 |
| Clay soils | 1 | 25.4 |

### B. DRY soils (with dense vegetation) [1]

Multiply values given in A. by **2**

### C. MOIST soils [1]

| Condition | Adjustment |
|-----------|------------|
| **Soils at field capacity** (drained but not dried out) | Divide values from A and B by 3 |
| **Soils partially dried out** | Divide values from A and B by 1.5 - 2.5 |
| **Soils close to saturation** | Use value close to min. infiltration rate (f∞) |

---

## Min. Infiltration Rate (f∞) by Soil Type [2]

The minimum infiltration rate equals the saturated hydraulic conductivity (K):

| Soil Texture Class | K (in/hr) | Recommended f∞ (in/hr) |
|--------------------|-----------|------------------------|
| Sand | 4.74 | 1.0 - 1.5 |
| Loamy Sand | 1.18 | 0.5 - 1.0 |
| Sandy Loam | 0.43 | 0.3 - 0.5 |
| Loam | 0.13 | 0.1 - 0.3 |
| Silt Loam | 0.26 | 0.1 - 0.3 |
| Sandy Clay Loam | 0.06 | 0.05 - 0.1 |
| Clay Loam | 0.04 | 0.05 - 0.1 |
| Silty Clay Loam | 0.04 | 0.03 - 0.05 |
| Sandy Clay | 0.02 | 0.02 - 0.05 |
| Silty Clay | 0.02 | 0.02 - 0.05 |
| Clay | 0.01 | 0.01 - 0.03 |

---

## Decay Constant (k) [1][3]

| Range | Value | Notes |
|-------|-------|-------|
| Typical | 2 - 7 hr⁻¹ | Most applications |
| Sandy soils | 3 - 5 hr⁻¹ | Faster drainage |
| Clay soils | 2 - 3 hr⁻¹ | Slower drainage |

- Higher k values → faster decay to minimum rate
- Lower k values → sustained high infiltration

---

## Drying Time [3]

| Soil Type | Drying Time (days) |
|-----------|-------------------|
| Sandy soils | 2 - 5 |
| Loam soils | 5 - 7 |
| Clay soils | 7 - 14 |

---

## Sources

| Ref | Citation | Used For |
|-----|----------|----------|
| [1] | EPA/600/R-17/111, *Storm Water Management Model Reference Manual Volume I – Hydrology*, U.S. EPA | f₀ values, decay constant range, volume calculation |
| [2] | Rawls, W.J. et al. (1983), *Green-Ampt Infiltration Parameters from Soils Data*, J. Hyd. Engr. 109:1316 | Hydraulic conductivity K (used as f∞) |
| [3] | Professional practice / EPA SWMM defaults | k typical ranges, drying time estimates |

---

## See Also

- [Soil Characteristics](soil_characteristics.md) - Complete soil hydraulic properties from Rawls et al. (1983)
- [pervious_landcover_parameters.md](pervious_landcover_parameters.md) - Pervious surface parameters (Manning's n, depression storage)
- [impervious_parameters.md](impervious_parameters.md) - Impervious surface parameters

---

*Last updated: December 2024*
