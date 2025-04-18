# Inlet 2D flow capture in XPSWMM

XPSWMM offers quite a few options for modeling the flow exchange between the 1D inlet and the 2D surface. In this article we will compare…

---

### Inlet 2D flow capture in XPSWMM

XPSWMM offers quite a few options for modeling the flow exchange between the 1D inlet and the 2D surface. In this article we will compare using a rating curve and the default 2D flow capture options.

Below is the model setup. We have a flat surface, the water level is controlled by the downstream boundary condition. It increases the level from 90–95ft over a few hours. And we can observe the relationship between the inlet and its inflow.

![](images\1_QcTifEoDX6iJFM0kR3DT6g.png)

In order to monitor the flows through the inlet, a dummy pump is connected to the inlet, it is not exactly the same as the inflow from the 2D into the system, but should be close.

We use the equation of Q=10\*D ^ 1.5 for the rating curve.

![](images\1_GFd-Tr2YzUkvCK99IwlwfQ.png)

And for the 2d flow capture, the same equation.

![](images\1_uLn5oG3dJN0NYeJ49MMt0w.png)

As shown below, the rating curve and the check matches very well. The 2d capture option captures a lot less flow than using the rating curve when the depth is less than 0.5ft, but matches much better once the depth is higher than 1ft.

![](images\1_jQ6o99N35dDslwpN_NlhTg.png)

[View original.](https://medium.com/p/cb7d41363d32)

Exported from [Medium](https://medium.com) on March 18, 2025.