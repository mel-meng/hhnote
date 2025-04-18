# Cannot import GIS layers into XPSWMM

source: Innovyze Support Portal

---

### Cannot import GIS layers into XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Cannot-import-GIS-layers-into-XPSWMM)

If you are having trouble importing GIS files into your XPSWMM model, one possibility is that it has a geometry XPSWMM doesn’t support.

To test it,

* create an empty model
* then load the gis layer into XPSWMM

![](images\1_q6dMbJ7JhBHnoMlzSpnABQ.png)

If nothing shows up in the map window, XPSWMM doesn’t support the shapefile.

The resolve the issue, we need to convert the shapefile into simple geometries.

Here is an example using ArcMap to fix the problem.

1. load the shapefile into ArcMap
2. Open the attribute table and check the geometry

![](images\1_4muZqkdGPz32F4pfyQ_mZw.png)

As shown above, for lines, XPSWMM only support Polyline, and we need to convert this from Polyline M to Polyline.

You can Google keywords such as “convert polyline m to polyline in xxxx” xxx is the software package you use.

Below shows how to get it done in ArcMap.

[**Converting shape Polyline-M to Polyline using ArcGIS Desktop?**  
*Thanks for contributing an answer to Geographic Information Systems Stack Exchange! Please be sure to answer the…*gis.stackexchange.com](https://gis.stackexchange.com/questions/9723/converting-shape-polyline-m-to-polyline-using-arcgis-desktop "https://gis.stackexchange.com/questions/9723/converting-shape-polyline-m-to-polyline-using-arcgis-desktop")

Once the shapefile is converted to simple geometry type, XPSWMM should be able to display it and thus import it.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [July 2, 2021](https://medium.com/p/448882dbbc82).

[Canonical link](https://medium.com/@mel-meng-pe/cannot-import-gis-layers-into-xpswmm-448882dbbc82)

Exported from [Medium](https://medium.com) on March 18, 2025.