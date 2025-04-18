# How to visualize capacity issues in XPSWMM

source: Innovyze Support Portal

---

### How to visualize capacity issues in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-visualize-capacity-issues-in-XPSWMM)

Evaluating a collection system’s capacity is a critical task for planning and design projects. XPSWMM provides a wide range of tools for modeler to evaluate the system capacity.

Common tasks include checking the HGL of system to,

* identify capacity issues of manholes without enough freeboard and pipes that are surcharged
* understand the causes of the capacity issues, pipe too small or downstream restriction, etc.

### Profile View

The most useful tool is the “dynamic long section” tool

![](images\1_gBUW52UgAd2bA5kf27ox6g.png)

To use this tool, first select a flow path. XPSWMM provides several ways to select a flow path in a network,

1. right click on a node and select upstream or downstream

![](images\1_xV4dvO-3u7gX3t32onlE9g.png)

2. click the start node, then hold “shift” key and click the end of a flow path, XPSWMM will select the path in between.

3. Hold “ctrl” key to select one pipe at a time

Once the flow path is selected, click on the profile tool

![](images\1_vo8fwaJXh3NAibQ3x2m8Hg.png)

In general, if the model performs well, we only need to focus on the max. HGL. There are a few simple checks to determine the pipe capacity by comparing the slope of the HGL and the pipe,

* When the pipe has enough capacity to convey the flow, the HGL should have the same slope as the pipe
* When the pipe doesn’t have enough capacity, to push more flow through the pipe, the HGL will have a steeper slope than the pipe, so that there is more head on the upstream end to push more water
* When the downstream end is backing water up, the HGL slope will be less than the pipe slope, so that there is less head to push the water through the pipe

Using the above rules, we can quickly identify sections of the profile that have capacity issues, and the causes for these issues.

![](images\1_rnv_LdHL3XyWjYBTgLNa9Q.png)

However, the rules above assume the flow through the pipes does not change dramatically throughout the system, and its behavior can mostly be described using the manning’s equation, and energy equations. Therefore, it is a good idea to watch the animation and verify that the max. HGL is a result of the same peak flow passing through the system.

“Dynamic section views” combines both the profile and the hydrographs in one place, so that the dynamics of the system can be better studied.

![](images\1_tW2NxiffgQoCZNZmn6VcFg.png)

The dynamic section views can display a lot of customizable information.

The link/node tables are from the XPTables, which can be customized.

As shown below, the cross section view and the hydrograph view are linked using the link name.

![](images\1_vxoVpHE4-3-PUp5xptmsKw.png)

You might need to maximize the graph to see the link name by right click on the graph.

![](images\1_iIMnabY6P74rlNvd8EQvgA.png)

You can drag the dashed red line to change the current time of the animation.

![](images\1_ar8x2nk3MmeouD4dNAEDQQ.png)

As shown below, understanding what is going on in this graph can take some time. The dynamics of a collection system can be complicated, and watching the animation is one of the best ways for modelers to develop intuitions how water moves through a system.

![](images\1_BK_2Ric6Or_-Sg_8Msg2JA.png)

### Plan View

For people without the engineering training on hydraulics and hydrology, a plan view might be easier to understand.

![](images\1_0_mPUcpIuS8l2iNHfFOoqg.png)

The Dynamic plan view shows system performance as animation on a map.

Links and nodes are styled with different color and sizes to represent the flow and flooding conditions. The animation also shows the flow direction inside the pipes.

Zoom to the area of interest, then click on the “Dynamic Plan View” button,

![](images\1_Vpu57kK9lkw8EjmjDiDWSQ.png)

You can use the controls on the top of the window for playing the animation.

![](images\1_qO4WNxt3IXHCP047vtJr2A.png)

The colors and freeboard settings can be accessed using the file menu.

![](images\1_Tj9u6Hmm6ybLk3dLfG9uZA.png)![](images\1_e3uPW0XArKtnCSK4jJkxIw.png)

### Summary

XPSWMM has several visualization tools just a click away to reveal the capacity issues of the model, through some practice, the modeler can quickly identify the capacity issues and the causes.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 10, 2021](https://medium.com/p/d14ee27cafe).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-visualize-capacity-issues-in-xpswmm-d14ee27cafe)

Exported from [Medium](https://medium.com) on March 18, 2025.