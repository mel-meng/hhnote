# How to use rational method in XPSWMM

Source: Innovyze Support Portal

---

### How to use rational method in XPSWMM

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-use-rational-method-in-XPSWMM)

### Introduction

This article shows how the single valued critical flow of the rational method has been implemented in XP-SWMM. Historically storm water design has been accomplished using the Rational method ensuring that each segment of the system can carry the flow of a return period that matches the time of concentration to that point. Using this method allowed a simple spreadsheet or tabular implementation but it is unable to take in to account storage effects of conduits and ponds etc. XP-SWMM is a dynamic program and routes hydrographs, when using the rational method the user needs to specify how long the constant flow will last and a hydrograph with a constant flow for that duration will be generated.

The Rational formula as typically implemented is shown below:

**Q = CIA**

Where,

C = Runoff Coefficient, a fraction between 0 and 1, dimensionless

I = Intensity from a Rainfall Intensity Frequency Duration Graph (IDF Curve), in/hr or mm/hr

A = Area of the drainage basin, acres or hectares

The rainfall intensity can be read from the IDF curve. An example is shown below, for the given frequency year, based on the time of concentration, the rainfall intensity can be read.

![](images\1_kM_3HaLjl-95jrn1U7lIAQ.png)

This formula yields the maximum flow expected at the point in the network with contributing area A upstream. The intensity is selected from a given return period curve using the time of concentration to the point for the duration on the graph.

### Example

In this example, we’ll setup a single node model with rational method. Start a blank xpswmm model, switch to RNF mode and create a node.

### Setup IDF Curve

Enter the IDF table into the model, so that XPSWMM can interpolate the rainfall intensity for us from the table. For example, if the Tc is 30 min and the return period is 5 year, then the intensity is 4.3 in/hr as shown below.

![](images\1_khhbXOOB7ir_86bwme6bHA.png)

Then we set the C value for impervious areas,

![](images\1_UkCpMKnBOw1ftiofFSD-Tg.png)

### Setup the subcatchment

As shown below, only the area and Imp (%) are used for the subcatchment, we can use 1 for width and slope so that it will pass the error check. Since we set impervious as 0%, only the pervious settings will have an impact on the results. We set C=0.68, tc=30. The 120 at the bottom is the duration of the constant flow to be simulated from the start of the simulation.

![](images\1_QHdB8rt8WrG5hq9H032skQ.png)![](images\1_2MHK9_p8sEtOW1Kx7g3ueQ.png)

**Note**: The hydrograph is not exactly 35.819 because of the conversion with units using cfs for flow and inches per hour for rainfall and acres for area. The conversion factor is actually 1.00833 and is normally omitted in hand calculations using the formula but included in the precision used by XP-SWMM.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [January 16, 2021](https://medium.com/p/b108392118ba).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-use-rational-method-in-xpswmm-b108392118ba)

Exported from [Medium](https://medium.com) on March 18, 2025.