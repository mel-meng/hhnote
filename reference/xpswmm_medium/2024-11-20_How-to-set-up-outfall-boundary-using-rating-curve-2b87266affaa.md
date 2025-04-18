# How to set up outfall boundary using rating curve

source: github

---

### How to set up outfall boundary using rating curve

source: [github](https://github.com/mel-meng/hhnote/tree/main/hydraulics/rating_%20curve)

### Introduction

Rating curve defines the relationship between the depth and flow. It is often used to define the boundary condition of an outfall,

* Flow into a treatment plant
* Split a model into sub models, and model the flow condition at the split locations

In InfoWorks ICM, the easiest way to add a rating curve to an outfall is to convert it to a screw pump.

![](images\0_U8WHgDK3WUQFNcv8.png)

1. Make a copy of the outfall
2. Change the existing outfall to a break node
3. Add a pump link
4. Change it to screw pump and set the on/off base level the same as the break node
5. Update the head discharge table with the rating curve

### Example Model

A simple model with rectangle outfall pipe is modeled in both InfoWorks and SWMM5.

![](images\0_ruOU8RBMFilpSznJ.png)

The results are shown as a scatter plot of depth vs velocity as shown in the following figures,

* Orange is the normal depth calculated from Manning’s equation
* Green is critical depth calculated from the flow
* X is simulated results from the model

![](images\0_9-dReZBO0OeDTNyC.png)

For free outfall, InfoWorks ICM and SWMM5 show similar results, it is the lower of the Yn and Yc.

Since InfoWorks doesn’t have a normal outfall condition, a screw pump with a rating curve is used, and it shows similar results as SWMM5.

![](images\0_lMxBWm6R58ZN8rKp.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [November 20, 2024](https://medium.com/p/2b87266affaa).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-set-up-outfall-boundary-using-rating-curve-2b87266affaa)

Exported from [Medium](https://medium.com) on March 18, 2025.