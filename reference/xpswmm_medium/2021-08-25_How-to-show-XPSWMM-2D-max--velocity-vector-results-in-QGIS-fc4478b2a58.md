# How to show XPSWMM 2D max. velocity vector results in QGIS

Source: Innovyze support portal

---

### How to show XPSWMM 2D max. velocity vector results in QGIS

Source: I[nnovyze support portal](https://innovyze.force.com/support/s/article/How-to-show-XPSWMM-2D-max-velocity-vector-results-in-QGIS)

The velocity vector shows how the water flows through the surface, it can be a great tool to help understand the causes and impacts of surface flooding when reviewing 2D simulation results.

Although XPSWMM has powerful rendering engine to show the 2D results, from time to time, engineers and communities might need to create maps in GIS software packages to combine other sources information and create customized maps. In this article, we will use QGIS to render the max. flow velocity vectors.

![](images\1_0EM76Q3KHP3dMDfQ_mA5ew.png)

Rendering the velocity in QGIS takes just a few steps,

1. Export the max. velocity vector as a point shapefile
2. Add the shapefile and create the symbiology for the vector

### Export max. velocity vector

Use the XP2D Utility Interface tool to extract the velocity data from the xmdf file.

![](images\1_4zTGL18DsqhJ4wgZBwF4UQ.png)![](images\1_Oy4_atcvwXmryxzzRLAi7w.png)

### Style vector in QGIS

Load the shapefile exported from the previous step into QGIS

![](images\1_ayhiAqT1rhijZJHNOHRynQ.png)

1. double click the layer to open the properties
2. change the marker type to vector field maker

![](images\1_DZ6JER5Y52jEpoUCtCJ0Dg.png)

The velocity vector is represented using polar coordinate system,

* x: the length
* angle: the angle

Follow the instructions below set the mapping of the fields and the coordinate system.

You might need to adjust the scale factor so that the lines look OK.

![](images\1_lkdcRSYvs1-EeTGjSW_4jQ.png)

Adding arrow to the end of the vector,

1. adding a new marker line symbol
2. specify only show the marker at the end of the link

![](images\1_L5CtdQjCm3CqrtxFZPv_Og.png)

Change the symbol to arrow,

1. select simple marker
2. change it to an arrow

![](images\1__ee9uNyHVWeermkxKHVUtQ.png)

to change the size of the arrow,

1. select Maker
2. change the size
3. apply and view the results (4)

![](images\1_oxqceFwR3OO3cOnX-l1-Cg.png)

To change the color of the arrow based on the velocity,

1. change to graduated symbol
2. change the color
3. select a color ramp
4. classify to add the entries (5)

![](images\1_452SuE7SuICZgJGgOc58sw.png)

To reuse the style,

![](images\1_4cTY-HDzbjCV-WhImVxxLw.png)![](images\1_2ySD4E4gQtd1XjGX_QO5jQ.png)

For very small grid size, the number of velocity vectors can make it hard to see the arrows when zoomed out. In this case we can apply a random sampling to only show some of the vectors.

First we need to create a new column in the point layer to classify the points into different groups.

![](images\1_hqKyiYzVFxf5NBA5Ibjzjg.png)

1. enter edit mode
2. create a new column group
3. make sure you are updating group
4. generate random number from 1 to 50 (I need to show 1 out of 50 points, it depends on your actual situation, play with this number)
5. update the values of group column

![](images\1_raWF1NvmH74pkBKxU3ictQ.png)

Next we are going to filter the layer only showing group 1.

1. double click the layer to open the properties
2. go to source and enter the filter of group 1

![](images\1_m4obgnlKojuOnNmgxvmPcw.png)![](images\1_Z6ovf5fLHWk2zouxFbZSyw.png)

You can also change the grid size while exporting the vector using the XP2D utility to down sampling the results.

![](images\1_gMm4SMYpzRigPM-4owokVA.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 25, 2021](https://medium.com/p/fc4478b2a58).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-show-xpswmm-2d-max-velocity-vector-results-in-qgis-fc4478b2a58)

Exported from [Medium](https://medium.com) on March 18, 2025.