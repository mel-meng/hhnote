# Common GIS conversion tasks for Modeling

source: Innovyze Support Portal

---

### Common GIS conversion tasks for Modeling

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Common-GIS-conversion-tasks-for-Modeling)

GIS has many formats and from time to time you might have a GIS data format that your modeling software doesn’t support.

We will show a few common conversion tasks,

* projection conversion
* complex to simple geometry
* format conversion

We will use ArcMap as an example for the conversion.

### Projection Conversion

Projection might be the most confusing part of GIS data, the earth is a 3D sphere, and when drawing a map on a 2D surface, we’ll need complicated math models to define the earth shape, and then the rules how to project the 3D surface to a 2D surface.

As far as modeling is concerned, we live in a 2 dimension world. Everything comes in with an X and a Y, when we overlay different layers in the same model, they need to use the same set of reference system.

For modeling packages such as XPSWMM which can only load data using the same coordinate system, the modeler needs to convert all data sources to the same system.

For modeling packages such as ICM which supports projection, each layer of the data should have its projection correctly defined.

Due to the complexity of projection conversion, it is highly recommended to convert all your key source data into the same projection regardless if the modeling package support on-the-fly projection or not.

Typical work flow,

* load all the layers into ArcMap to figure out the projection of each layer
* define the projection for layers with missing projection information
* convert the data to the desired projection

1. load your layers into ArcMap
2. Check the projection of the data frame

![](images\1_LhEQiFqq8R8it_IDxCK5Gg.png)![](images\1_6DdpKerOkYc_lYdofqh1Pg.png)

3. Use the base map to check the projection.

![](images\1_ddP2oP2lTjxvx5d9-DthAA.png)

4. change the projection of the data frame to find the projection that lines up with the data

![](images\1_HfBHIPDEOFuwYsWYO-NR3g.png)

5. To define the projection, search “projection” in the tools

![](images\1_D7ywpjLThAQ2b6zj0TsT7w.png)![](images\1_GtX9uqSvR_473uODlS6BJA.png)![](images\1_-iRmycFAf6XWD1SFOUmI9w.png)

4. Convert to a different projection. You can use the toolbox, or you can change the data frame projection to the desired projection and simply export the layer using the data frame projection

![](images\1_WG1HwMV3zqO_UYF-WjFi3w.png)![](images\1_3CeS3vAspmnGVtrUqDDlwA.png)

### Complex to Simple Geometry

Most modeling software only support simple geometry type, point, polygon and polyline. Anything other than these should be converted to remove the complex components.

Open the attribute table of the layer and check the shape column, in the example below, we need to remove the “ZM”

![](images\1_A_CHjqR4DlV_rl6UCmxLZQ.png)

To remove the “ZM”, we’ll need to use the toolbox and change the environment settings.

![](images\1_SKk-BV85ys0deLJ-uhqEpw.png)![](images\1_-L-BaueGYXK2Ew73mzDQHA.png)

This will convert the geometry to simple geometries.

![](images\1_mYSrCkX6QtB1Z3JWoKo7Cg.png)

### Donut Polygon

Another common issue is donut polygon. When working with City wide land use data, we often have polygons with holes in it.

![](images\1_FdnQcaXhlbxRHDfH2auVfA.png)

Most modeling packages have trouble recognizing the holes in these polygons.

![](images\1_viRkEYAlJZkqb2WSujPEhg.png)

To fix this issue, we can cut the polygon through the holes.

![](images\1_PWbgzXDXDwsrN2DraQW7tw.png)

Turn on the editor toolbar,

![](images\1_If24CNp0LLzyXQ_8IX800A.png)

select the polygon with holes

1. click the cut polygon tool
2. draw a line through all the holes

After that the modeling software can correctly render the polygon

![](images\1_57JePhT7uzMvqtpiRN24oQ.png)

### Batch Opening Donut Polygons

If you have a lot of donut polygons, instead of manually drawing lines to cut the donut polygons open. You can create a regular grid and then intersection the donut polygon layer with the grid polygon layer. The result will be a polygon layer with all the donuts cut open.

### Format Conversion

Most of the format conversion can be done by exporting a layer or using the toolbox.

![](images\1_cwAKHypu9O25quN31lAtHg.png)![](images\1_ZBKgRabxN5BUD4qwmchujQ.png)

You can also search the toolbox,

![](images\1_xp0H4yhTkx4nuIN7FvPKvw.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [July 16, 2021](https://medium.com/p/1d344b326c0a).

[Canonical link](https://medium.com/@mel-meng-pe/common-gis-conversion-tasks-for-modeling-1d344b326c0a)

Exported from [Medium](https://medium.com) on March 18, 2025.