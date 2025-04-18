# What is a hot restart file in XPSWMM

Source: Innovyze Support Portal

---

### What is a hot restart file in XPSWMM

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/What-is-a-hot-restart-file-in-XPSWMM)

![](images\0_0Y1lW0GUvT4BzqVY)

Before getting into what is a hot restart file, let’s go through a few scenarios to get the context.

When the simulation starts unless we provide additional information of the water level in the nodes and pipes, the model will start dry without any water in the system. For most of the storm sewer system, this is the correct starting condition.

However, for sewer systems or storm systems that constantly having flow in the system. The assumption of starting with a dry system can lead to several issues,

1. the existing water in the system as the run starts might has significant impact on the results. The results could look quite different.
2. to overcome the above limitation we might need to warm up the system by running the simulation long before the event we are mostly interested. However, this will greatly increase the run time.
3. another less common situation is for certain tricky system, starting dry might get the model unstable. Therefore, starting from a slightly wet condition might get the model over that initial instability

As the above discussion shows, getting the correct initial condition of a system can be critical. Rather than manually set the initial depth of each node, we can simply run the model and save the state of all the water levels, etc. when the simulation ends. This is the idea behind hot restart file,

* hot: the system already has flow in it, no longer dry
* cold: the system is dry, no data from a previous run are used to warm up the system

Now if we go to the [online help](https://help.innovyze.com/display/xps/Hydraulics+Mode+Job+Control#HydraulicsModeJobControl-HotRestartHotRestart%28REDO%29), we can find more details on how to set it up..

### Hot Restart

A hot restart facility allows a file to be read and/or created to establish initial conditions for a run. This may avoid re-running of, for example, dry-weather flow conditions prior to the start of a storm runoff simulation.

![](images\0_0Y1lW0GUvT4BzqVY)

The user can create a hot start file from a normal run or from a previous hot start run. Only one hot start file can be created.

**Start Cold, Create Hot-Start File**

*Use case: create a hot-restart file for the future runs so that you don’t need to start the model a few days before the event to warm it up.*

If this option is selected then the model does not use a hot restart file to set initial conditions and creates a hot restart file for the next simulation run.

#### Start Hot Using Hot-Start File

*Use case: already have the initial condition simulated in a previous run, just need to start hot from it.*

If this option is selected then the model uses a hot start file to set initial conditions and does not create a new hot restart file for the next simulation run.

#### Start Hot, Create New Hot-Start File

*Use case: you might have a very long continuous simulation that you are breaking into a few more manageable runs. So you start with the hot-restart file from a previous run, but you’ll need to save the end state for the next run.*

If this option is selected then the model uses a hot restart file to set initial conditions and then creates a new hot restart file for the next simulation run.

### Import Tip: update hot-restart file when needed

If you read the 1D log, you’ll notice this section below. The XPSWMM engine uses internal IDs, which is unique for each model. Since the hot-restart file is implemented at engine level, the data are referenced only using internal IDs.

Any time you make significant changes to your model, the internal IDs might change for the node and it could cause problems.

![](images\1_y9EtgK3oxUAodDM96XMpLQ.png)

Therefore, it is a good idea to update your hot-restart file any time you make significant changes to your model.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 30, 2021](https://medium.com/p/a9f47e65075f).

[Canonical link](https://medium.com/@mel-meng-pe/what-is-a-hot-restart-file-in-xpswmm-a9f47e65075f)

Exported from [Medium](https://medium.com) on March 18, 2025.