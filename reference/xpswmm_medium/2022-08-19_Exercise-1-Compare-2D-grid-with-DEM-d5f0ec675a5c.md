# Exercise 1 Compare 2D grid with DEM

source: github, Innovyze support portal

---

### Exercise 1 Compare 2D grid with DEM

source: [github](https://github.com/mel-meng/hhnote/blob/main/workflow/data/dtm/modify_elevation/Exercise%201%20Compare%202D%20grid%20with%20DEM.md), [Innovyze support portal](https://innovyze.force.com/support/s/article/Exercise-1-Compare-2D-grid-with-DEM)

In this exercise, you’ll use QGIS to compare the input DEM, and the 2D engine created 2D surface.

1. Open the “./data/model/starter\_model.xp”
2. Change the 2D settings to generate check files.

![](images\0_e1c7GXq3OsxWxw_p.png)

1. Change the GIS output files to shapefiles.

![](images\0_pYGFUW1_RZPOc6Z3.png)

NOTE: this will break the diagnostics, which uses the \*.mif format. If you need to check the diagnostics, remove this line.

![](images\0_9mYHyBWIDdl71Jne.png)

1. Update the dem path.

![](images\0_28Piik-rR6dbsPOZ.png)

1. Run the model to generate the check files. You can stop the simulation once it starts. All the 2D related files are saved in the 2D folder defined in the 2D settings.

![](images\0_vHrAJgVpGF01jewX.png)

* Check: all the check files
* Data: all the Tuflow 2D model input and control files
* Log: logs, and diagnostic files
* Output: results

1. Start QGIS, and load the DTM file.
2. Load the 2D engine generated surface, it is in the “Check” folder with the name \*\_DEM\_Z.flt.
3. Open the profile tool and load both dem layers

![](images\0_pLbR0qxfFgSAwYuK.png)

1. You can change the color of each layer, and compare the profile of the street

![](images\0_4YRy9YvrFrKIYX7q.png)

As shown in the profile, red is the raw DEM, and blue is the 2D engine generated surface. Due to the resampling of the grid, we can see the 2D generated surface is not as smooth as the raw input (red). Therefore, we’ll need to create a breakline to ensure the high points of the roads are correctly represented.

1. To get better understanding why this happens, you can load the grid check file showing the 2d Grid. (1) drag the \*\_grd\_check\_r.shp to QGIS (2) select the layer (3) click on the style button to apply Tuflow style.

![](images\0_qSyQmXokps5aoKJk.png)

1. Change the DEM layer style to hillshade.

![](images\0_-QcYAB3-OkfF5arz.png)

As shown below, many cells are sitting on the slope of the road, as a result, the average elevation of the cell is much lower than the top of the road.

![](images\0_xNYl67kOXQoqJPxk.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 19, 2022](https://medium.com/p/d5f0ec675a5c).

[Canonical link](https://medium.com/@mel-meng-pe/exercise-1-compare-2d-grid-with-dem-d5f0ec675a5c)

Exported from [Medium](https://medium.com) on March 18, 2025.