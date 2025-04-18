# How to export 2D results in XPSMM

2D results can be exported directly from the 2D results layer panel or using the XP2D utilities.

---

### How to export 2D results in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-export-2D-results-in-XPSWMM)

2D results can be exported directly from the 2D results layer panel or using the XP2D utilities.

![](images\1_ZXDHpXrYwci4zirhh68GVg.png)

### 2D results Layer Tree Context Menu

When using the context menu, there are a few options,

* export the current results time step as a csv file

![](images\1_EI3E-8kie47I_7pNIeJuLw.png)

* export the results as rendered on the map

![](images\1_BUr6EaRVrWTH5LlUUtKSRg.png)

When choosing the vector format (MapInfo/ESRI Shape File), the contour lines rendered in XPSWMM will be exported. Therefore the setting of the rendering can impact the results.

To export only the boundary use the setting below, set the first contour at 0 and the interval very high, which will result the boundary line being rendered. With the fill also turned on you can verify lines are at the right location before exporting.

![](images\1_9Q83ALtWnR1RdKEGNLWqaw.png)![](images\1_NTpOjp95FgEX7G73X3t2YA.png)

For the ESRI Grid option, if the 2D grid is rotated, you’ll get a warning as shown below. In this case, you’ll need to use the XP2D tools. Otherwise, the exported results will not be at the right location.

![](images\1_EO3yN9sO-nrLDBkSsFhtJw.png)

### XP2D Utility

You can also use the XP2D Utility to export the 2D results.

![](images\1_jiCLB6xUOT4fq9W5hPyJPQ.png)

To export the max. depth as a grid, follow the instructions below.

![](images\1_TT4OeCi6piZVE2UFFywLtg.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [February 26, 2021](https://medium.com/p/a283b2efbb1f).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-export-2d-results-in-xpsmm-a283b2efbb1f)

Exported from [Medium](https://medium.com) on March 18, 2025.