---
title: SWMM5 Infiltration Methods Comparison
---

# Introduction

The runoff from pervious areas can be highly dependent on the infiltration settings used in models like SWMM. To ensure accurate results, SWMM infiltration methods have undergone several major updates. The choice of infiltration methods in SWMM5 are the modified Green Ampt, Modified Horton, and CN methods, all these methods support the recovery of infiltration capacity during dry periods between storms.

In this article, we will compare the matching SWMM5 infiltration methods found in XPSWMM, InfoWorks “sim” and “SWMM” engines.

|                                                                      |            |              |                 |                    |        |
|----------------------------------------------------------------------|------------|--------------|-----------------|--------------------|--------|
| SWMM5                                                                | Horton     | Green Ampt   | Modified Horton | Modifed Green Ampt | CN     |
| Sim                                                                  | HortonSWMM | Green Ampt   | Horton\*        |                    | CNSWMM |
| XPSWMM                                                               | Horton\*   | Green Ampt\* |                 |                    | CN\*\* |
| \*Similar results                                                    |            |              |                 |                    |        |
| \*\*SWMM doesn't support initial abstraction factors found in XPSWMM |            |              |                 |                    |        |

The infiltration methods used in InfoWorks SWMM and XPSWMM are called “Runoff volume” methods in InfoWorks Sim engine.

<img src="./media/image1.png" style="width:6.5in;height:3.46667in" alt="Graphical user interface, text, application Description automatically generated" />

## Horton/Modified Horton

Horton’s method is empirical in nature. SWMM5 added a modified version of the Horton method to improve accuracy when the rainfall intensity is low, which uses the cumulative infiltration in excess of the minimum rate as its state variable (instead of time along the Horton curve).

As shown in the figure below, the infiltration rate decreases from the max. rate to the min. rate. The classic method calculates the potential infiltration rate based on the equivalent time along the curve while the modified method tracks the cumulative infiltration.

<img src="./media/image2.png" style="width:6.5in;height:3.62639in" />

