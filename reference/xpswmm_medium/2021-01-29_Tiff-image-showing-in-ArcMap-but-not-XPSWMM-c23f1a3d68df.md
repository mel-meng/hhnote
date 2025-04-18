# Tiff image showing in ArcMap but not XPSWMM

source: Innovyze Support Portal

---

### Tiff image showing in ArcMap but not XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/tiff-image-showing-in-ArcMap-but-not-XPSWMM)

Some of the images that are showing fine in ArcMap cannot be displayed properly in XPSWMM. The two common causes are,

* Different projection used for the image from the model
* XPSWMM doesn’t support the image format

### Set projection for image

For images that are saved in a different projection, they need to be projected to the same projection as the model. It can be easily done in ArcMap.

1. set up the dataframe using the model projection

![](images\1_SMj5eQi5nW2RJbdxaVr2Rg.png)![](images\1_nA4uf3EeXflZ6EWNYQSY9A.png)

2. Export the image using the dataframe projection

![](images\1_xqJ2srvg06Hs4PbZzgeZrg.png)![](images\1_HVHANMAwA0ziRocdT_1t9w.png)

3. For small modeling area, you can also export the map. Zoom to the area to be exported,

![](images\1_QqWknESCWaj5mw7YGHTiuA.png)![](images\1_d6sLrGiDauU8Fnnd3eIbkg.png)

### Convert to supported format

XPSWMM doesn’t support some images formats that renders fine in ArcMap. By using the render, it usually can fix the problem.

1. when exporting an image, make sure the output raster settings are checked as shown below.

![](images\1_OhJdCedy3MheWTTUZNaZ3w.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [January 29, 2021](https://medium.com/p/c23f1a3d68df).

[Canonical link](https://medium.com/@mel-meng-pe/tiff-image-showing-in-arcmap-but-not-xpswmm-c23f1a3d68df)

Exported from [Medium](https://medium.com) on March 18, 2025.