# How to model culvert in SWMM5/XPSWMM?

Source: Innoyvze Support Portal

---

### How to model culvert in SWMM5/XPSWMM?

Source: [Innoyvze Support Portal](https://innovyze.force.com/support/s/article/How-to-model-culvert-in-SWMM5-XPSWMM)

### Theory

[FWHA HDS5](https://www.fhwa.dot.gov/engineering/hydraulics/pubs/12026/hif12026.pdf) is a great resource for sizing culvert with detailed background information on the theory and procedures.

With the help of the [HY-8 Culvert Hydraulic Analysis Program](https://www.fhwa.dot.gov/engineering/hydraulics/software/hy8/), a modeler can quickly get the performance curve, which can then be used as a “calibration” source when building more complicated models.

Another great source of culvert design is HECRAS, and the [reference manual](https://www.hec.usace.army.mil/software/hec-ras/documentation/HEC-RAS%205.0%20Reference%20Manual.pdf) has good information on how RAS implements and improves the FHWA method.

### Inlet Control vs Outlet Control

The theory is quite complicated, and the good news is that I don’t need to know the details for most design problems because I can rely on HY8 and HECRAS for quick calculations.

It does help to have some basic understanding of inlet and outlet control.

### Inlet control

Inlet control is when the inlet is limiting the flow that can pass through the culvert, so downstream condition doesn’t matter. In this case, empirical equations were developed to calculate the headwater depth. As shown blow, typically the inlet works as an weir or orifice and supercritical flow develops inside the culvert.

![](images\1_5v4tT_gAnNuTkUpiJRaevg.png)

For SWMM5/XPSWMM, both the dynamic wave equation and the inlet control equations are applied, and the results with higher water level on the upstream end will be used as the final results.

### Outlet Control

Outlet control is more complicated, both upstream and downstream conditions matters. And it is usually calculated using energy equations. And for SWMM5/XPSMM, it relies on the SWMM unsteady state dynamic wave engine to figure out the headwater depth.

![](images\1_T7VRpsAFWcYaV6HTV3OiAA.png)

### Modeling Culvert

As explained above, the only time the inlet equation will be used is when the program knows that it is a culvert, and it is in an inlet control condition. Otherwise, the calculation will be the same as any other pipe in the model.

For XPSWMM, the inlet edge type needs to be specified so that XPSWMM knows it is a culvert, as shown below, “Conduit Factors” needs to be enabled, and inlet edge design needs to be set other than “None”.

![](images\1_UwmPj-AMaRae9u57HqivIQ.png)

For outlet control, it is important to select the correct energy loss coefficient, refer to HY8 or HDS5 for the recommended factors.

It should be noted that SWMM5/XPSWMM uses the dynamic wave equation rather than the energy equation to solve for the outlet control condition. The main difference is that the dynamic wave equation conserves momentum rather than energy, therefore, very small difference is expected when comparing with steady state calculations.

Culvert calculation is summarized in the 1D log, Table E13 and E13a.

Table E13 summarizes the headloss and the headwater/tailwater. Table E13a summarizes the flow condition of the culvert, if there is time showing for the inlet control, then the inlet control equation will be applied.

![](images\1_mqxwCM1Mq_8TgM9gzcAuCA.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [February 9, 2021](https://medium.com/p/8bdac30c0b).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-model-culvert-in-swmm5-xpswmm-8bdac30c0b)

Exported from [Medium](https://medium.com) on March 18, 2025.