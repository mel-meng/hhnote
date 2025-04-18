# How to compare NEXRAD with rain gauge data in ICM? — Part 2

source: Innovyze Support Portal

---

### How to compare NEXRAD with rain gauge data in ICM? — Part 2

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-compare-NEXRAD-with-rain-gauge-data-in-ICM-Part-2)

In [part 1](https://mel-meng-pe.medium.com/how-to-compare-nexrad-with-rain-gauge-data-in-icm-part-1-605c63437b94), we setup two models, one uses NEXRAD, and the other uses a single rain gauge from a time series stored in a TSDB.

What if we want to use both the rain gauge data and the NEXRAD rainfall in the same model, for areas close to the rain gauges, we would like to use rain gauges, and for areas too far away we would like to use the NEXRAD.

### Turn rain gauges into Spatial rainfall Polygons

In [part 1](https://mel-meng-pe.medium.com/how-to-compare-nexrad-with-rain-gauge-data-in-icm-part-1-605c63437b94), we created two TVD connectors for the two rain gauges as points and used the rainfall profile in the subcatchment properties to reference the data.

To use spatial rainfall, we need to create polygons instead of points for the rain gauges. When using spatial rainfall, instead of relying on the rain gauge IDs, the spatial relation between the rain gauge polygon and the subcatchment polygon will be used to determine the rainfall time series for the subcatchment.

As shown below, the two subcatchments that are completely within the TVD polygon will use the rain gauge data from that polygon, and subcatchment “Spatial” is crossing both TVD polygons.

![](images\1_jsC2P359V1yc9_AoXutIXQ.png)

### Area-averaged rain

By default, the rain gauge region that contains the centroid of the subcatchment will be used to provide rainfall data for the entire subcatchment. For very large subcatchments, where the subcatchment overlaps multiple rainfall polygons, this can mean that the simulated subcatchment rainfall is not representative of the rainfall over the subcatchment as a whole. Check the subcatchment Use area-averaged rainfall field to use data from all rain gauge regions that the subcatchment overlaps.

![](images\1_Gi8QI_gaU7i97RWTi5njjA.png)

If we don’t check the “Use area-averaged rain”, then RW\_PINN will be used for subcatchment “Spatail”, otherwise, an area averaged rainfall of both rain gauges will be used.

### Create Rain Gauge Polygons

Use the polygon tool to create the TVD connector,

![](images\1_z3eTkMi3k0ZQ2I4RVsgdhA.png)![](images\1_XzSH9J5wSpyNyEBv2G-d7g.png)

To use the TVD polygons to assign rainfall, we need to create a rain gauge network first.

![](images\1_BFvkDD8Ao1D6-8CIaejaxw.png)

We first need to group all the rain gauge polygons using the same category name “rg”, it can be anything meaningful for the project.

![](images\1_ih9cd-n4B9k60x4eDNJSsA.png)

Then, we add a record to the “Spatial rain source” tab,

1. switch to the spatial rain source tab
2. give the rain gauge network a name
3. choose the “Raingauge polygons” option to group all the polygons into one rainfall source
4. this the category name we defined in the TVD connector tab
5. give it a priority: when multiple sources are available using the priority to decide which source to use first

![](images\1_PXCYF5jTCZUHVtd01g7iOg.png)

### Spatial Rainfall Results

As expected, the rainfall are exactly the same for the subcatchments are completed within the rain gauge polygon.

For subcatchment “Spatial”,

when using profile: RW\_PINN

using centroid: exactly the same as RW\_PINN, since the centroid is in that rain gauge polygon

using area-weighted: much higher because RW\_GWRISSOM recorded more rainfall.

![](images\1_AzvgQmqWXrhtxCHox2R33g.png)

The sample model can be downloaded from [github](https://github.com/mel-meng/icm/tree/master/models/rainfall_tsdb).

In the next post, we’ll learn how to prioritize different rainfall sources.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 12, 2021](https://medium.com/p/3acc6e2f08b8).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-compare-nexrad-with-rain-gauge-data-in-icm-part-2-3acc6e2f08b8)

Exported from [Medium](https://medium.com) on March 18, 2025.