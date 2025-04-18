# How to reduce the size of simulation results of an ICM model?

source: Innovyze Support Portal

---

### How to reduce the size of simulation results of an ICM model?

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-reduce-the-size-of-simulation-results-of-an-ICM-model)

For large models with long simulation time, the results can grow very quickly and filling up the disk space. In this article we’ll discuss a few strategies and techniques to manage the growing size of the modeling results.  
When ICM runs a simulation, behind the scenes ICM sends the model to an agent, the agent will first run the simulation and save the results in its working folder, after it is done, then send the results back to the results folder. In most cases, we don’t need to worry too much about what is happening in the working folder of the agent, as after the simulation is done the files will be deleted soon. Refer to links under workgroup functions for more information.  
In this article we’ll focus on managing the results saved with the simulations.

### Strategies of managing modeling results

When using a standalone database, by default, the simulation results are saved on the local drive. If more storage is needed, we can use the remote results root to save or move results to a networked drive to free up space on the local drive.  
For more flexibility, we can use a workgroup master database and a remote agent to run the simulation to pool computing and file storage resources for a team. With this setup, the team cannot only off load results to a networked location, but also can share the models with team members.  
To meet the storage needs, we have approaches,

#### Add more storage to the system

* Use larger hard drive for the desktop computer if results are saved locally
* Use remote results folder on networked location if network storage can be more easily and cheaply added

#### Reduce modeling results size

* Custom the run so that only results that will be used are stored
* Delete the working runs that are no longer needed
* Delete the results of runs if we can afford to rerun the model to get the results
* Move the results of runs to a remote folder
* Archive the results of runs off the main storage system

### Use remote results root

If you have extra storage on the server, you can also move or save your simulation results to a remote folder. You need to work with your IT staff to make sure you have the needed permission to write to the folder.

![](images\1_vMVyUQndozF05U3uq2-r2g.png)![](images\1_ADKcCBiBhIr4XHzviTIBoQ.png)

### Reduce results size in a run

By default, the simulated results for all the objects in a model are saved. In most cases, we are only interested in getting detailed results for a very small number of objects in the system. ICM provides a few ways to reduce the results size,

* Increase the results time step
* Limit the detailed results to gauged objects
* For continuous simulation, use Episode collection to limit the results to a few events

![](images\1_Hj-csFX_nvjShtuXWYgcKw.png)

Timestep is the time step the engine uses internally to keep track of the flow, depth, etc. as the time progresses. For statistics such as max., min. and volumes, etc., they are calculated directly from the internal results at each calculation time step.  
When we plot the hydrograph and other time series data, they are retrieved from the results file, which only save the results at the specified results timestep. As shown in the screenshot above, for a timestep of 60 sec, a 5 results timestep multiplier will write results every 5 minutes.  
We can further reduce the size of the results by gauging the model objects. When gauging the model objects, we have two groups of model objects,

* Gauged objects: these are defined in a selection list in the “Additional objects to be gauged” box. The timestep of these objects will be defined in the “Gauged timestep multiplier”
* Not gauged objects: these are the objects not in the gauged selection list. And the timestep is defined in the “results timestep multiplier”.

An example is shown below, by setting a 0 results timestep multiplier, there will be no results for model objects except those defined in the flow meter selection list FM, and the results will be reported at 5 min interval.

![](images\1_PTOdeygm178RXSPJAoLDaA.png)

For long continuous simulations, we can greatly reduce the simulation size if episode collection can be used. As shown below,

* For example, we run the simulation through the whole period first to identify all the events that will need further analysis. From there, we can keep improving the model, and only run the model for these important events
* We can define a few key events as episode collection and only run the model during these periods
* To keep the hydrology accurate, we can simulate only the runoff between the episodes

![](images\1_9eZWUy5lEriObmtT-Ll1kA.png)

### Delete results of runs

Deleting simulation results can free up storage, and we can use the Results manager to view all the runs in a master database.

![](images\1_B5Kw5N_4PcwQj8npT7ph0w.png)

You have the option to delete all the results files, selected simulation, etc.

![](images\1_RLaZV0_2ByZFym6FM4jWrQ.png)

### Move results to remote results folder

When using a standalone database, by default the simulation results is saved locally in the default results folder. You can clean up the results folder to free some space.

![](images\1_SgTWdljjfRgp2fX2aK2r_Q.png)

To move the results to a remote results server, you can use the results management tool

![](images\1_fNChJLY16utB4Q86zp1XSw.png)

To save the results directly to the remote results server, after starting the run, choose the store results on server.

![](images\1_dx98B3KWMXOZA-GPfWBVYQ.png)

### Archive runs

The easiest way to archive a run is using a transportable database.

* Create a new transportable database

![](images\1_uqsew1k1zJICQNcygKR5cw.png)

* Copy the run or the report.

![](images\1_-fN4mklFd2xfBvg-1vwawA.png)

* Paste the run or report into the transportable database. ICM will get all the required database items to re-run the simulation or report to the new database

![](images\1_yEDdzzC9i5OhOhVrCERlAQ.png)

* If you plan to re-run the model, you should say yes to copy all the data and objects. If you also want to include the results rather than having to re-run it, say yes to copy the simulation results.

### Workgroup Functions

For more advanced application, ICM offers a very powerful and flexible collaboration platform to manage teams and models that require frequent collaboration, high-end computing, and fast and large storage. Refer to the following papers for more information.  
· [Workgroup Platform Release Notes](https://innovyze-emea01.s3-eu-west-1.amazonaws.com/WorkgroupProducts/Dropbear/2021.6.1/ReleaseNotes.pdf)  
· [Workgroup Data Server Administration](https://innovyze-emea01.s3-eu-west-1.amazonaws.com/WorkgroupProducts/Dropbear/2021.6.1/WorkgroupDataServerAdministration.pdf)  
· [Configuration of Simulation Agents](https://innovyze-emea01.s3-eu-west-1.amazonaws.com/WorkgroupProducts/Dropbear/2021.6/ICMSimAgentConfig.pdf)  
· [IT Architecture](https://innovyze-emea01.s3-eu-west-1.amazonaws.com/WorkgroupProducts/Dropbear/2021.1/Innovyze+Workgroup+Products+IT+Architecture.pdf)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 6, 2021](https://medium.com/p/19b85b922179).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-reduce-the-size-of-simulation-results-of-an-icm-model-19b85b922179)

Exported from [Medium](https://medium.com) on March 18, 2025.