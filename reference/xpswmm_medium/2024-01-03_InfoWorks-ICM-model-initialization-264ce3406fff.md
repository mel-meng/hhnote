# InfoWorks ICM model initialization

source: github

---

### InfoWorks ICM model initialization

source: [github](https://github.com/mel-meng/hhnote/tree/main/hydraulics)

![](images\0_vIf5Xs6OzFOSx1_9.png)

### Introduction

Model initialization is a crucial, automated step in model preparation. While it typically operates behind the scenes without user intervention, it can sometimes fail or cause undesirable starting conditions in complex models. Understanding the process and the common workaround techniques can help resolve these issues.

### Why initialize a model?

To understand model initialization, consider the analogy of an airplane preparing for takeoff. As an airplane requires a lengthy, flat runway to steadily gather speed for a smooth ascent, a model similarly needs to prime its ‘pipes’ with a steady, calm surface of water before introducing additional flows.

InfoWorks ICM builds this ‘runway’ by loading the initial flows, as determined by the input parameters, into the model as constant flows. This process continues until a steady state is reached, where the waters in the system remain calm as time goes by.

Once this ‘runway’ is established, the simulation can gracefully launch from this steady state, mirroring an airplane’s seamless takeoff from its runway.

In most models, this process works seamlessly at the beginning of simulation, and most people won’t even notice it happened.

However, for certain models, initialization can cause issues such as:

* Failure to initialize
* Undesirable initialized conditions, like a full storage tank after initialization

### Common causes for initialization issues

Achieving a steady state during initialization can be challenging. Several factors can cause a model to fail during initialization, including:

* Dry pipes: storm systems typically start in a dry state, which can cause the model to struggle during initialization. One potential solution is to introduce dummy inflows at the simulation’s onset to prime the pipes.
* Boundary Conditions: Models with boundary conditions that can cause backups at the start can take considerable time to reach a steady state as the empty pipes fill up. A potential solution is to initiate the boundary condition as a free outfall, then gradually increase the levels at the boundary during the simulation phase.
* Special Structures: Special structures such as gates, orifices, especially connected one after another is known hard to initialize. A potential solution is to simplify these structures, stabilizing the solution during the initialization phase.
* Tricky Flow Splits: for tricky flow split, minor changes in flow conditions can significantly change how flow splits. In these cases, studying the structure and simplifying it can make it easier for the solver to determine the flow split.

### Common solutions

When initialization fails, it can either fail immediately or get stuck. In the latter case, you can force stop the initialization and continue to the simulation phase. If your model struggles to initialize but works fine once the simulation starts, you can try to skip the initialization step. If not, you need to address the problems at the source.

You can skip the initialization,

* Force stop the initialization when it got stuck
* Use the initial state file saved previously to skip the initialization
* Use initial conditions object

Otherwise, you need to fix the problems at the source,

* Dummy inflow
* Start boundary condition from free outfall
* Simplify tricky structures
* Simplify tricky flow splits
* Bypass problematic objects using RTC rules
* Find a way to skip initialization.

We’ll get into details for each solution in the following sections. The first step is to review the timestep log to locate the problematic areas, refer to this [article](https://medium.com/@mel-meng-pe/infoworks-timestep-log-file-reader-f633c5147257) for more details.

### Skip the initialization

### Force stop the initialization when it got stuck

When the initialization got stuck, you can select the run (1), open the job progress window(2), and click the stop initialization button (3), and your simulation will move right into the simulation.

![](images\0_LRUcqLYZ3kTo688U.png)

### Use the initial state file saved previously to skip the initialization

If you can force stop initialization, you might want to save the state so that next time you run your model, you don’t have to manually stop the initialization.

1. Open your existing run and save the state at the end. Run the simulation and force stop the initialization if needed.

![](images\0_PeBYhanaxUcr1cS8.png)

1. Create a new run to use the previous run as initial state without initialization.

![](images\0_f6tiEWFskCCUYQXx.png)

### Use initial condition object

Using [initial conditions](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-3F4D9E73-18E5-470B-8761-BB3403F5FFA0) might also help the model to initialize.

### Dummy inflow

Using dummy inflow can be very effective for storm systems. The idea is to keep a constant flow inside the dry pipes until the rain event happens.

For example, if the peak flow in the pipes is 1000 cfs, you can introduce 10cfs flow into the model and that shouldn’t change the results significantly. And if you want to be more careful, you can time your inflow input so that it stops when the actual flow picks up.

Below is an example, for the initialization to work, you just need to enter flows in the first time step, which will be used as the constant flow.

![](images\0_YIHh9kaaTJ7SKvwV.png)

You can start by loading dummy inflows at a few upstream nodes that are on the longest flow paths.

### Start boundary condition from free outfall

Similarly to the dummy inflow method, you just need to update the level event so that for the first time step, the level is below the outfall invert, for example setting the value at 0.

To make sure once the simulation starts the rapid rise of the level will not cause issues, ramp up the level over a longer period maybe an hour instead of 10 minutes.

### Simplify tricky structures

A common problem is to have two structures connected, for example, “user control”->”flap gate”, “orifice”->”user control”.

Unlike a gravity pipe which has a volume that can change, that can operate on a much wide range of flow conditions. Controls are zero-length links that can only operate along a rating curve. Having two directly connected, we greatly reduced the likelihood of finding a solution.

The experiment below illustrates this point. In the model with the same inflow and boundary conditions, the only difference is the link between B and C as pipes, and orifice, etc. As the inflow oscillates, the boundary conditions changes, therefore, for the same flow the head conditions are different.

![](images\0_MDza1MwLH_us2jQU.png)

The comparison of the head difference between B and C and the flow is shown below,

* For pipes (red x), you can see for the same flow, the head difference can adapt to the changing boundary conditions. This shows that a pipe can operate on a much wide range of conditions for the same flow.
* However, for all other controls, the range is much smaller.

![](images\0_4Fv_BSZGRJTt_cZh.png)

You might try to add a dummy pipe between structures, this hack provides a buffer to allow the flow conditions transitioning between controls that would otherwise be impossible.

Another factor is the [drowning conditions](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-66F0B502-4BE9-428A-A2CD-D43047B2093C), once the tail end rises and breaks the free flow condition for the controls, the head difference will be used for the flow calculations. For controls that use modular limit, use 0.67 instead of the default 0.9 have proved to help in many unstable situations.

![](images\0_lESoirYFyMbDUgWv.png)

Unless the model is specifically built to test the operations of a facility, the controls can be greatly simplified. For typical planning models, we can treat the facility as a black box, usually it can be represented as a very simple system with an inlet, an outlet, a storage and a pump link. By focusing on building the simplest model that can achieve the operation goals of the facility, we can drop most of the details inside of the facility.

### Simplify tricky flow splits

An even flow split condition can be problematic for simulation, because with a shared water level at the splitting nodes, you need to solve all the connected pipes at the same time. Here are a few things you can try,

* Increase the initial flow through the flow split, in hope at a higher flow rate, it might be easier to solve.
* Adjust the split configurations, so that it is more obvious which way it will flow, maybe dropping one pipe a little lower, so that during low flow, all flow goes to one pipe.

### Bypass problematic objects using RTC rules

Another useful strategy for initialization is to use an RTC rule to divert the flow away from problematic pipes and structures to a dummy outfall during initialization. This will exclude these problematic model objects from the initialization calculation. See this [article](https://medium.com/@mel-meng-pe/how-to-keep-a-storage-node-dry-at-the-start-of-an-infoworks-icm-simulation-03bbc4160382) for more details.

### Less common ones

During initialization, RTC rules are ignored, therefore even if you are overwriting the RTC attributes in your RTC rules, making sure using correct initial settings.

### Conclusion

Model initialization is a vital step in the simulation process as it sets the starting conditions for the model. Understanding the reasons for initialization issues and implementing appropriate solutions is crucial. By troubleshooting and resolving initialization problems, users can ensure a successful initialization and smooth simulation. With a deeper understanding of the initialization process and the available workaround techniques, you can overcome challenges and achieve accurate and reliable simulation results.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [January 3, 2024](https://medium.com/p/264ce3406fff).

[Canonical link](https://medium.com/@mel-meng-pe/infoworks-icm-model-initialization-264ce3406fff)

Exported from [Medium](https://medium.com) on March 18, 2025.