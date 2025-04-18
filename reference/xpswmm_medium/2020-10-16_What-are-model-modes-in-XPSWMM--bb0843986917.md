# What are model modes in XPSWMM?

Source: Innovyze Support Portal

---

### What are model modes in XPSWMM?

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/What-are-model-modes-in-XPSWMM)

### The History

XPSWMM has 3 model modes, runoff, sanitary and hydraulics. These modes are originated from earlier versions SWMM. In the early days of SWMM, computers are not very powerful, therefore running a full simulation with both hydrology, hydraulics and water quality simultaneously is beyond the hardware limits. Therefore, the SWMM engine has an architecture to separate the different components as separate programs(blocks), that can take the output from another program as input. In this manner, the computer only needs to run one program at a time.

![](images\1_0BTns4lYpeEHmeyE4IjQjw.png)

The XPSWMM engine is based on SWMM and inherited the architecture in the earlier days. Fast forward to today, the computer hardware is no long a limitation, and the underlying engine is also evolved to run the hydrology and hydraulics at the same time without using an interface file. However, for backward compatibility purposes, the mode modes are still part of the user interface, and the user can still choose to run hydrology and hydraulics separately just like in the old days.

### The Modes

Runoff mode is the hydrology, it is similar to HEC-HMS. You can generate runoff from subcatchments, and you can also route flow through links using hydrology routing methods.

Hydraulics mode is the hydraulics, it uses the 1D shallow water Saint-Venant equations to route the flow through pipes.

Sanitary mode is for long term water quality modeling. By using a (???) routing method, it is suited for long term water quality modeling due to its simplicity and speed.

### Runoff + Hydraulics

XPSWMM models usually uses the runoff model to generate inflows to the network, and then uses the hydraulics mode to route flow. You need to switch to runoff mode to enter runoff parameters for subcatchments, and the hydraulic mode to enter invert for pipes and nodes.

![](images\1_ectNJHEV3rbf4DG-JVvx2A.png)

A common mistake is to setup the routing in pipes in both hydrology and hydraulics. When hydraulics routing is used, all the pipes should be disabled in the runoff mode.  
1. select runoff mode  
2. select all pipes  
3. disable all pipes  
4. all the pipes should be disabled shown as dashed lines

![](images\1_LFyjVkwoM0YIlNaRrv5jDw.png)

### Choose What to run

To tell XPSWMM what mode should be used for the simulation, go to the “mode properties”.

![](images\1_irKjFj5sd4Rt6jB_Qa2Z2A.png)

When the current model is selected, it will only run the current mode, which is the default setting. If you are in the runoff mode, it only run the runoff simulation without the routing.

![](images\1_zsFij6cRn09KHiY9DLLJUQ.png)

However, there is one exception. If in the “Hydraulics Job Control”, “Solve Runoff & Hydraulics Mode Simultaneously” is checked, XPSWMM will run both runoff and hydraulics.

![](images\1_5p7EdhoEneWCSr64B2LV9A.png)

As explained before, running Runoff and then use its output as input for hydraulics simulation was a compromise due to historical hardware limitations. In most cases, they should be run simultaneously.

You can also overwrite the default behavior of what mode to run when the run button is clicked.  
1. Uncheck “current model” if checked  
2. check the mode you would like to run

![](images\1_oh7NicM60Obkj9O77_j1sQ.png)

After this setting, regardless of the current model when the run button is clicked, the checked mode will be running.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 16, 2020](https://medium.com/p/bb0843986917).

[Canonical link](https://medium.com/@mel-meng-pe/what-are-model-modes-in-xpswmm-bb0843986917)

Exported from [Medium](https://medium.com) on March 18, 2025.