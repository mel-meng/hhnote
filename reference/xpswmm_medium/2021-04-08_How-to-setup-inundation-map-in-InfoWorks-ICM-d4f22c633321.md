# How to setup inundation map in InfoWorks ICM

Source: Innovyze Support Portal

---

### How to setup inundation map in InfoWorks ICM

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-setup-inundation-map-in-InfoWorks-ICM)

ICM provides a wide range of tools to style an inundation map and it could be overwhelming for new users. In this article, we will go through a few typical setup.

### Flood theme vs 2D Zone theme

ICM offers two ways to render flooding extent.

* flooding theme: a GIS based approach. A water level surface is generated from 1D and 2D simulation results, and then it is compared to the ground model to calculate the water depth. The rendering is NOT based on the simulated results as it, rather it is calculated from the results. For 1D river system, flooding theme is the only way to render the flooding extent within ICM.
* 2d zone theme: 2D results are the direct simulated values of velocity and depth for each 2D element. No ground model information is used.

You shouldn’t use both 2D results and flooding theme at the same time, as shown below, flood theme and 2D zone theme will give slightly different results due to the differences in how flooding extent is calculated. Pick one the suite for your application.

![](images\1_ceFAyFMXlsJAKF_sXANlVg.png)

### Flood theme

To use the flood theme,

1. drag ground model into the results geoplan

![](images\1_zPQ3iUw11JVE6KZhti_1vg.png)

2. turn off the 2D zone and turn on flood theme

![](images\1_f5F4rHnjEMgwcTnXyAGk5Q.png)![](images\1_c4qLhRsGXAhY9O3RyocHyw.png)![](images\1_lPCf9L64q30M9YI-2L52nw.png)

You can edit the color ramp by clicking on the edit button.

![](images\1_nYLYyyZbIZWF4mR_8xRCuQ.png)

I would highly recommend saving your theme settings as an object for reuse.

![](images\1_DbwKsa9_JJ0uix7b0n2jyg.png)![](images\1_eqTG23Q89HRgw0coZIMwIA.png)

1. go to the model group where the theme will be saved
2. give it a name

![](images\1_y5V1zvV3fkuJDUShprXZow.png)

uncheck all the layers, then only check the flood layer. You can type “F” to find the layer,

![](images\1_ACmsxobaSdkXMlzimqx-rA.png)![](images\1_PXyRNV9vNxj1tgrWblMIrA.png)

Next time you need to style your flood theme simply drag the theme into the geoplan.

![](images\1_oaXVTQpJbpH4yl0bsSykRA.png)

### 2D Zone Theme

2D zone theme is more flexible because you have access to all the simulated values for each 2D element, and if you don’t have any 1D river system, this should be your first choice. To style a 2D zone map, we’ll need to work with,

* 1D elements
* 2D polygon and lines
* 2D simulation results
* 2D element lines

![](images\1_SHUIeHB2br7ebybsnfb7rg.png)

For 1D elements, refer to other resources to style them.

For 2D polygons and lines, you can either turn them off or use techniques similar to 1D elements.

For 2D simulation results, I’ll show two typical setups below,

For the depth,

![](images\1_-LCwDF21sM_YsOXzVkt56Q.png)

For the velocity,

![](images\1_5zIpaxZ9RstuK8wqLx4FIA.png)

You can easily turn on/off different sub themes using the disable button.

![](images\1_EerL9IRVck51clLN9_uGOQ.png)

Or use the thematic key window (Window->thematic key window)

![](images\1_TnuqLm3MU2EQ15Ah5mdN6Q.png)

For the element lines, they can be turned on/off or changing styles using the “Elements” Tab.

![](images\1_ATNmQgYx7WHQtK70oRK2LA.png)![](images\1_mNw6r8bkOQcoQ97RhPntVQ.png)

### Custom Results

You can also use SQL to create new values from the simulation results.

Say we need to show the total flood duration in hours instead of seconds.

Using the SQL button, we can build new expressions from a long list of variables.

![](images\1_aHEgu4yU7KzmKaEQaOviUQ.png)

The expression below will turn seconds into hours,

![](images\1_A0oqbpOgqzhvu3tvcLt71w.png)![](images\1_GW2jNbmhWavxO3Jir1krfA.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 8, 2021](https://medium.com/p/d4f22c633321).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-setup-inundation-map-in-infoworks-icm-d4f22c633321)

Exported from [Medium](https://medium.com) on March 18, 2025.