# Display XPSWMM 2D modeling results in QGIS

XPSWMM has powerful mapping functionalities for rendering the 2D results, and that can meet most common reporting and analysis needs.

---

### Display XPSWMM 2D modeling results in QGIS

XPSWMM has powerful mapping functionalities for rendering the 2D results, and that can meet most common reporting and analysis needs.

For projects that will require customized mapping, it is common to export the results as GIS files and then using GIS software to create the maps.

One of the less known data format of 2D modeling is the [mesh data format](https://docs.qgis.org/3.16/en/docs/user_manual/working_with_mesh/mesh_properties.html), a format that stores large spatial temporal dataset.

With native support of mesh data, 2D results can be rendered in QGIS with just a few clicks.

### What is a mesh?

For XPSWMM, the most common mesh is the fixed 2D grid. And for each grid, we have 2D simulation results for depth, velocity, etc.

In XPSWMM, the mesh data is saved in the 2D folder,

* \*.2dm stores the 2D grid (mesh)
* \*.xmdf stored the time series results for each grid

![](images\1_RhWyEEL6IloIKuufD_5EZA.png)

### Load mesh into QGIS

To load the mesh into QGIS,

* load the mesh file
* add the results into the mesh

![](images\1_y8WR9gUwymINruyGiFRuBw.png)

### Load the results

Right click the layer to go to the properties, then add the xdmf file.

![](images\1_7v0obY8IoM0L9qejgRI3IQ.png)![](images\1_l_nA8A7hIewGUcFENaV5ZA.png)

### Select the results to render on the map

Uncheck all the results, then check the max. depth and velocity

![](images\1_W4tjaFexmZkTdS23KqtC0w.png)

### Style the selected results

1. go to symbology
2. enable max depth as surface
3. enable max velocity as vector (e.g. arrows)

![](images\1_5n8UI4Y51-nmFLyakL_qVQ.png)

To style the surface/contour,

![](images\1_eCukcvtjFGL57qe40sg0zQ.png)

To style the vector,

![](images\1_cf-pgg5Q8m3lTk8Usnha-Q.png)![](images\1_K1k6tRohMTOlBoj73pjDjQ.png)

Arrows

There are several interesting vector renderings that XPSWMM doesn’t offer yet.

![](images\1_HT0U_Nw2fLSlUoS8N5PJbg.png)

Streamlines

![](images\1_Wp5_yNUYo9jsU2i07rQ2JA.png)

Traces

### Playing Animation

To play animation, turn on the animation toolbar.

![](images\1_JmWFU-qlkSwpTolupKd8rg.png)

Then we need to load the time series results.

Go to the mesh layer properties, select the depth surface and velocity vector, make sure it is not the max/min values.

![](images\1_2AYfllkECq-xAKt4b1vrBQ.png)

Go through the same steps to setup the symbology.

In the temporal controller, select the mesh layer

![](images\1_5mMb4K0OrkZDBY_kkoAHvA.png)![](images\1_EjfhMDSFlQkHIAf4M6SlZA.gif)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 24, 2021](https://medium.com/p/d708d9438001).

[Canonical link](https://medium.com/@mel-meng-pe/display-xpswmm-2d-modeling-results-in-qgis-d708d9438001)

Exported from [Medium](https://medium.com) on March 18, 2025.