# How to speed up an ICM 2D simulation

source: Innovyze Support Portal

---

### How to speed up an ICM 2D simulation

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-speed-up-an-ICM-2D-simulation)

For an ICM 2D model that takes hours or even days to run, it could greatly impact the schedule of a project. In this article, we’ll discuss a few quick steps to identify areas for improvements.

Below are the common areas to look into,

* Make sure the model is using all the CPUs and GPUs
* Make sure the time step is appropriate
* Identify speed bumps in the model

### Check the Simulation Log

The first place to visit is the simulation log,

![](images\1_00Hr6YH9EXhNdtHyqKvC2Q.png)![](images\1_jDFROgQFJ2xxw0-x1FxotQ.png)

At the end of the log file, you can find the information about how many CPUs and GPUs are used for the simulation.

![](images\1_a1KHWW8bSxDOMPF6p8EN-Q.png)

To change the number of CPU threads used,

1. when running the model
2. in general you should use the “Let agent set limits” to decide how many CPUs to be used for the simulation.

![](images\1_jH-oWeXQjo3lC81KkujrPg.png)

For GPU, make sure “if suitable card is available” is selected.

![](images\1_6jH4qMD82BoWW1CBsGD0ow.png)

### Check the run time

When the model is running, check the run time information in the Job “Progress window” to get a sense how smooth the computation engine is running.

![](images\1_IURrnddjpBn5O1hbLf6UYQ.png)

Watch the changes of the job progress for a while, both during a “normal” period and during “peak” events.

As shown below,

* timestep and failed link and nodes can reveal model elements that is struggling to converge, a good place to start investigation, the time step might need to be tweaked to match the number showing
* Min. 2D timestep: if the value is below 0.1 sec, a sign the 2D model is not optimized.

![](images\1_l2Kt11JTjQb95ABoRcEMGg.png)

### Optimize 1D

The links and nodes that failed to converge very often should be reviewed to rule out data entry errors. And simplifying complicated hydraulics conditions might also help to speed up the simulation without significantly changing the simulation results. In general, making the flow line smooth will help. Using consistent slope, diameter, roughness values with connected pipes, removing the bumps, etc.

### Optimize 2D mesh

The more elements in the mesh the more time it takes to run the model, the more calculation that needs to be done for each mesh element the more time it takes to run.

Things we can do to reduce the calculations on each element,

* calculation is only carried out for wet elements, therefore, rain on the mesh will greatly increase run time.
* infiltration and other hydrology calculations on the mesh will increase run time
* complicated triangulation will create small and odd shaped triangles which can slow down the calculation
* tricky 1d/2d interfacing can lead to more computations

Things to check for reducing the number of mesh elements,

* conduit 2D with small diameters (< 3ft) can lead to small elements
* simplify and reduce number of vertex of geometries added to the 2D mesh (polygons, river banklines, etc.)
* using terrain sensitive meshing, mesh zones, etc. to fine tuning the details only in areas needed

By [Mel Meng](https://medium.com/@mel-meng-pe) on [March 31, 2021](https://medium.com/p/5c8dd3ef435).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-speed-up-an-icm-2d-simulation-5c8dd3ef435)

Exported from [Medium](https://medium.com) on March 18, 2025.