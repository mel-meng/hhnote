---
title: Dam Break Analysis
---

# Introduction

XPSWMM has advanced support for modeling dam break using a 2D model. In
this article, you will recreate the part 1 and part 2 of the [Tuflow dam
break tutorial](https://wiki.tuflow.com/index.php?title=Tutorial_M10#Introduction) in XPSWMM.

-   Part 1: 2D Variable Geometry Time Trigger - the dam break begins at
    0.5 hour and develops over 15 minutes.

-   Part 2: 2D Variable Geometry Water Level Trigger - the dam break
    begins when the water level at a point is triggered.

In this exercise, you will learn to

-   Build a dam behind the road

-   Add a breach

-   Simulate the inundation extent of the breach

<img src="media/image1.png" style="width:3.57676in;height:3.03948in"
alt="A picture containing text Description automatically generated" />

# Starter Model

1.  Open the **model\starer_model.xp**

<img src="media/image2.png" style="width:3.63515in;height:3.97731in" />

The 2d grid uses 5-meter cells.

<img src="media/image3.png" style="width:2.31399in;height:2.62128in"
alt="Graphical user interface Description automatically generated" />

The boundary condition is 0.01 slope.

<img src="media/image4.png" style="width:1.62922in;height:0.96673in"
alt="Graphical user interface Description automatically generated" />

For inflow, we use a polygon rather than a single flow boundary for improved stability.

<img src="media/image5.png" style="width:2.20313in;height:2.33884in" />

2.  Update the 2D settings to reference the grid in **model\grid\DEM.asc**

<img src="media/image6.png" style="width:5.76643in;height:4.60698in"
alt="Graphical user interface, text, application Description automatically generated" />

3.  Run the model and review the results. The road is serving as a dam that blocks the water behind it.

<img src="media/image7.png" style="width:6.5in;height:3.59236in"
alt="Map Description automatically generated" />

# Build a dam

Refer to model\build a dam.xp for the final model.

4.  Build the dam. We need to add a ridge line

<img src="media/image8.png" style="width:5.20768in;height:1.77061in"
alt="Graphical user interface, text, application Description automatically generated" />

The dam will be built at where the current roads are. After drawing the line, (1) set the elevation to 65 m, and it needs to be a thick line.

NOTE: “thick” means the elevation of the cell will be modified by the ridge line, in this example, you are raising the whole road to 65m. “Thin” means only the side of the cell will be modified by the ridge line, it is more like a fence or thin wall installed along the road.

<img src="media/image9.png" style="width:6.5in;height:3.54306in"
alt="A picture containing graphical user interface Description automatically generated" />

5.  Fill the pond behind the dam will some water.

<img src="media/image10.png" style="width:3.19271in;height:2.86973in" />

6.  Run the model and review the results. At the beginning of the model, we have water ponded behind the dam.

<img src="media/image11.png" style="width:4.63062in;height:4.64448in"
alt="Map Description automatically generated" />

# Part 1 Dam break triggered by time

See **model/part1 dam break by time.xp** for the final model

7.  Add the dam break

<img src="media/image12.png" style="width:4.6765in;height:1.15611in"
alt="Graphical user interface, text, application Description automatically generated" />

Then define the dam break: 
(1) the dam break will start 0.5hr after the simulation
(2)by the end of the break, the elevation of this polygon will be at 43m. 
(3) It will take 0.25hr for the breach to complete.

<img src="media/image13.png" style="width:5.21315in;height:5.15355in"
alt="Diagram Description automatically generated with medium confidence" />

8.  Run the model and review the results. A little pass 30min the dam started to breach.

<img src="media/image14.png" style="width:4.7471in;height:3.81188in" />

# Part 2: Dam break triggered by water level

A more common trigger for the dam break is the water level behind the dam. You need to add a trigger point to monitor the water level.

9.  Add trigger point.

<img src="media/image15.png" style="width:4.25988in;height:1.37483in" />

You (1) create the trigger point (2) hover the mouse at the center of the dam break polygon and drag it to the trigger point to associate them together.

<img src="media/image16.png" style="width:4.50246in;height:4.21659in"
alt="A picture containing text, stationary, envelope, businesscard Description automatically generated" />

10. Now edit the dam break polygon. You can set the trigger at 60m, once the water level hits 60m at point 0, it will trigger the start of the dam break. Everything else works the same as the previous example.

<img src="media/image17.png" style="width:6.5in;height:5.19028in" />

11. Get the level time series inside the dam

<img src="media/image18.png" style="width:6.5in;height:3.95972in"
alt="A picture containing map Description automatically generated" />

12. Run the model and review the results. Check the water level inside and outside of the dam.

<img src="media/image19.png" style="width:3.92659in;height:1.2186in"
alt="Graphical user interface, text, application Description automatically generated" />

<img src="media/image20.png" style="width:6.5in;height:3.37431in" />

# Conclusion

In this article, you built a model to simulate dam break using a 2D model. The key steps include,

-   Model the dam

-   Setup the initial water depth inside the dam

-   Setup a dynamic elevation shape to simulate the dam break

-   Trigger the dam break using time, and water level

-   Review the dam break results using time series output
