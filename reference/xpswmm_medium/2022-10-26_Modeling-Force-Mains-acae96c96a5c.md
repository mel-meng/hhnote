# Modeling Force Mains

source: github

---

### Modeling Force Mains

source: [github](https://github.com/mel-meng/hhnote/tree/main/hydraulics/forcemain)

### Introduction

The hydraulic theory of a force main is quite simple, water flows pressurized inside the pipe, and the in and out flow rates are the same. We only need to get the friction loss and the minor losses (entrance and exit loss, etc.) correctly accounted for. Very similar to how a car go through a tunnel, everyone understands it.

However, within the context of a sanitary sewer system, the force main might not be flowing pressurized all the time. During the time the pump kicks on and off, the force main will flow with a free surface.

This switch between free surface (gravity flow) and pressurized flow can be tricky to model. And we’ll discuss that topic in a different article.

In this article, we’ll only focus on how the friction loss and minor losses are handled by the model when the force main is flowing full.

### Friction Loss

Friction loss is everywhere, you can slide easily on ice with very little effort, but much harder on the grass. The mechanics of the friction of water is a lot more complicated, but the idea is similar, smooth surface has less friction than rough surfaces. Commonly used friction loss equations are,

* Manning’s equation
* Hazen-Williams equation
* Darcy-Weisbach equation

Manning’s equation is widely used for open channel flow, for steady state flow, the friction slope is the bed slope (gravity is balanced by the friction force). For force mains, the Hazen-Williams equation is widely used in the United States due to its simplicity. The C-factors are available for commonly used pipe materials and sizes. The Darcy-Weisbach equation is most theoretically correct, however, getting the right friction coefficient can be more complicated.

In this article, we’ll use the equations shown below to hand calculate the friction loss using the modeling results.

* You will run the model and extract the modeling results. By setting minor losses at 0, the only head loss is the friction loss.
* Simulated friction loss = simulated upstream head — simulated downstream head
* Hand calculated loss = length of force main \* friction slope of pipe. As shown in the functions below, it can be calculated from the simulated water depth in the pipe (full when surcharged) and velocity. For full pipe flow R=D/4 (R is hydraulic radius, D is pipe diameter)

### Manning’s equation

When using the Manning’s equation, the friction loss is calculated as the friction slope.

![](images\0__aVKVc9mgIB8cHJD.png)

where,

* Sf is the friction slope (head loss per unit length) (ft/ft)
* n= the Manning roughness coefficient (sec/m1/3)
* R = the hydraulic radius of the flow cross-section (ft)
* V = flow velocity (ft/sec).

### Hazen-Williams Equation

![](images\0_YjkjThqaTbCbuGZe.png)

where,

* Sf is the friction slope (head loss per unit length) (ft/ft)
* C= Hazen-Williams C-factor coefficient
* R = the hydraulic radius of the flow cross-section (ft)
* V = flow velocity (ft/sec).

### Darcy-Weisbach Equation

![](images\0_kTrKpnEU3lT3aP6K.png)

where,

* Sf is the friction slope (head loss per unit length) (ft/ft)
* f= dimensionless friction factor
* R = the hydraulic radius of the flow cross-section (ft)
* V = flow velocity (ft/sec).

### Sample Model

A simple model with a force main is shown below.

![](images\0_MGoWDq16hwU_bela.png)

* Pipe length = 100 ft
* N = 0.0097|C=120|e=0.01 inch
* dZ = 11ft (upstream invert — downstream invert)

To test how the model calculates the friction losses, the inflow is ramping up from 2–7 cfs in 3 hours. We’ll compare the friction losses when the pipe is flowing full. To keep it simple, no minor losses are modeled.

![](images\0_y8YME-ve5tCEWaFF.png)

The models used in this article can be found in the “model” folder on github.

### SWMM5/ICM SWMM5

For SWMM5, you can model a pipe as a force main. It will automatically switch to gravity flow (dynamic wave) equations when it is flowing with free surface. You also have the option to model the pipe as a gravity pipe, and it will use the gravity flow equations when it is flowing full.

SWMM5 supports both the Hazen-Williams and Darcy-Weisbach equations for force mains.

![](images\0_XXRtadD8t3nQ_x87.png)![](images\0_TUDG9gXLUEL38jLz.png)

In ICM SWMM5, the data are entered differently.

![](images\0_EYosKs9HQAjID6Ri.png)

### Manning’s Equation for gravity pipe

For the pipe using gravity main solutions, friction loss is accounted for by the St. Venant equation in the form of the manning’s equation.

* When the pipe is flowing full, the friction loss calculated from the velocity and hydraulic radius is very similar to the simulated results (head difference of the upstream and downstream nodes)
* When the pipe is flowing partial full, the results are noticeably different

![](images\0_BpaU6g-mpXh7Cmka.png)

(refer to icm\_swmm.ipynb for the calculation.)

* Gravity\_f\_check: friction loss calculated from simulated velocity and assuming a full pipe flow.
* Gravity\_f\_sim: friction loss simulated, calculated as us\_head — ds\_head
* Gravity\_f\_check\_r: when the pipe is not flowing full, using the simulated depth to calculate the hydraulic radius.

### Hazen-William Equation

When modeling the pipe as a force main with the Hazen-William equation, it shows similar results.

![](images\0_W0J5AyQLELWcaAVX.png)

(refer to icm\_swmm.ipynb for the calculation.)

fm\_f\_check: friction loss calculated from simulated velocity and assuming a full pipe flow.

fm\_f\_sim: friction loss simulated, calculated as us\_head — ds\_head

fm\_f\_check\_r: when the pipe is not flowing full, using the simulated depth to calculate the hydraulic radius.

### Darcy-Weisbach Equation

The calculation for the DW is more complicated as the friction factor changes depending on the velocity. The only input is the surface roughness height (e). For more information refer to the SWMM5 hydraulics design manual.

![](images\0_OJP7k-E0K18A28Fa.png)

Using the calculation shown above, very close results are found between the simulated and hand calculation.

![](images\0_46BUUhBqVI8kq8-I.png)

(refer to icm\_swmm\_dw.ipynb for the calculation.)

* fm\_f\_sim: friction loss simulated, calculated as us\_head — ds\_head
* fm\_f\_check\_r: hand calculation using DW equation based on the simulated velocity, depth.

### ICM

For ICM, you can model the force main in several ways, a surcharged gravity pipe, a pipe that can automatically switch from gravity and pressurized condition, or a force main that is artificially kept full all the time. Refer to the [online help page](https://help2.innovyze.com/infoworksicm/Content/HTML/TechNotes/Modelling_of_Pressurised_Pipes_within_InfoWorks_ICM_and_CS.html) for more details.

To use force main friction equations in ICM, you need to use the force main solution model.

![](images\0_osrcD19FzcKpM4Zt.png)

The force main solution offers two type of friction equations,

* Colebrook-White equation
* Manning’s equation

The Hazen Williams method is a little confusing because it uses the manning’s equation internally, the C factor is converted to n.

![](images\0_glE_s6vQvGRx1i-e.png)

A few changes were made to the model after converting the SWMM5 model into ICM. The force main nodes were converted to break nodes so that they can be surcharged.

### Manning’s Equation

For the HW option, hand calculation is very similar to the simulated results.

* fm\_f\_sim: simulated friction loss: us total head — ds total head
* fm\_f\_check: manning’s equation calculated from the velocity and C factor (C=120 equivalent n=0.0097)

![](images\0_yskTDJXpzpVczqJW.png)

(refer to icm\_icm.ipynb for the calculation.)

### C-W Equation

For the CW option, it is very similar to the DW option in SWMM5, except that it assumes it is turbulent flow (eq. 7–33 in SWMM5 manual). And the results match very well with the hand calculation.

* fm\_f\_sim: simulated friction loss: us total head — ds total head
* fm\_f\_check: hand calculation using DW equation based on the simulated velocity, depth.

![](images\0_xJBUJgBi-VCjBKDw.png)

### Other Solutions

### Full solution

When using the full solution, a Preissmann slot is used when the pipe is surcharged/pressurized.

![](images\0_OxWWrUVkRAQEddtY.png)

An obvious effect of this approach is the upstream and downstream velocity will be different for the pipe. As shown below, when using the full solution, the downstream velocity is higher than the upstream velocity.

![](images\0__7-V28PhKZ7gKtnP.png)

With the use of the slot, the downstream end will have a smaller slot than the upstream end, thus with a higher speed. For longer pipes, the effect of attenuation will also be noticeable.

With the use of the slot, the velocity will be less than when the pipe is flowing full. Due to the complexity, it will be hard to reproduce the losses by hand.

As shown below,

* the blue line is the simulated friction loss by ICM
* When the pipe is following full, it is in general within the two dashed lines calculated using the manning’s equation with the simulated upstream/downstream velocity
* The orange line is calculated using the simulated flow to calculate the full pipe velocity. Due to the use of slot, this velocity will be higher than the simulated velocity therefor a higher friction loss

![](images\0_vMy_L6aapKx7lqvt.png)

### Pressure Solution

In theory, the pressure solution should work similar to SWMM5 force main solution, which will automatically switch between gravity and pressurized equations. However, I found that it is a little tricky for this model. When modeling the force main as a single pipe, it stayed as full soltuion all the time. After I split the force main into two pipes, the lower end of the pipe stayed pressurized and the results matches well with using the Manning’s equation.

![](images\0_BmFnnJJc7PYf_Ky6.png)![](images\0_Pi1wrlLjSYcZuFYp.png)

(refer to icm\_icm.ipynb for the calculation.)

### XPSWMM

For XPSWMM, you can only model a pipe using the gravity flow equations. If you do want to apply force main losses, there is a [workaround](https://help.innovyze.com/display/xps/Special+Conduits#SpecialConduits-PumpDischargePipes%28ForceMains%29) to adjust the pump curves by reducing the pumping head with the head loss through a force main for each curve entry.

When a force main is modeled as a gravity pipe, XPSWMM uses [a Priessmann slot](https://help.innovyze.com/display/xps/Flow+and+Head+Computation+during+Surcharge+and+Flooding#FlowandHeadComputationduringSurchargeandFlooding-EXTRAN5%28EXTRAN-XP%29) when the pipe is surcharged. One difference between XPSWMM and ICM is that ICM adds internal [computational nodes](https://help2.innovyze.com/infoworksicm/Content/HTML/ICM_ILCM/Simulation_Parameters.htm) within each pipe, therefore, the velocity changes throughout the pipe. While for XPSWMM/SWMM5, there is no internal points for the pipe, therefore, there is only 1 simulated velocity for the pipe.

Due to this simplification in XPSWMM, the friction loss calculated from the simulated velocity matches better in XPSWMM than in ICM, because the simulated velocity is an “averaged” value. As shown below the simulated (fm\_f\_sim) has good match to the one calculated from the simulated velocity using manning’s equation (fm\_f\_check).

![](images\0_UllHcllKjrw0LWyy.png)

(refer to icm\_icm.ipynb for the calculation.)

A second option is a [workaround](https://help.innovyze.com/display/xps/Special+Conduits#SpecialConduits-PumpDischargePipes%28ForceMains%29) to model the pump and the force main in the same multi-link as a system curve. And XPSWMM will adjust the pump curve head to account for the head loss through the force main.

![](images\0_jv0ZWELkTyZgEJIn.png)

Below is the 1D log showing the system curve in the table at the end (Flow rate vs Force Main).

![](images\0_7ZIDNPCmgHCJmTv2.png)

Modified head = original head — minor losses

Force main = original head — minor losses — friction loss

Friction loss is calculated using the flow rate, and manning’s n (0.01).

As shown below, the check column is hand calculated using the manning’s equation, and the results are very close.

![](images\0_45j6JYlASlBvUr5t.png)

### Conclusion

The equations describing force main hydraulics might be one of the simplest. However, implementing force mains in an unsteady state collection system model can be quite complicated because the fact the force mains can operate under both pressurized and free surface conditions. The implementation of force main varies in ICM/SWMM5/XPSWMM.

* In SWMM5, a force main can be modeled as a gravity pipe or a force main pipe. The difference is when modeled as a force main pipe, once it is under pressure, it will switch to either HW or DW equations.
* In ICM, a force main can be modeled as a gravity pipe (full solution) with a Preissmann slot solution when pressurized, using the pressure solution which will automatically switch to using pressurized equation when pressurized; or using the force main solution which will artificially keep the pipe flowing full all the time.
* XPSWMM doesn’t have a dedicated solution for force mains, it can only be modeled as a gravity pipe. However, XPSWMM provides a way to modify the pump curve to account for losses through force mains

### Appendix

Calculation can be found in the Jupyter notebooks on github,

friction.py: functions calculating the friction loss

icm.py: functions that load the csv export from ICM runs

Friction\_loss.ipynb: validate the code with text book examples and XPSWMM help document

Icm\_icm.ipynb: hand calculation for the ICM model/XPSWMM model

Icm\_swmm.ipynb: hand calculation for the SWMM5 model

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 26, 2022](https://medium.com/p/acae96c96a5c).

[Canonical link](https://medium.com/@mel-meng-pe/modeling-force-mains-acae96c96a5c)

Exported from [Medium](https://medium.com) on March 18, 2025.