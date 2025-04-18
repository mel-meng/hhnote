# InfoWorks ICM Ground Water Module

source: github

---

### InfoWorks ICM Ground Water Module

source: [github](https://github.com/mel-meng/hhnote/tree/main/hydraulics/icm_gi)

### Introduction

InfoWorks ICM [Ground Infiltration](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-398817F8-D56F-4981-AAE4-2FBFA4616E78) (GI) simulates the complicated long term hydrological cycle of sewer infiltration over long periods. It provides an effective way to model the long tails of the elevation flows long after a storm event.

Given that most parameters for ground water infiltration cannot be measured directly, the GI module is often used as a black box model to match observed metering data. A good understanding of the equations driving the GI processes and the corresponding parameters can speed up the calibration process.

### Ground Infiltration Process Overview

Despite the numerous processes involved in GI, all of them operate under simple linear equations as functions of the water level in the soil and ground stores. As illustrated in the subsequent diagrams:

* Soil store,
* Receives inflow from the subcatchment pervious land cover soil infiltration
* Loses flow from evaporation and percolation into the ground store
* All the flows are linear to soil store level
* Ground store,
* Receives inflow from soil store percolation.
* Loses flow from baseflow and infiltration.
* All the ground store flows are linear to ground store level.
* Receiving node,
* The soil store infiltration is linear to the percolation
* The ground store infiltration is linear to the head between the ground store level and node water level

![](images\0_KMULpXOGCE3oyEqZ.png)

Data fields

The mapping between the [ground infiltration data fields](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-151A9385-D673-4C73-A40D-F64CC04FD7FF) to the equations is shown in the following figure.

![](images\0_By2Qzgi5iNoYTvK0.png)

### Threshold: relative vs absolute

The primary state variables that drive the GI processes are the water levels in the soil and ground store. InfoWorks offers two ways of measuring levels in the ground store, absolute vs. relative.

![](images\0_DSkon3U0rDk90vRz.png)

When using the relative threshold type, Ht1, and Ht2 measure the distance from the node invert (negative if it is below the node invert.) NOTE that you can set Ht2 below the node invert, and infiltration will start when the level is above Ht2 but still below the node invert.

### Initial conditions

Initial conditions can greatly impact the modeling results. Typically, initial levels are estimated by running the simulation for extend periods to get the low levels during dry season and elevated levels during the wet season.

You can set the initial levels using the “[Ground Infiltration Event](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-397A9119-1A7F-4462-AD8A-11E7573A893F)” object, which can be specified for each ground infiltration ID or an individual subcatchment.

As shown in the following example,

1. In most cases we don’t have observed ground water level data, and the time series should be left blank
2. The initial soil saturation defines the level in the soil store
3. The initial groundwater level defines the level in the ground store. The level must rise above the infiltration threshold level for ground infiltration to occur. Note the level is in elevation measured from the same datum as the receiving node. When relative threshold type is used, the threshold is measured as the distance from the receiving node invert instead as elevation.

![](images\0_uRG58uGoQ7jMLWgS.png)

### Evaporation

In areas where evaporation accounts for a lot of loss, define the evaporation parameters, which function linearly to the soil store level.

![](images\0_5XN_bs6wQZTC_FTI.png)

### Conclusion

The InfoWorks ICM Ground Infiltration module is a robust tool for simulating complex hydrological cycles of sewer infiltration. With a comprehensive understanding of its processes and careful calibration, you can effectively math your modeling results to observed long tails.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [December 4, 2023](https://medium.com/p/d3a9198d0391).

[Canonical link](https://medium.com/@mel-meng-pe/infoworks-icm-ground-water-module-d3a9198d0391)

Exported from [Medium](https://medium.com) on March 18, 2025.