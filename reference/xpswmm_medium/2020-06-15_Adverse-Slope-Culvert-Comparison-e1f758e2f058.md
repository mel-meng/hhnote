# Adverse Slope Culvert Comparison

In this post I will compare the results of HY8, XPSWMM, SWMM5 and HECRAS for an adverse slope culvert. For inlet control, we know all the…

---

### Adverse Slope Culvert Comparison

In this post I will compare the results of HY8, XPSWMM, SWMM5 and HECRAS for an adverse slope culvert. For inlet control, we know all the software packages are using the same equations, it will be interesting to see how each package handles outlet control using its own implementation.

![](images\1_--QtxvF2TjGwBq3ViP0mUw.png)

As shown in the figure below, HECRAS and HY8 give very similar results using default settings. For SWMM5 and XPSWMM, the entrance/exit losses need to be adjusted to match the HY8 curves.

* using the HERAS default values of entrance = 0.2 and exit = 1, SWMM5 and XPSWMM can produce similar results
* dahsed line is HY8 result “Outlet” control line
* both XPSWMM and swmm5 overestimes the headwater depth, and XPSWMM is slightly higher than SWMM5
* HECRAS is pretty close to the HY8 result

![](images\1_Dlyb44d5iOaJS2VLUcDntw.png)

You can find the [notebook](https://nbviewer.jupyter.org/github/mel-meng/SewerAnalysis/blob/master/references/culvert/6%20culvert%20with%20negative%20slope.ipynb) and source code on [github](https://github.com/mel-meng/SewerAnalysis/blob/master/references/culvert/6%20culvert%20with%20negative%20slope.ipynb).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 15, 2020](https://medium.com/p/e1f758e2f058).

[Canonical link](https://medium.com/@mel-meng-pe/adverse-slope-culvert-comparison-e1f758e2f058)

Exported from [Medium](https://medium.com) on March 18, 2025.