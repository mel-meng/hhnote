# How to update your existing 2D surface in XPSWMM

source: Innovyze Support Portal

---

### How to update your existing 2D surface in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-update-your-existing-2D-surface-in-XPSWMM)

When building a 2D model, updating the existing 2D surface is a common task,

* add more details to the surface, such as adding breaklines for road
* add proposed structures, such as new buildings, roads and ponds

In XPSWMM, you have a few choices:

* Updating the surface in a 3rd party software such as Civil3D or ArcMap
* Using a layered approach to combine a few DTM layers
* Adding breaklines and elevation shapes

### Updating the surface in a 3rd party software such as Civil3D or ArcMap

If you are designing a project in Civil 3D, this will be the easiest way to get your updated surface into XPSWMM.

* In Civil3D, export your surface as a LandXML file
* In XPSWMM, import the LandXML file

![](images\1_bS-jDRdRsoILDcfRW7Cu8g.png)

In general, if you need to make a lot of changes to your surface, CAD or GIS has more powerful tools to get the job done.

### Using a layered approach to combine a few DTM layers

For example, we need to add a pond to the existing surface.

* the existing surface is a flat surface at 10 ft
* the proposed pond is 10 ft deep

![](images\1_HyPHFRQ0PeS3oWVMN1S4zQ.png)

You can try the following,

* create a new DTM that shows the surface for the proposed pond

![](images\1_uAj8ZFfpB1NIMXfguiriCA.png)

* then add it to your model, and make sure it is on top of the existing flat surface

![](images\1_QihO4BQE96TSKi_9ItmRog.png)

For simple geometries, it can be directly created using the Build DTM tool. As shown below, we can easily define the pond using two rectangles

![](images\1_D-moKl0av8R-WIan56bguw.png)

### Adding breaklines and elevation shapes

A more advanced approach is to use the built-in tools to add breaklines and elevation shapes into the model.

First you need to create the layers under the Topography group.

![](images\1_NBLdNfgBS0YVkfkQea7a6g.png)

For the same pond, you can use a fill area to represent the bottom, and a elevation shapes to represent the sides.

NOTE: the end results is a change of the elevation of the cell. Turn on the grid for better reference, the line should go through the middle of the cell to apply the changes.

Add a fill area from the bottom with elevation of 1.

![](images\1_yEyMeHnv4X9Rj_CWfyrMCg.png)

add elevation shape for the 4 sides.

![](images\1_DTa8gPVV3h6cjglKUsa9Kw.png)

Below is the final result,

![](images\1_FU3eLGQb2Ti-Q4HXHx6wlw.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [March 17, 2022](https://medium.com/p/bd0f198a639e).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-update-your-existing-2d-surface-in-xpswmm-bd0f198a639e)

Exported from [Medium](https://medium.com) on March 18, 2025.