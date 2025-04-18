# How does ICM model manhole

source: Innovyze Support Portal

---

### How does ICM model manhole

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-does-ICM-model-manhole)

ICM assumes a manhole has two part, a shaft and a chamber.

![](images\1_2d_xIWy064-3XNo7Z9VMLw.png)

The default values works fine for most manholes, just set the “#D flag” for the input parameters, ICM will calculate the parameters for you.

![](images\1_-Dn-gfAr4nuMYZO-aRAcoA.png)

According to the help file, the defaults are

* chamber roof level: maximum of all soffit levels (pipe crown)
* chamber floor level: min. of invert levels
* chamber plan area: a circle with a diameter of the large pipe width(m) + 0.762 (m)
* shaft plan area: same as default chamber plan area

As shown below, when I have large diameter pipes, I need to reduce the size of the shaft area, and view the changes in 3D view.

![](images\1_nG6QHH78R6cs7MWG_IYNUQ.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 1, 2021](https://medium.com/p/888817e106cc).

[Canonical link](https://medium.com/@mel-meng-pe/how-does-icm-model-manhole-888817e106cc)

Exported from [Medium](https://medium.com) on March 18, 2025.