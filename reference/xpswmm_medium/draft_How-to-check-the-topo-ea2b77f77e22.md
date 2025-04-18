# How to check the topo

EX9: Review Input data with QGIS Plugin

---

### How to check the topo

### EX9: Review Input data with QGIS Plugin

Tuflow can generate check files for more close review of the input data. The most important file to review is the grid check file, which is the most important input for the 2D engine. With the Tuflow QGIS plugin, you can easily check the results.

1. Install QGIS and the Tuflow Plugin (<https://wiki.tuflow.com/index.php?title=TUFLOW_QGIS_Plugin>)

2. Enable check files and change the file format to shapefiles

Add a control file command: GIS Format: SHP. This will break some of the functionalities of XPSWMM which assumes \*.mif files are generated. For example, the diagnostics file will not load.

3. Re-run the model. The check files will be created in **/2D/Check**.

4. Start QGIS and Tuflow Plugin.

.

The Run ID is the model name. Go to the Check folder, it is the first part of the shapefile name.

5. The layer we want to check is the XX\_grd\_check\_R.shp file. It is the grid file.

You can easily check the input data from this shapefile. You can check if the Quadtree is correctly applied, the invert elevation of cells, the infiltration and manning’s n values etc.

[View original.](https://medium.com/p/ea2b77f77e22)

Exported from [Medium](https://medium.com) on March 18, 2025.