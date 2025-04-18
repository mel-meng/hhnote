# Modify the digital terrain model for a 2D model

Source: github, Innovyze Support Portal

---

### Modify the digital terrain model for a 2D model

Source: [github](https://github.com/mel-meng/hhnote/tree/main/workflow/data/dtm/modify_elevation), [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Modify-the-digital-terrain-model-for-a-2D-model)

### Introduction

Modifying the elevation of an existing DTM is a common task when modeling a 1d/2d model in XPSWMM to ensure correct flow paths. For more advanced manipulation of the surface, it is important to review the surface after the changes, you’ll need specialized GIS tools outside of XPSWMM for this task.

NOTE: in this article, DTM (digital terrain model), topo, surface are used interchangeably, the data representing the surface water flows on. DTM and topo usually refers to the source data, and surface sometimes implies the calculated results.

In this article you’ll learn how to install these tools, and use them to ensure the desired changes are made to the surface.

You will need to install:

* Install [QGIS](https://www.qgis.org/en/site/)
* Install [Tuflow](https://wiki.tuflow.com/index.php?title=TUFLOW_QGIS_Plugin) QGIS plugin
* Install Profile QGIS plugin

This tutorial is based on [Module 02](https://wiki.tuflow.com/index.php?title=Tutorial_M02) on the Tuflow website. You will add 3 break lines to represent the roads.

![](images\0__QnmKeMhPWF_JcUX.png)

### 2D Grid

The 2D engine sees the world as cells (or cubes in 3D). It is a fixed grid with rectangle cells defined by the user, which is very similar to how Minecraft models the world. For more details, refer to the [Tuflow Manual](https://www.tuflow.com/downloads/). The actual surface your 2D model uses can be very different from your DTM, therefore, you’ll need GIS tools to compare your 2D surface with the DTM for models with more complicated terrain.

![](images\0_pUB5EpZRjgMmeuK4.png)

Figure Minecraft models the world as blocks

As shown in Figure 6–1 from the manual, each cell has 4 points, and each point will have an elevation sampled from the underlying topo data.

* ZC: the center point of the cell, it represents the bottom of the cell
* ZU/ZV: controls how water moves between cells, you can use breakline to raise the elevation of the sides of the cell to act like fences

![](images\0_QLK47EDao4Eab29Z.png)

The goal of manipulating the 2D surface is to change the values of the elevation at the ZC, ZV and ZU points, so that water will flow through your intended path.

### Breaklines

There two types of breaklines,

* Thin breaklines only changes the elevation of the sides of a cell, for example, level walls.
* Thick breaklines will raise both the sides and the bottom of the cell, for example elevated wide roads

![](images\0_TdoCtwHk5AaHJyEw.png)

Figure Thick breakline example

![](images\0_DM0ua36VsrwzIpNC.png)

Figure Thin breakline example

You’ll complete the following exercises,

* [Exercise 1 Compare 2D grid with DEM](https://github.com/mel-meng/hhnote/blob/main/workflow/data/dtm/modify_elevation/Exercise%201%20Compare%202D%20grid%20with%20DEM.md)
* Exercise 2 Create Breakline (TODO: add link)

### Data files

Data files can be found in the “data” folder,

* Aerial\_Photo
* grid: topo data and related shapefiles
* model: XPSWMM model files

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 19, 2022](https://medium.com/p/862ad6bb04ed).

[Canonical link](https://medium.com/@mel-meng-pe/modify-the-digital-terrain-model-for-a-2d-model-862ad6bb04ed)

Exported from [Medium](https://medium.com) on March 18, 2025.