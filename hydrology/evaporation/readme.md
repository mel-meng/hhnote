---
title: Evaporation
---

# Introduction

Evaporation usually is not a significant source of loss for models running a single design storm for system capacity analysis. However, for continuous simulation with a focus on water volume and quality, it can have significant impact on the modeling results.

Evaporation happens when there is standing water on the subcatchment surface, therefore, the actual evaporation for a subcatchment might not be limited by the evaporation rate, but the time water is standing on the surface. Evaporation can also happen for open channel and subsurface if groundwater is modeled, in this article we only focus on subcatchment evaporation.

Commonly used evaporation methods include,

- a constant, e.g. 0.1 inch/day

- monthly average

- evaporation time series

We’ll review how to setup evaporation in XPSWMM, InfoWorks SWMM and InfoWorks ICM models.

# XPSWMM

In XPSWMM, evaporation is applied to the whole model regardless of the rainfall profiles used. The default is a 0.1 in/day value. The alternative is the use a monthly average.

<img src="./media/image1.png" style="width:2.75694in;height:3.02985in" alt="Graphical user interface, application Description automatically generated" /> <img src="./media/image2.png" style="width:2.66767in;height:3.04408in" alt="Graphical user interface, application Description automatically generated" />

# InfoWorks SWMM

SWMM offers similar options, you can define a constant value in a SWMM climatology object.

<img src="./media/image3.png" style="width:6.5in;height:3.6625in" alt="Graphical user interface, application Description automatically generated" />

When using the monthly average, you need to setup the evaporation data in the rainfall object. Please note SWMM only support a single evaporation profile for the whole model. Only the first one will be used.

<img src="./media/image4.png" style="width:6.5in;height:4.70208in" alt="Graphical user interface Description automatically generated" />

# InfoWorks ICM

The InfoWorks ICM network uses the same rainfall object with evaporation time series as InfoWorks SWMM. Different from SWMM, in InfoWorks ICM each rainfall profile will have its own evaporation profile, therefore, you need to define the evaporation profile in the subcatchment attribute.

<img src="./media/image5.png" style="width:3.77036in;height:1.67687in" alt="Graphical user interface, application, table Description automatically generated" />

# Results Comparison

For a sample model setup,

- subcatchment RG1: 1 in/hr constant rainfall

- subcatchment RG2: 0.1 in/hr constant rainfall

- subcatchment RG3: 1 in/hr constant rainfall

For Evaporation,

- RG1 starts with 0.1 in/day then 0.2 in/day

- RG2 starts with 0.4 in/day then 0.2 in/day

- RG3 starts with 0.4 in/day then 0.2 in/day

<img src="./media/image6.png" style="width:4.58276in;height:1.95809in" alt="Table Description automatically generated" />

<img src="./media/image7.png" style="width:3.00051in;height:2.79255in" alt="Diagram Description automatically generated" />

## XPSWMM

XPSWMM reports the same evaporation rate despite there is very little standing water on RG2.

<img src="./media/image8.png" style="width:5.68272in;height:2.66833in" alt="Graphical user interface, chart, line chart Description automatically generated" />

## InfoWorks SWMM

As shown below, the evaporation is almost 0 for RG2 because the rainfall is only 0.1 in/hr, and there is very little standing water on the surface. Although RG1 and RG3 has different evaporation rates, they show exactly the same results, that is because SWMM only uses the first evaporation profile for the whole model.

<img src="./media/image9.png" style="width:2.66633in;height:2.91052in" alt="Diagram Description automatically generated" />

## InfoWorks ICM

InfoWorks ICM differs in two ways,

- InfoWorks ICM reports the evaporation rate defined in the rainfall rather than the actual evaporation.

- InfoWorks ICM interpolates the evaporation rates between to entries, while SWMM and XPSWMM assumes the same evaporation rate until the next reading

<img src="./media/image10.png" style="width:3.32661in;height:3.12906in" alt="Chart, line chart Description automatically generated" />

However, the sim engine linearly interpolates the evaporation between the data points. As shown below, SWMM/XPSWMM assumes the evaporation will stay the same until a new value is provided.

<img src="./media/image11.png" style="width:6.5in;height:3.17222in" alt="Graphical user interface, application Description automatically generated" />

# Conclusion

XPSWMM, InfoWorks SWMM and InfoWorks ICM all support evaporation. XPSWMM and InfoWorks SWMM can only use one evaporation for all the rainfall profiles, while InfoWorks ICM can assign different evaporation profiles for each subcatchment. Additionally, XPSWMM and InfoWorks SWMM assumes the evaporation rate doesn’t change until there is a new reading, while InfoWorks ICM interpolates the rate between entries.
