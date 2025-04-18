# SCS Hydrology Method — Part 1

Introduction

---

### SCS Hydrology Method — Part 1

[Part 1](https://mel-meng-pe.medium.com/scs-hydrology-method-part-1-44d6825d7599), [Part2](https://mel-meng-pe.medium.com/scs-hydrology-xpswmm-vs-hec-hms-part-2-914bbc65861f), [Part 3](https://mel-meng-pe.medium.com/scs-hydrology-in-infoworks-icm-part-3-3e7324fc4266)

### Introduction

SCS hydrology is a widely used method for designing stormwater sewer. It is well documented in [TR-55](https://www.hydrocad.net/pdf/TR-55%20Manual.pdf) and implemented in many software packages. HEC-HMS online help explains how it transforms the rainfall into hydrograph,

· [SCS curve number loss model](https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/infiltration-and-runoff-volume/scs-curve-number-loss-model)

· [SCS Unit hydrograph routing model](https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/surface-runoff/scs-unit-hydrograph-model)

In the first step, you use the SCS Curve Number method to calculate the losses for the rainfall (which lumps infiltration and other losses). Next, you use the SCS unit hydrograph method to route the excess rainfall into the hydrograph.

### Curve Number Loss Model

The curve number loss model calculates the rainfall excess using the equation below,

![](images\1_-4EiSJTn8JUUH9d3nMnzEw.png)

where Pe = accumulated precipitation excess at time t;

P = accumulated rainfall depth at time t;

Ia = the initial abstraction (initial loss);

and S = potential maximum retention, a measure of the ability of a watershed to abstract and retain storm precipitation.

By default, the initial abstraction is set at 20% of the maximum retention.

![](images\1_feTuqnqCIJe-vSqRp6RJPQ.png)

S is calculated using the following formula.

![](images\1_2RbDeEVngOUcRgC7Sn8lAg.png)

CN is the curve number, its values range from 100 (for water bodies) to approximately 30 for permeable soils with high infiltration rates.

For mixed land cover, composite CN is calculated using an area weighted average. According to the National Engineering Handbook, when the CN values are close among the different covers, this method is acceptable. However, if the CN value difference is large, each land cover should be calculated separately, and the combined flow should be used. Refer to the section impervious area for more information.

![](images\1_VcxAUNv3crHAjv-zMghEPw.png)

### SCS Unit Hydrology Routing

SCS UH routing turns the excess rainfall calculated from the CN method into a hydrograph. At the heart of the SCS UH model is a dimensionless, single-peaked UH (unit hydrograph).

![](images\1_0mAKvVw8zZ6CzPj1uL7M8A.png)

As the figure from National Engineering Handbook shows, when a unit of rainfall falls, it generates a curvilinear response (or the triangle curve if you choose that one), and the shape of this unit hydrograph can be defined using only 3 parameters,

· Area

· Shape factor

· Time of concentration

in which

A = watershed area; and

C = conversion constant (default value is 2.08 in SI and 484 in foot-pound system), the shape factor

Tp = The time of peak (also known as the time of rise) is related to the duration of the unit of excess precipitation as:

· **dt: time step, dt=0.133 Tc**

· **tlag: lag time, tlag = 0.6\*Tc**

· **Tc: time of concentration**

**NOTE:** For more detailed explanation and example, refer to the National Engineering Handbook [**chapter 16**](https://directives.sc.egov.usda.gov/OpenNonWebContent.aspx?content=17755.wba).

· The shape of the unit hydrograph is defined by a single parameter, the peak rate factor (PRF), and the default one is PRF=484, an example of the UH is shown in Figure 16–1

· The time step (duration of the excess rainfall), time of concentration (Tc) and lag time (L) can be related as shown in figure 16A-1, dD = 0.133Tc, L=0.6Tc. It should be noted that all unit hydrograph method results are sensitive to the time step.[[M(M2]](#_msocom_2)

· To route the SCS CN runoff using the SCS UH method, the excess rainfall incremental for each time step is calculated using the curve number method.

### Impervious Area

According to the [National Engineering Handbook](https://directives.sc.egov.usda.gov/viewerFS.aspx?hid=21422), there are two ways to handle impervious areas.

* set up pervious and impervious as two subcatchments, then average the combined flow (Weighted Q)
* calculate an area weighted CN, then use that to calculate the flow (Weighted CN)

The weighted CN is also called as a composite CN, and due to its simplicity, it might be the most widely used method in practice. However, when the impervious areas CN value of 98 is much higher than the pervious area, a composite CN might not be correct.

[TR-55](https://www.hydrocad.net/pdf/TR-55%20Manual.pdf) provides a detailed instruction on how to handle impervious areas depending on if it is connected or disconnected. (Unconnected vs connected: connected area flows directly into the drainage system.) And the implementation of impervious areas can vary from package to package. In the next post, I’ll compare the results in XPSWMM/HEC-HMS and ICM.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [February 2, 2023](https://medium.com/p/44d6825d7599).

[Canonical link](https://medium.com/@mel-meng-pe/scs-hydrology-method-part-1-44d6825d7599)

Exported from [Medium](https://medium.com) on March 18, 2025.