Source: [How Does Horton Infiltration Work in SWMM 5? – EPASWMM5, Autodesk Innovyze InfoWorks ICM SWMM & ICM InfoWorks, InfoSWMM , InfoDrainage, SWMM5+](https://swmm5.org/2013/08/08/how-does-horton-infiltration-work-in-swmm-5/)

As shown below, the modified Horton method has more infiltration capacity before the peak of the storm.

<img src="./media/image3.png" style="width:2.76813in;height:3.49443in" alt="Chart, line chart Description automatically generated" />

XPSWMM uses the classic Horton’s method, while SWMM5 supports both methods (Horton and Modified Horton). In InfoWorks ICM sim engine, the modified Horton method is called “Horton”, and the classic method is called “HortonSWMM”.

## Green Ampt/Modified Green Ampt

Green Ampt is often preferred over Horton method because it is more physically based. The choice of the method often depends on the availability of the soil parameters in the modeled area.

<img src="./media/image4.png" style="width:5.86329in;height:2.88842in" alt="Diagram Description automatically generated" />

The modified Green Ampt method was added in SWMM5 to improve the accuracy during the initial low intensity period by not depleting moisture deficit in the top surface layer of soil during initial periods of low rainfall as was done in the original method. As shown in the figure below, the modified version will produce more infiltration during the peak of the storm.

<img src="./media/image5.png" style="width:3.02026in;height:3.29687in" alt="Chart Description automatically generated" />

## SCS CN

In SWMM5, the SCS CN infiltration method can also be used, although it does not support initial abstraction. In comparison, both XPSWMM and InfoWorks Sim support initial abstraction when using the CN method.

<img src="./media/image6.png" style="width:2.66248in;height:2.35101in" alt="Chart Description automatically generated" />

InfoWorks Sim offers two options: CNSWMM and CN. The CNSWMM doesn’t support initial abstraction but requires drying time. As shown in the figure below. When there are no initial abstractions, the results are very close.

<img src="./media/image7.png" style="width:2.62801in;height:2.86869in" alt="Chart Description automatically generated" />

# XPSWMM

XPSWMM supports RUNOFF routing methods with the following infiltration methods: Horton, Green Ampt, Uniform loss and SCS Curve number. XPSWMM doesn’t support infiltration recovering.

<img src="./media/image8.png" style="width:4.93062in;height:4.22632in" alt="Graphical user interface, application Description automatically generated" />

You can get infiltration parameters using the XPTables. The mapping of the XPTables columns is shown below.

<img src="./media/image9.png" style="width:4.46436in;height:1.13898in" alt="Table Description automatically generated" />

<img src="./media/image10.png" style="width:6.5in;height:4.09722in" alt="Graphical user interface, application Description automatically generated" />

# InfoWorks ICM SWMM

The mapping of the parameters from XPSWMM to ICM SWMM is shown below.

<img src="./media/image11.png" style="width:6.5in;height:3.51944in" alt="Graphical user interface, diagram Description automatically generated" />

# InfoWorks Sim Engine

When using the InfoWorks Sim Engine, infiltration is defined in the Runoff surface. See the field mapping below for more details.

Horton and HortonSWMM uses the same input parameters,

<img src="./media/image12.png" style="width:6.5in;height:3.76111in" alt="Graphical user interface, application Description automatically generated" />

Green Ampt

<img src="./media/image13.png" style="width:6.5in;height:3.325in" alt="Graphical user interface, text, application Description automatically generated" />

CN and CNSWMM

CNSWMM does not support initial abstraction.

<img src="./media/image14.png" style="width:6.5in;height:4.0875in" alt="Graphical user interface Description automatically generated" />

# Results Comparison

The infiltration for the sample model of a single subcatchment shown below is setup in XPSWMM, InfoWorks ICM and InfoWorks SWMM.

<img src="./media/image15.png" style="width:4.34825in;height:3.54782in" alt="Graphical user interface Description automatically generated" />

## Horton

InfoWorks ICM and SWMM show very similar results, and XPSWMM shows slightly higher infiltration.

<img src="./media/image16.png" style="width:6.5in;height:3.70556in" alt="Chart, line chart Description automatically generated" />

## Green Ampt

InfoWorks ICM and SWMM show very similar results, and XPSWMM shows slightly higher infiltration.

<img src="./media/image17.png" style="width:6.5in;height:3.66667in" alt="Chart, line chart Description automatically generated" />

## Modified Horton

XPSWMM doesn’t support modified Horton method, the XPSWMM Horton method is shown for comparison. InfoWorks ICM and SWMM show very close results, both showed higher infiltration during the peak of the storm when comparing to XPSWMM Horton.

<img src="./media/image18.png" style="width:6.5in;height:3.69653in" alt="Chart, line chart, histogram Description automatically generated" />

## Modified Green Ampt

Neither XPSWMM nor InfoWorks ICM supports Modified Green Ampt method. The InfoWorks SWMM modified method shows higher infiltration rate during the peak of the storm because during the lower intensity period the infiltration capacity was not depleted.

<img src="./media/image19.png" style="width:6.5in;height:3.51528in" alt="Chart, histogram Description automatically generated" />

## CN initial abstraction

In XPSWMM, you can have initial abstraction. The figure below shows the difference with vs without IA.

<img src="./media/image20.png" style="width:4.68618in;height:3.63079in" alt="Chart Description automatically generated with medium confidence" />

Both InfoWorks ICM Sim “CN” and XPSWMM support initial abstraction. As shown below, XPSWMM shows the highest infiltration, Sim is the second highest since both have initial abstractions.

<img src="./media/image21.png" style="width:6.5in;height:3.70556in" alt="Chart Description automatically generated" />

However, InfoWorks Sim “CNSWMM” doesn’t support initial abstraction. As shown below, the “CN” method showed higher infiltration, and the infiltration only starts when rainfall exceeds the initial abstraction (NOTE: in XPSWMM, the initial abstraction is also reported as infiltration).

<img src="./media/image22.png" style="width:3.97253in;height:3.38014in" alt="A picture containing shape Description automatically generated" />

Once the initial abstraction is set as 0, all the methods show very similar results.

<img src="./media/image23.png" style="width:5.27355in;height:2.97482in" alt="Chart Description automatically generated" />

# Recovery for Infiltration

For continuous simulation, infiltration capacity should regenerate between storm events. This advanced topic will be discussed in a separate article.

<img src="./media/image24.png" style="width:6.5in;height:3.10694in" alt="Graphical user interface Description automatically generated" />

# Conclusion

Accurate modeling of infiltration is crucial for predicting runoff from pervious areas. This article compared the SWMM5 infiltration methods, including Modified Horton, Horton, Modified Green Ampt, Green Ampt, and CN, used in InfoWorks SWMM, InfoWorks Sim, and XPSWMM. The comparison revealed that,

- For the matching methods, all packages show similar results. InfoWorks Sim matches SWMM better than XPSWMM.

- For the CN method, only InfoWorks Sim CN and XPSWMM supports initial abstraction. SWMM and Sim CNSWMM doesn’t.

- Sim engine doesn’t support the modified Green Apmt method.

- More analysis is needed to understand how different packages handles recovery during dry periods between storms.
