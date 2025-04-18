# Using Breakline in XPSWMM

source: github

---

### Using Breakline in XPSWMM

source: [github](https://github.com/mel-meng/hhnote/tree/main/workflow/data/dtm/ex2_breakline)

### Introduction

XPSWMM represents the 2D surface using 2D grids, a Minecraft like scheme to build a very blocky world. As a result, important details that form the flow paths can be lost in that translation. Breaklines can help capture such ground features, you can add ridges such as “levee” to block the flow path, or gullies such as “ditches” to guide the flow path.

In XPSWMM, break lines can be thick or thin

* Thick breaklines will raise both the sides and the bottom of the cell, for example elevated wide roads (shown in Fig.2, points on sides and center indicate the raised elevations to match the break line)
* Thin breaklines only changes the elevation of the sides of a cell, for example, level walls. (shown in Fig.3, only the sides are raised.)

![](images\0_o6GEyNxTYv8WeRDK.png)

Figure Thick breakline example

![](images\0_RCbYTCWPu5hjYKU6.png)

Figure Thin breakline example

You can create thin breaklines inside XPSWMM, but for thick breaklines, you have to manually create the shapefiles and use flags to define it.

### Use the breakline tool in XPSWMM to create thin breakline

1. Use the starter model from [Ex1 QGIS](https://github.com/mel-meng/hhnote/tree/main/workflow/data/dtm/ex1_qgis),
2. After adding DTM, save it as “breakline.xp”
3. Turn on contour lines to identify the top of the road

![](images\0_i4ZCZ_7y54HGfHkc.png)![](images\0_K0cc2l6WNW-bH6eB.png)

1. Draw the center line of the road.

![](images\0_IEZ6ipKFErNUvbTl.png)![](images\0_nXI4TabJyuex0ax-.png)

Style the line to show vertex.

![](images\0_KpUxqgnr8ifS3pjZ.png)

1. Check the breakline profile.

![](images\0_b8HJ3dg-LDNjbc3V.png)

1. For example, you can tell if a vertex is off the high point.

![](images\0_Dozbl_J-vJNstKfc.png)

1. Save the model and run it.

### Review thin breakline results

Refer to [Ex1 QGIS](https://github.com/mel-meng/hhnote/tree/main/workflow/data/dtm/ex1_qgis) on loading the check files into QGIS and then compare the elevation of the 2D and DTM.

1. Export the breakline from XPSWMM, as a polyline shapefile file

![](images\0_H_CWMPtER-dSpxQ2.png)![](images\0_wZwZZeS1KqRU2-PB.png)

1. Start QGIS load the breakline exported from XPSWMM
2. Load the check files from folder using Tuflow Plugin, and only keep the following layers

![](images\0_7aKGqCUP52GoWRwM.png)

1. In the map we can see the processed 2D grid translated the breakline into changes to sides of the cells

![](images\0_-6sNSVcuT50NBL6G.png)

1. Next, we’ll check the values of the sides in the profile. Update the elevation of the breakline\_zsh\_zpt\_check\_P

![](images\0_nFsXdE3TXnpXxHcl.png)

1. Refer to [Ex1 QGIS](https://github.com/mel-meng/hhnote/tree/main/workflow/data/dtm/ex1_qgis) to update the elevation for the grd\_check\_r layer and the DEM layer.
2. View the elevation profile

![](images\0_AJ73VcOA1WGlVA24.png)

1. Compare the elevations: (1) click the select line tool (2) click the breakline (3) review the profile

![](images\0_c4uQoA5lMFLtbhmW.png)

1. Add a 5m buffer to include the points along the sides in the profile

![](images\0_nUdhx5ipjbmA9tfc.png)

1. As the figure shows, although the cell elevation is not changed, the sides are elevated to match the breakline.

![](images\0_RbFdgAobxWfY7l9w.png)

### Use the asc\_to\_asc tool to add thick breakline

Tuflow has a free [asc\_to\_asc](https://wiki.tuflow.com/index.php?title=ASC_to_ASC#Extract_Breaklines_from_DEM) tool that can extract breaklines from an existing line. You can find the tool from the [download](https://www.tuflow.com/downloads/) page or the tutorial [dataset](https://wiki.tuflow.com/index.php?title=Tutorial_Introduction).

![](images\0_4UbpDkNcEotVegFp.png)

The asc\_to\_asc tool is a command line tool,

* Create the breaklines as shapefiles
* Run the asc\_to\_asc tool to generate the breakline and elevation point shapefiles
* Add the geometry commands in XPSWMM to reference the breakline shapefiles.

### Create the breakline shapefile

The asc\_to\_asc tool has strict requirement on the geometry and attribute settings for the input breakline shapefile, use the breakline\_template.shp (./data/gis/breakline\_template.shp) as a template, you can redefine the projection to fit your project, and then start digitizing or copy the polyline from another file. It has the following fields.

![](images\0_aAfB_I61OdbF8FIU.png)

Refer to Table 6–8 2D Z-Shape (2d\_zsh) Attribute Descriptions in the [Tuflow Classic/HPC Manual](https://www.tuflow.com/downloads/) for more information.

* Z=99999, not used by this tool but used by Tuflow.
* dZ=0, means no adjustment of the height
* Width=5, means it is a thin line, and it will get the exact Z from DEM at the location. If it is greater than 0, then the tool will search around the point using the width as a radius for the highest point
* Options=MAX, this is a ridge breakline used to raise the elevation.

It is important to set the Width the same as your grid size for the thick breakline to work.

For simplicity, you can save the asc\_to\_asc.exe, DEM and breakline to the same folder.

![](images\0_99a-wKddCpUaiYXD.png)

In the command line window,

* Change to the folder where the tool and all the data are located: chdir “folder path”
* Run the asc\_to\_asc tool: asc\_to\_asc\_w64.exe -brkline breakline1.shp DEM.asc

![](images\0_4H4nLwwpPGuWS9Lv.png)

It will generate two files which can be used as the input for the breakline,

* breakline1\_brkline\_P.shp: the point layer with elevation extracted
* breakline1\_brkline\_L.shp: the line layer showing the line

![](images\0_Hwrli42P5B2QKyii.png)

### Setup XPSWMM flags for thick breakline

Once the line and point layers are ready, we can enter the XPSWMM flags.

1. Enter the control file and geometry control file commands. (3) will export all the check files in shapefiles format, (4) will use the layers to enforce thick breaklines

![](images\0_3nauBHAYqrFQWXL-.png)

For the value in (4), XPSWMM has limit on the length of the value, you need to keep the path short. As shown here, the first is the breakline layer, and the second is the point layer.

C:\tmp\A\breakline\_brkline\_L.shp|C:\tmp\A\breakline\_brkline\_P.shp

1. Save the model and run it.
2. Refer to [Ex1 QGIS](https://github.com/mel-meng/hhnote/tree/main/workflow/data/dtm/ex1_qgis) to load the check files, and compare the elevations. As shown below both the sides and the cell elevations are raised.

![](images\0_RCNMsDUKV0grmKxg.png)

### Use elevation shape in XPSWMM

There are other terrain editing tools inside XPSWMM such as fill areas and elevation shapes to apply changes to an area.

1. Create a new elevation shape layer

![](images\0_pd7fMvpwcA4Zc6Dm.png)

1. Select the layer, then draw a polygon, and set the new elevation.

![](images\0_LsBn0ilx3XLB9Xyz.png)

1. Refer to [Ex1 QGIS](https://github.com/mel-meng/hhnote/tree/main/workflow/data/dtm/ex1_qgis) to load the check files, and compare the elevations. As shown below the area is lowered to 40m.

![](images\0_5qfDrv5R4Nj_3zIi.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [December 7, 2023](https://medium.com/p/efe52d7d3888).

[Canonical link](https://medium.com/@mel-meng-pe/using-breakline-in-xpswmm-efe52d7d3888)

Exported from [Medium](https://medium.com) on March 18, 2025.