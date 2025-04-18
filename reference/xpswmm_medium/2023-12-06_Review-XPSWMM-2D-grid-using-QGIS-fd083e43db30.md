# Review XPSWMM 2D grid using QGIS

source: github

---

### Review XPSWMM 2D grid using QGIS

source: [github](https://github.com/mel-meng/hhnote/tree/main/workflow/data/dtm/ex1_qgis)

![](images\0_XJxiRglMIjaC3EeW.png)

### Introduction

For XPSWMM 2D models with a lot of manual terrain modifications, it is important to review the engine processed 2D grid to make sure all the modifications are correctly applied.

With the help of the Tuflow plugin, QGIS is a great tool for the task. In this article we will go through a few examples to learn,

* Setup the XPSWMM model to generate check files as shapefiles
* Install QGIS and the Tuflow plugin
* Compare the 2D grid and the DEM

### Setup the XPSWMM model to generate check files as shapefiles

In this exercise, you’ll use QGIS to compare the input DEM, and the 2D engine created 2D surface.

1. Open the “./data/model/starter\_model.xp”
2. Add background, “./data/gis/Aerial\_Photo\_M02.jpg”

![](images\0_k3e0DUuZXw7lwylD.png)

1. Add DTM, “./data/gis/DEM.asc”

![](images\0_ThLGnBGsoctv5t0w.png)

1. Change the 2D settings to generate check files.

![](images\0_NNQT-J3UpavkWUei.png)

1. Change the GIS output files to shapefiles.

![](images\0_1fG-jFL64bht-yGJ.png)

1. Save the model as run1.xp
2. Run the model, ignore the initialization error.

![](images\0_nZ1WFYeahs8i0Cjx.png)

1. Go to the model folder “./2D/Check”, you should see a long list of files. Next, we will review these files in QGIS.

![](images\0_TzNF40x8PoV_Po0Q.png)

### Install QGIS and the Tuflow plugin

Follow the instruction links to install [QGIS](https://www.qgis.org/en/site/) and [Tuflow](https://wiki.tuflow.com/index.php?title=TUFLOW_QGIS_Plugin) QGIS plugin.

### Load the 2D grid and the DEM into QGIS

1. Start QGIS, and load the DTM file, “./data/gis/DES.asc”.
2. Load the check files using the Tuflow plugin

![](images\0_IZ4G1rMc-05bBIhG.png)![](images\0_3Gsvzb0PPb-eGPjn.png)

### Compare the 2D grid and DEM profile

1. Keep only the DEM and “run1\_grd\_check\_R” turned on, and open the “Elevation Profile”

![](images\0_LaHm9GU6wpdynAKb.png)

1. Double click on DEM layer to turn on “Represents elevation surface”

![](images\0_6Z8TsjyynSG3BFtv.png)

1. Double click the “run1\_grd\_check\_R” layer to set the elevation

![](images\0_RJg7rEyOHbasRXDp.png)

1. Now you can use the elevation profile tool to cut cross sections.

![](images\0_2YmtmIRc-XpC5C-n.png)

1. Change the DEM style to hill shade to highlight steep slopes.

![](images\0_bmL9CpHGbLRjCzB5.png)

1. Study how the 2D grid is representing the culvert area. The highlighted cell represents the average elevation mostly of the bank, therefore, it is much higher than the DEM. Let’s try using a finer grid.

![](images\0_eQyKt5qbobr-0-pm.png)

### Comparing 1m vs 6m grid

Using a finer grid should help capture the DEM, you will create a new model with 1m grid size, then compare the 2D check files for the grid.

1. Save the XPSWMM model as run2.xp
2. Change the 2D grid size from 5m to 1m

![](images\0_9CDwBncT8aczH_Gf.png)![](images\0_tV9lWMSovncBOT6n.png)

1. Save the model, then run the model
2. The check grid file for this model will be named in the same folder with a prefix of “run2”.
3. Drag the grid file for run2 to QGIS, and setup the elevation with the same settings as the run1 grid, now we can compare the profiles. As you can see the green lines (1m) are tracking the DEM much better than the red lines (5m)

![](images\0_KKTNwXHiUaaCyyfY.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [December 6, 2023](https://medium.com/p/fd083e43db30).

[Canonical link](https://medium.com/@mel-meng-pe/review-xpswmm-2d-grid-using-qgis-fd083e43db30)

Exported from [Medium](https://medium.com) on March 18, 2025.