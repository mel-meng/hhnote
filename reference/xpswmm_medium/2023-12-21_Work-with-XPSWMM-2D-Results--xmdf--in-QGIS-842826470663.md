# Work with XPSWMM 2D Results (xmdf) in QGIS

source: github

---

### Work with XPSWMM 2D Results (xmdf) in QGIS

source: [github](https://github.com/mel-meng/hhnote/tree/main/workflow/data/xmdf)

### Introduction

[QGIS](https://docs.qgis.org/3.28/en/docs/user_manual/working_with_mesh/mesh_properties.html) offers native support for XPSWMM 2D results files, allowing you to access simulation results in their raw format without the need for conversions. This capability provides several benefits, including:

* The ability to use advanced visualization styles and animations for mesh in QGIS.
* An expanded range of options for converting results to other GIS formats.

![](images\0_qY99EKz7YVywR22X.png)

In this article, you will learn,

* Load XPSWMM 2D results into QGIS
* Rendering maximum values in the map
* Play animation of the simulation
* Export the results to raster format
* Export the results to vector format

### Load XPSWMM 2D results into QGIS

XPSWMM saves the 2d results in two files,

* \*. [2dm](https://www.xmswiki.com/wiki/SMS:2D_Mesh_Files_*.2dm): saves the mesh, and the terrain data
* \*.[xmdf](https://en.wikipedia.org/wiki/XMDF): saves the time series

To load the results into QGIS,

1. Load the \*.2dm file into QGIS. Drag the file into QGIS.

![](images\0_l8I84fDVBSlh9EIZ.png)

1. Load the \*.xmdf into the \*.2dm mesh

![](images\0_bFe4luWvTw-JTZEj.png)

### Rendering maximum values in the map

### Max. Depth

1. Select max. depth as the value to show

![](images\0_JeubG9Ri9jwU0Dmz.png)

1. Select the color ramp and make it transparent

![](images\0_Kwa_YzhO6tL8UMWS.png)![](images\0_3SswnLrfDyVBO-63.png)

### Play animation of the simulation

1. Set depth as the contours (fill), and velocity as the vector

![](images\0_RKIsJ4QBEgjXOBm3.png)

1. Set the depth style

![](images\0_wjL-7xNpRmNtX1OK.png)

1. Set the velocity style

![](images\0_mUzFQOyYZz3M1z7B.png)

1. Turn on the time control

![](images\0_MeWbZdUuORT2DTf9.png)

1. Play the animation

![](images\0_RV8bVwXwKGw398Lv.png)

1. You can explore more vector styles

![](images\0_-pelbvyqCVswX2Oa.png)

### Export the results to raster format

1. Turn on the processing toolbox

![](images\0_B_7rtEZ_N6msTut3.png)

1. Locate the Mesh tools

![](images\0_dD-guo5IoUiuLTps.png)

### Export max. water depth as raster

1. Open “Rasterize mesh dataset”
2. Set up the parameters for the tool

![](images\0_589wf55NSkZ8U0ob.png)![](images\0_sWObTxwTnbfTFj-E.png)

### Export max. water contour lines

1. Open the “Export contours” tool
2. Set up the parameters

![](images\0_SCrz4T1dwZ9vdPpJ.png)

1. Turn on the contour line layer

![](images\0_ck3OyZwOY7F52cfx.png)

### Export the results to vector format

1. Open the “Export mesh vertices” tool
2. Setup the parameters

![](images\0_gbzQ2sKCy10z0o9d.png)![](images\0_E3hML2mj2PdDNTH7.png)

### Conclusion

In conclusion, working with XPSWMM 2D results in QGIS provides benefits such as advanced visualization styles, animation capabilities, and options for converting results to other GIS formats. By following the steps outlined in this article, you can easily load XPSWMM 2D results into QGIS, render maximum values on the map, play animations of the simulation, and export the results to raster or vector formats. This integration enhances the analysis and visualization capabilities for water management and flood modeling projects.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [December 21, 2023](https://medium.com/p/842826470663).

[Canonical link](https://medium.com/@mel-meng-pe/work-with-xpswmm-2d-results-xmdf-in-qgis-842826470663)

Exported from [Medium](https://medium.com) on March 18, 2025.