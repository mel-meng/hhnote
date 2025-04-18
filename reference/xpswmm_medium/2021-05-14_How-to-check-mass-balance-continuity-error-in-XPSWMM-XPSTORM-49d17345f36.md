# How to check mass balance/continuity error in XPSWMM/XPSTORM

source: Innovyze Support Portal

---

### How to check mass balance/continuity error in XPSWMM/XPSTORM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-check-mass-balance-continuity-error-in-XPSWMM-XPSTORM)

XPSWMM hydraulic engine routes flow in the model by solving [dynamic wave](https://help.innovyze.com/display/xps/EXTRAN+Theory+-+Dynamic+Wave+Solution) partial differential equations. Numerical errors are inherent to the numerical methods. To ensure the errors are within acceptable range, continuity error is widely used as a quick way to evaluate the model health.  
   
Continuity errors are reported in the simulation logs: 1D Log and 2D Log,

![](images\1_Tjv6aPs_hqfJpJnfPr2I1A.png)

Since 1D and 2D use two separate engines, continuity errors are reported separately.

### 1D Continuity Error

XPSWMM reports 1D continuity error at both system and node level in the 1D log.  
   
Continuity error at junction level is reported in Table E18, a sample is shown below.  
   
The numerator should be zero if there is no error. This volume error is then normalized by the denominator of the total flow and the average volume of the node at the start and end of the simulation.  
   
XPSWMM gives references to typical error ranges from excellent to terrible.

![](images\1_iIgiX6_QObTOIDBkLWrK8Q.png)

Nodes with larger errors should be reviewed, as shown in the sample table blow, especially nodes with very high continuity error both in terms of volume and percent of inflow should be reviewed to reduce the errors. Error in model input data are common sources (e.g. wrong invert, rim level of manholes, wrong invert of pipes, etc.) of high continuity error.

![](images\1_89XxJV-yv8nylP5IETeWmg.png)

Table E21 shows the system continuity error. A sample is shown below, it lists all the inflow and outflow sources, and the system continuity error as the difference between the inflow, outflow and the system volume changes.

![](images\1_jjHDldzKdqJIUrIavRCfQA.png)

Table E22 reviews the results in both E18 and E21, and gives recommendation on the overall continuity.

![](images\1_NePrgluydD5PFSuA2MqNug.png)

When the continuity error is poor, the modeler should investigate the model to identify the sources to reduce the errors. In the case the modeled system has challenging hydraulic conditions, the modeler should demonstrate the higher than ideal continuity error is not impacting the results for making engineering decisions. For example, by building scenarios to get the likely range of flow conditions after simplifying the parts that are causing the high error.

### Common sources of high continuity error

### Time Step

Using too big a time step can lead to high continuity error. Check table E7 for the minimum time step.  
As shown in the example below, the average and smallest time step is 1 second, so a time step close to 1 second might be a better choice.

![](images\1_ivpInGLDfl-f6IiFRytjPg.png)

### Rating Curves

Rating curves should start with 0, 0 for the first row.

### Pumps without wet well

Wet well volume for a pump station not properly setup as storage node.

### Short Pipes

When a pipe length is shorter than the wave can travel in a time step, it can lead to instabilities. Adjust the time step or make the short pipe longer to avoid this situation.

If needed using [Configuration Parameters](https://help.innovyze.com/display/xps/The+Configuration+Menu#TheConfigurationMenu-ConfigurationParameters) to override default min. length and time step with MINLEN and MIN\_TS.

### Long conduits

Since XPSWMM assumes a single straight water surface within the pipe without any additional calculation points, very long pipes should be broken into smaller segments to better capture the true water surface.  
Especially for long pipes with great slope changes at one end, which tend to cause hydraulic jump situations, and a shorter pipe can more accurately capture the situation.

### Poor initial condition

System will large storage that will take time to fill up before routing happens will show large continuity errors. Proper initial condition should be established using initial condition or hot start file.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 14, 2021](https://medium.com/p/49d17345f36).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-check-mass-balance-continuity-error-in-xpswmm-xpstorm-49d17345f36)

Exported from [Medium](https://medium.com) on March 18, 2025.