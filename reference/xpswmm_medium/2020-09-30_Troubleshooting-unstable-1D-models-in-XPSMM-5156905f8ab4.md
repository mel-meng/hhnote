# Troubleshooting unstable 1D models in XPSMM

source: Innovyze Support Portal

---

### **Troubleshooting unstable 1D models in XPSMM**

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Troubleshooting-unstable-1D-models-in-XPSMM)

### What is model instability?

Due to the explicit nature of the numerical methods used for Dynamic Wave routing (and to a lesser extent, Kinematic Wave routing), the flows in some links or water depths at some nodes may fluctuate or oscillate significantly at certain periods of time as a result of numerical instabilities in the solution method. SWMM does not automatically identify when such conditions exist, so it is up to the user to verify the numerical stability of the model and to determine if the simulation results are valid for the modeling objectives ([Chapter 8.4 of EPA SWMM User Manual](https://www.epa.gov/sites/production/files/2019-02/documents/epaswmm5_1_manual_master_8-2-15.pdf)).  
   
Time series plots at key locations in the network can help identify such situations as can a scatter plot between a link’s flow and the corresponding water depth at its upstream node. Numerical instabilities can occur over short durations and may not be apparent when time series are plotted with a long-time interval. When detecting such instabilities, it is recommended that a reporting time step of 1 minute or less be used, at least for an initial screening of results.

### Common source of instability

Instability usually is the result of dramatic change in the calculation, common sources are,

* Challenging hydraulic conditions, flow over bumps, e.g. error in pipe invert to be above manhole invert
* Hydraulic jumps, great slope changes between pipes
* Complicated controls, complicated controls might have unintended side effects on the hydraulic routing results
* Switch of numerical solutions, pipe surcharged vs gravity flow, nodes overflowing vs not overflowing, river flowing over the bank, structures switching flow mode (weir flow vs orifice flow, etc)

### Troubleshoot instability

First step is to identify the pipe or node that is causing the instability.  
   
By tracing the instability upstream by checking the hydrograph we can quickly narrow down the areas that might cause it. Playing the HGL animation can also be a good way to quickly visualize the problem, the HGL will jump up and down at the nodes with instability issues.  
   
Another way to quickly narrow down onto problematic nodes is to review table E8. Review junctions with very high number of not converged iterations, and total iterations, etc.

![](images\1_cZj2Gw0sbPYkQRYKTR6X5g.png)

Due to the complexity involved in the numerical methods, troubleshooting instability is an iterative process of identifying possible sources.  
Once the source is identified, we should go through this checklist,

* Make sure the input is correct, no errors
* Is there a smooth flow path through the area, if not what might make the flow condition more challenging?
* Is the instability caused by switching mode? E.g. overflowing, surcharging, etc.
* Is there a boundary condition that might be causing it? Level, flow, etc.
* Any special controls might be causing it?
* Any model settings might cause it?

We’ll discuss each of them in more details below.

### Boundary condition

* Will the boundary condition cause any instability issues? For example, high water level will backflow into the system. Frequent changes in boundary water levels. Try a constant boundary condition to see if it solves it.
* Is the model initialized properly so that the initial boundary condition won’t cause stability issues? Initial depth or hot-restart file might be used.

### Challenging flow conditions

For example,

* Manholes overflows
* Pipe surcharges
* Overflow structure activation
* Flow line not smooth, removing the interruptions of the flow line usually will fix this type of problem
* Bumps, pipe invert higher than manhole invert
* Pipes with great slope changes (hydraulic jump might happen), if the pipe is too long and cannot accurately capture where the hydraulic jump happens, divide it into smaller segments.
* Channel with dramatic cross section changes, roughness changes
* Long pipes. XPSWMM route flow at pipe level without internal calculation points, and it assumes the flow condition within the pipe should be very similar across the full length of the pipe. Therefore, when the pipe is too long, and significant flow changes is expected within the pipe, the engine will have trouble to accurately simulate the flow, and in such situation the pipes should be divided into shorter pipes, especially for large diameter pipes, and a length of a few hundred feet is recommended.

In some cases, instability will be the expected behavior, thus it is the modeler’s responsibility to adjust the model to support the design goals. Maybe the modeler should increase the losses of the pipe so that it stayed in the surcharge condition during the simulation, which will result a more conservative result.

### Engine Settings

Sometimes, it could be the settings of the engine that is the source of the instability.  
   
If the time step is too long to capture the flow changes, it could lead to instability issues. Sometimes a time step of 1 second might be needed. It should also be noted that too short a time step might also cause stability issues.  
   
Using Table E7 in the 1D log we can get a report on the time steps. As shown in the example below, the average and smallest time step is 1 second, so a time step close to 1 second might be a better choice.

![](images\1_Yu8z3UOCHkOiP7SBq5svCA.png)

As shown below, the stability issue can be resolved by change the time step from 60 sec to 10 sec.

![](images\1_Xu3B1XfjfByAJkuiGrRTxQ.png)

When a pipe length is shorter than the wave can travel in a time step, it can lead to instabilities. Adjust the time step or make the short pipe longer to avoid this situation.  
If needed using [Configuration Parameters](https://help.innovyze.com/display/xps/The+Configuration+Menu#TheConfigurationMenu-ConfigurationParameters) to override default min. length and time step with MINLEN and MIN\_TS.  
   
You might also find [overwriting default settings](https://help.innovyze.com/display/xps/Hydraulics+Mode+Job+Control#HydraulicsModeJobControl-SimulationTolerances) useful.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 30, 2020](https://medium.com/p/5156905f8ab4).

[Canonical link](https://medium.com/@mel-meng-pe/troubleshooting-unstable-1d-models-in-xpsmm-5156905f8ab4)

Exported from [Medium](https://medium.com) on March 18, 2025.