# How to effectively manage simulation results in ICM

source: Innovyze support Portal

---

### How to effectively manage simulation results in ICM

source: [Innovyze support Portal](https://innovyze.my.site.com/support/s/article/How-to-effectively-manage-simulation-results-in-ICM)

Some ICM models can produce large results datasets — sometimes in the order of tens or even hundreds of GBs per simulation. Large results datasets can lead to storage or file access issues. In this article we’ll discuss strategies to manage the size of modelling results files.

Description

When running hydraulic simulations in ICM, the importance of having a good strategy when managing results files becomes apparent over time. Storage requirements can range between orders of magnitude depending on user choices and will grow indefinitely if unmanaged.

Good results management practices result in a **streamlined modelling experience** (for instance, by improving performance when accessing results) and **prevent potential modelling disruption** (for instance, due to lack of storage).

### Before running — reducing the total results size

By default, simulation results are saved for all attributes in all objects in a network at a regular user defined timestep. However, users might only be interested in a subset of results. ICM provides ways to reduce results size, including:

* Increasing the simulation *Results Timestep Multiplier*
* Limiting detailed results to *Gauged Objects* with a smaller timestep multiplier
* Using the *Results Selector* feature
* Using the *Episode Collection* feature

### Results timestep multipliers

The frequency at which results are written during the simulation can be adjusted in the Run object dialog. This can be used to reduce the total results size without changing the simulation *Timestep*.

For instance, when a new *Run* object is created, it populates by default a *Timestep* of 60s and a *Results timestep multiplier* of 5. This means that whilst the simulation will never use a timestep higher than 60s (1 minute) when attempting convergence, it will only write results obtained every 300s (5 minutes).

![](images\1_Kw6KZIrEsSqeNPZBGOuohQ.png)

### Gauged timestep multipliers

There is also a a *Gauged timestep multiplier* field, which allows users to change the default multiplier for a subset of objects. By default this field is 1, so if a user drags a list of objects to the *Additional objects to be gauged* box, results for those objects will be written every 60s instead of every 300s.

Note that attributes for statistical values — such as maxima or total volumes — are calculated at the simulation timestep. However, statistics calculated once the simulation has finished — such as those seen in time series data plots — are retrieved from the results file, which only saves results at the multiplier timestep.

By setting 0 as the results timestep multiplier, no results will be saved for non-gauged objects.

![](images\1_17YwY3FkEt26MwDtXJ-CeA.png)

Note that such an approach should be used with caution where results — such as flooding — might be required from non-gauged objects. In this case it might be preferential to set a large multiplier so that such results are still recorded.

In summary, there can be two types of model objects grouped by granularity of results:

* **Gauged objects**: these are defined by a *Selection List* in the *Additional objects to be gauged* box. Their results timestep is defined in the *Gauged timestep multiplier*
* **Non-gauged objects**: these are all other objects not in the gauged selection list. Their results timestep is defined in the *Results timestep multiplier*.

More detailed information about this topic can be found [here](https://help2.innovyze.com/infoworksicm/InfoWorksICM.htm#HTML/ICM_ILCM/Schedule_Hydraulic_Run_view.htm?).

### Results Selector

A *Results selector* is a database object that limits the results generated from a run to only include attributes of interest. These can be selected using the *Results Selection* dialog. You can create as many *Results selector* items as required but only one *Results selector* item can be included in a run.

![](images\1_J2SLYP2wnACGXZc8-V13_Q.png)

This feature is available in ICM version 2021.6 and newer. More detailed information about this topic can be found [here](https://help2.innovyze.com/infoworksicm/InfoWorksICM.htm#HTML/ICM_ILCM/Results_Selection_Dialog.htm).

### Episode Collection

*Episode Collection* can be used to run the full hydraulic model only during key events (such as storms); runoff is simulated between episodes to maintain hydrological conditions. This can reduce the total results size for simulations with long durations by only returning the full hydraulic results when required.

Users can define key events manually, or by using statistics for the software to automatically detect them. This can be done by running the simulation in *runoff-only* mode throughout its entire duration to identify the events that will need further analysis. From there, a statistics report can be used to identify the *Episodes*.

![](images\1_Al-AniXzNHleelfG28RiCg.png)

More detailed information about this topic can be found [here](https://help2.innovyze.com/infoworksicm/InfoWorksICM.htm#HTML/ICM_ILCM/Episode_Collection.htm%3FTocPath%3DDatabase%2520Items%7CEpisode%2520Collection%7C_____0).

### After running — managing results datasets

### Results storage mechanism

ICM simulation jobs are managed by ICM *Agents*.

Most standalone users request that their *Local Agent* (the Agent on their machine) runs a simulation to be stored in a *Local Results Folder* (a results folder on their machine). In this case, the Agent will store results directly on the user’s *Local Results Folder*.

However, users taking advantage of the *Workgroup* functionality can request that simulations are run on a *Remote Agent* (a different computer) **or** that results files are stored in a *Remote Results Folder* (a common results server). In this case, results are temporarily cached in the *Working folder* of the Agent running the simulation. After the simulation finishes, the complete results dataset is moved to the results folder (either *local* or *server*). The results files are removed from the *simulation Agent working folder* once they are successfully transferred.

![](images\1_BtCPkjkKgNx40TWpt7tfmQ.png)

Note: usually, space in the default Agent working folder is enough to temporarily cache most results datasets. However, it is possible that simulations producing large results datasets require more than the available space in this drive, which will result in a failed simulation. This is compounded if multiple concurrent simulations are running in one single Agent and caching results simultaneously.

### Local results folder

By default, simulation results are saved locally on the user’s C drive. This is generally the fastest and most robust way to access results. Results which are local to the user interface benefit from good access speeds (system drives are generally fast) and do not suffer from latency bottlenecks which can occur in networked folders.

Local results folders can be cleaned up by using in-built tools which remove files generated when viewing results. This will not remove time-varying results.

![](images\1_yTRQ0IIcporGe_gfQjcjqg.png)

### Remote results folder

Users can take advantage of the *Workgroup* functionality and store results on a server. This is done by setting up a *Remote Results Root*, which is typically a network folder.

If you have a server with large storage capacity, users can move or save simulation results to a remote folder. This would likely warrant discussions with IT to insure the software has permissions to write to the folder.

![](images\1_mI-a3lb4n9NElmJTpOh2GQ.png)

Using Remote Results allows:

* Team users of a Workgroup to access the same set of results without having to rerun them.
* Local users to save space on their local drives.
* Remote simulation machines to store results directly to the results server, so users can issue sets of simulations to run on specialised machines and disconnect their local machine.

Note that the Remote Results functionality was designed primarily for local networks. Users accessing results remotely need to insure they have a fast and reliable connection to the results files. Accessing them over an internet connection or on a slow disk will result in significant performance when degradation interrogating results, particularly for large results datasets.

### Results Manager

The *Results manager* can be used to manage results in bulk. It can be opened by right clicking on a master group or model group.

![](images\1_SmTqyZW3po0JXinWdlAQxw.png)

Once open, a number of options will exist for each simulation depending on their state and save location. These include moving or deleting different types of results files. Deleting results files still maintains the Run object, should users need to re-run simulations in the future.

![](images\1_tfqLF-pwrPcrMbFKTgQVEA.png)

More detailed information about this topic can be found [here](https://help2.innovyze.com/infoworksicm/InfoWorksICM.htm#HTML/ICM_ILCM/Results_Management.htm?).

### Saving results to server

Simulation results can be stored directly to the remote results server once the simulation is finished. To do this, select the *Store results on server* option in the dialog that shows once a run job is requested. This option is only available once you have configured a *Remote results root* and if your *Local Agent* is connected to a *Coordinator Agent*.

![](images\1_f5qptG851ilrHthBbOlQeQ.png)

### Archiving runs

One way to archive runs is by using transportable databases. These are single files which can be stored in a location that does not require fast access.

* Create a new transportable database.
* Copy the run or the report.
* Paste the run or report into the transportable database. ICM will get all the required database items to re-run the simulation or report to the new database

If you plan to re-run the model, you should say yes to copy all the data and objects. If you also want to include the results rather than having to re-run it, say yes to copy the simulation results.

### Workgroup functionality

For more advanced application, ICM offers a very powerful and flexible collaboration platform to manage teams and models that require frequent collaboration, high-end computing, and fast and large storage. Refer to the following documents for more information.

* [Workgroup Platform Release Notes](https://innovyze-emea01.s3-eu-west-1.amazonaws.com/WorkgroupProducts/Dropbear/2021.6.1/ReleaseNotes.pdf)
* [Workgroup Data Server Administration](https://innovyze-emea01.s3-eu-west-1.amazonaws.com/WorkgroupProducts/Dropbear/2021.6.1/WorkgroupDataServerAdministration.pdf)
* [Configuration of Simulation Agents](https://innovyze-emea01.s3-eu-west-1.amazonaws.com/WorkgroupProducts/Dropbear/2021.6/ICMSimAgentConfig.pdf)
* [IT Architecture](https://innovyze-emea01.s3-eu-west-1.amazonaws.com/WorkgroupProducts/Dropbear/2021.1/Innovyze+Workgroup+Products+IT+Architecture.pdf)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 6, 2023](https://medium.com/p/cb19238dfe56).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-effectively-manage-simulation-results-in-icm-cb19238dfe56)

Exported from [Medium](https://medium.com) on March 18, 2025.