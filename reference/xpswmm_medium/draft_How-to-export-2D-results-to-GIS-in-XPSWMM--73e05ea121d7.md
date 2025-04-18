# How to export 2D results to GIS in XPSWMM?

There are several ways to export 2D results to GIS.

---

### How to export 2D results to GIS in XPSWMM?

There are several ways to export 2D results to GIS.

1. Export the contour from the layer directly
2. Using the XP2D Utilities

### Export the contour

To export the 2D results as contour lines, simply right click on the result layer and click “Export Results”

![](images\1_n8bwi95MMyqLJpE_YxNy3w.png)

You can export it as a grid, since I am export the Max Water Depth, it will be the max. value. Otherwise, it will be the current time step.

![](images\1_t2iWypwjSVP7pdnST1hxJg.png)

You can also export it as contour lines,

![](images\1_fcYqFzg-OuNiZcmGwHSS_g.png)

If you only want to export the highest water depth extent, here is the trick. Before exporting the contour lines, make the following changes so that only the extent line is shown in the results.

![](images\1_-mgKQ2tJ9z1lq1c3OxtyVg.png)

1. change the display to “Filled with Contours” so that we can see both the fill and the contour lines.
2. Click on the “Contours” tab
3. Set the 1st contour at 0,
4. and the interval as a very large number so that only the extent is shown
5. You might want to adjust the line width and color so that you can see the contour line

![](images\1_jKxmPiXsH9MEI3HXWx6NLA.png)

[View original.](https://medium.com/p/73e05ea121d7)

Exported from [Medium](https://medium.com) on March 18, 2025.