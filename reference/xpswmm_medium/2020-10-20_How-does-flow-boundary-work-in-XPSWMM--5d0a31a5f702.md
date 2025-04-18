# How does flow boundary work in XPSWMM?

Source: Innovyze Support Portal

---

### How does flow boundary work in XPSWMM?

![](images\1_zd-1JviTodu0WlQLRtk6Bw.png)

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-does-flow-boundary-work-in-XPSWMM)

What happens when you draw a flow boundary in XPSWMM?

As shown above, we have 5 flow boundaries presented in this model. A 3D view of the surface is shown below to help visualize the surface. You can find the model on [github](https://github.com/mel-meng/xpswmm/tree/master/models/flow_boundary).

![](images\0_8APDJNWUEnF-0QAx.png)

For linear flow boundaries(polylines), it introduces the flow at the lowest cell(s) along the line until the flow is conveyed, it will load all the flow to the lowest cell along the line,

1. It loads the flow in the channel
2. It loads at the east end the lowest point
3. When using the flow area, it can evenly distribute flow along the whole area when “equal distribution” is checked.

![](images\1_72kpy6LCHDKZLfTep0fE1A.png)

4. West end the low point

5. When aligning the line with the contour line, it forms a flat surface, therefore the flow spreads across the whole length

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 20, 2020](https://medium.com/p/5d0a31a5f702).

[Canonical link](https://medium.com/@mel-meng-pe/how-does-flow-boundary-work-in-xpswmm-5d0a31a5f702)

Exported from [Medium](https://medium.com) on March 18, 2025.