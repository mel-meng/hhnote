# How to setup dual Drainage in XPSWMM

What is dual drainage

---

### How to setup dual Drainage in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-setup-dual-drainage-in-XPSWMM)

![](images\1_fRRPy4DsB3ZoM9PvGZ9b8Q.png)

### What is dual drainage

Dual drainage is the setup to model typical storm water flows along streets.

* When runoff reaches the street, they start to flow along the gutters
* As it hits the catch basin, some of the flow will be captured and goes into the storm pipe underground
* The rest of the flow will continue along the gutter until it hits the next catch basin, then the same thing happens, part of it will be captured and goes into the pipe under ground, the rest flows along the street.

![](images\1_hcgQLCk6a-oYHjUlYeA6Kw.png)

### How does XPSWMM represent dual drainage system

To fully model the dynamics of a dual drainage system, an inlet need to be added to each node.  
   
As shown below, the trick is breaking the existing node into a top and a bottom node, and add a rating curve in between to represent the inlet. With this setup,

* When runoff is loaded into the node, the rating curve will determine how much flow will go into underground pipe, and the rest will flow into the street pipe
* Similarly, as the flow reaches the downstream node in the street pipe, the rating curve will decide how much will be captured into the underground

![](images\1_6Th6krdouvPqpZA9ULcQsw.png)

However, XPSWMM does this trick internally, from the user interface, it still shows the two nodes as one junction without exposing the details. The details could be revealed by checking the 1D log.  
   
Detailed node information can be found in table E3a, an example is shown below.

* The top node has the same node name as show in the XPSWMM user interface
* The bottom node has the suffix $I
* The top node has the original ground elevation and the invert of the street
* The bottom node has the original invert and the ground invert using the street invert

![](images\1_zbIYd8i2Kwf-NEEBMrV3Yw.png)

The rating curve is named with a suffix of $R after the node name, and the connectivity can be found in table E4 as shown in the example below.

![](images\1_V6WUj4DuYYRy-hfQFrmhyg.png)

The stages and flow of the two split nodes can be plotted in XPSWMM,

![](images\1_a-UzhzEeEcdswLQlHSBAIA.png)![](images\1_aqsM6yqBXkJjBNBJOt7hvA.png)

### How to setup dual drainage in XPSWMM?

As shown below, with this setup, we need to model the rim of the node as the top of the street channel cross section, instead of the rim of the actual manhole, also we need to model all the inlet into the node as a single inlet.

![](images\1_IeLD7AqGX9oOvKTIqz8Zow.png)

A convenient way of setting dual drainage is to create the underground pipe first, and then make sure all the ground elevation of the nodes are set to the street invert, then use the automated tool to create the street channels.

![](images\1_8VS1MK-KBx02_PPljp6cjA.png)

### Tips

XPSWMM assumes the open channel in the multi-link is the street.

* If you would like to use a closed pipe to represent the surface channel, it will not work properly, because it will be connected to the bottom node instead
* If you have more than one open channel going out of a node, the node will be split at the lowest invert of the open channel, make sure that is the desired configuration

When inlets are not used, dual drainage will behave as the following which might not give the desired outcome since there will be no flow in the open channel unless the level in the node is higher than the street channel invert.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 1, 2020](https://medium.com/p/ec7c592bf8c7).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-setup-dual-drainage-in-xpswmm-ec7c592bf8c7)

Exported from [Medium](https://medium.com) on March 18, 2025.