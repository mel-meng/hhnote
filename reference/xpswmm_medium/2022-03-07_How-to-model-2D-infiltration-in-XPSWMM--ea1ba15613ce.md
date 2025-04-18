# How to model 2D infiltration in XPSWMM?

source: Innovyze Support Portal

---

### How to model 2D infiltration in XPSWMM?

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-model-2D-infiltration-in-XPSWMM)

XPSWMM 2D can simulate infiltration at the cell level when water is flowing through the cells. Although in XPSWMM you can define both the manning’s n and the infiltration in a single landuse entry. For simplicity and flexibility, usually it is a good idea to treat manning’s n and infiltration as two different type of landuse entries.

For example, you have 5 different type of landuse, and 3 type of soils for infiltration. In you define both landuse and soil in the same landuse, then for each combination you’ll have to create a new landuse, e.g. road with soil A, road with soil B, etc. As you can see, it can get complicated very quickly. A simpler way is to treat landuse and soil as two different type of input without mixing them up. And that is the approach we will show in this article.

### Define landuse

As shown below, we first need to define manning’s and infiltration as separate landuse entries in the global database.

5: For manning’s n entries, we only check the “landuse” checkbox

6, 7, 8: For infiltration entries, we only check the “Infiltration” checkbox, then define the soil infiltration parameters.

![](images\1_lMVb6sXdSHhBkQ5bSlIoVA.png)

### Draw the polygons

There are 3 ways to get the manning’s n, and soil type polygons into XPSWMM.

* draw the polygon directly inside XPSWMM

![](images\1_Buh75smyNUxW7cBIBTcxkg.png)

* import from a shapefile

![](images\1_o7WF9jVQ3FPRnYD1Yma23Q.png)

* using the external references (another blog will cover the steps)

![](images\1_enPfXcHlw2ebu18f3qL5OQ.png)

### Default landuse

We’ll need to define a default landuse for the model. When soil infiltration is used, we should provide the default landuse with an infiltration type defined.

![](images\1_UQD6M51PWUymLE7oIYNCkA.png)

An easy way to define a soil that doesn’t infiltrate at all is setting the IL/CL (initial/continuous infiltration to 0)

![](images\1_aMkYONSfB45AHHV9SmIKtg.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [March 7, 2022](https://medium.com/p/ea1ba15613ce).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-model-2d-infiltration-in-xpswmm-ea1ba15613ce)

Exported from [Medium](https://medium.com) on March 18, 2025.