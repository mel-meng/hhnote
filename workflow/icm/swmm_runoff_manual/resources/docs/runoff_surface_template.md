# Runoff Surface Template

## Purpose

This template file provides default values for all 67 ICM runoff surface columns. When generating runoff surfaces from parameter databases, the script copies a template row and overrides only the fields sourced from the databases.

This approach ensures:
- Consistent default values across all generated surfaces
- Only database-sourced fields are modified
- Easy addition of new infiltration methods by adding template rows

---

## Template Index Reference

Each template row is identified by a unique `runoff_index`:

| runoff_index | surface_type | runoff_volume_type | When to Use |
|--------------|--------------|-------------------|-------------|
| 1 | Impervious | Fixed | Impervious surfaces (100-series and 200-series) |
| 2 | Pervious | HortonSWMM | Pervious surfaces with Horton infiltration (300-series) |
| 3 | Pervious | GreenAmptSWMM | (Future) Pervious surfaces with Green-Ampt infiltration |

### Template 1: Impervious

Use for all impervious surfaces, regardless of depression storage:
- **100-series**: Impervious with depression storage (depression_storage from database)
- **200-series**: Impervious without depression storage (initial_loss_value = 0)

Key defaults:
- `runoff_volume_type`: Fixed (no infiltration)
- `runoff_coefficient`: 1.0 (100% runoff)
- `routing_model`: SWMM

### Template 2: Pervious (Horton)

Use for pervious surfaces with Horton infiltration method:
- **300-series**: Pervious surfaces combining soil × landcover

Key defaults:
- `runoff_volume_type`: HortonSWMM
- `runoff_coefficient`: 0.0 (infiltration-based)
- `routing_model`: SWMM

Fields overridden from databases:
- `initial_infiltration` ← `horton_f0`
- `limiting_infiltration` ← `horton_finf`
- `decay_factor` ← `horton_k`
- `drying_time` ← `horton_drying_time`

---

## Column Reference

### Primary Fields (Overridden by Generator)

| Column | Description | Source |
|--------|-------------|--------|
| `runoff_index` | Unique surface identifier | Generated (101+, 201+, 301+) |
| `surface_description` | Human-readable name | Generated |
| `runoff_routing_value` | Manning's n | `manning_n` from landcover DB |
| `initial_loss_value` | Depression storage (ft) | `depression_storage / 12` |
| `initial_infiltration` | Max infiltration rate (in/hr) | `horton_f0` (pervious only) |
| `limiting_infiltration` | Min infiltration rate (in/hr) | `horton_finf` (pervious only) |
| `decay_factor` | Horton decay constant (1/hr) | `horton_k` (pervious only) |
| `drying_time` | Soil drying time (days) | `horton_drying_time` (pervious only) |

### Template Fields (Defaults)

| Column | Impervious | Pervious | Description |
|--------|------------|----------|-------------|
| `runoff_routing_type` | Abs | Abs | Absolute Manning's n |
| `runoff_volume_type` | Fixed | HortonSWMM | Runoff calculation method |
| `surface_type` | Impervious | Pervious | ICM surface classification |
| `ground_slope` | 0. | 0. | Not used (subcatchment slope applies) |
| `initial_loss_type` | Abs | Abs | Absolute depression storage |
| `initial_abstraction_factor` | 0. | 0. | Not used with Abs type |
| `routing_model` | SWMM | SWMM | SWMM nonlinear reservoir routing |
| `runoff_coefficient` | 1. | 0. | Fixed runoff coefficient |
| `rafts_adapt_factor` | 1. | 1. | RAFTS adaptation factor |
| `equivalent_roughness` | 0.025 | 0.025 | Channel equivalent roughness |
| `number_of_reservoirs` | 1 | 1 | Nonlinear reservoir count |
| `depression_loss` | 0. | 0. | Additional depression loss |
| `max_infiltration_volume` | — | 0. | Max infiltration volume (0=unlimited) |
| `initial_loss_porosity` | 50. | 50. | Porosity for initial loss |
| `infiltration_coeff` | 1. | 1. | Infiltration coefficient |

### Additional ICM Columns

The template includes all 67 ICM columns. Columns not listed above use ICM defaults and are typically not modified for SWMM-style runoff modeling.

---

## Adding New Infiltration Methods

To add support for a new infiltration method (e.g., Green-Ampt):

1. **Add template row** with next available `runoff_index` (e.g., 3)
2. **Set `runoff_volume_type`** to the ICM method name (e.g., `GreenAmptSWMM`)
3. **Set appropriate defaults** for method-specific columns
4. **Update generator script** to use the new template index
5. **Create/update infiltration database** with method-specific parameters

---

## See Also

- [horton_infiltration_parameters.md](horton_infiltration_parameters.md) - Horton infiltration parameter reference
- [pervious_landcover_parameters.md](pervious_landcover_parameters.md) - Pervious surface parameters
- [impervious_parameters.md](impervious_parameters.md) - Impervious surface parameters

---

*Last updated: December 2024*

