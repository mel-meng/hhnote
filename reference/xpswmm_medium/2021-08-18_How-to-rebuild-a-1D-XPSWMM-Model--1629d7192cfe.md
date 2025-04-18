# How to rebuild a 1D XPSWMM Model?

Source: Innovyze Support Portal

---

### How to rebuild a 1D XPSWMM Model?

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-rebuild-a-1D-XPSWMM-Model)

XPSWMM/XPSTORM database can get corrupted from time to time, for example after a system crash. Corrupted database can lead to strange model errors that are hard to diagnose. If your model meet the following descriptions, you might want to rebuild your model.

* For a 1D model with less than 100 nodes, the \*.xp file should be less than 10M for most models. If your \*.xp file is larger than 50M, usually it has a lot of historical information saved, which can make data corruption more likely.
* Strange errors
* Model might complain about missing values which are not missing

### 1D XPSWMM Model Data Structure

According to the [online help](https://help.innovyze.com/display/xps/The+Database), XPSWMM saves all 1D model information in the following files,

* \*.xp: the main database
* \*.sqlite: sewershed geometry, scenarios
* \*.json: ensemble rainfall analysis input and results
* External files: time series interface file, time series text files, background layers, DTM files etc.

The table below shows a more detailed summary of data items and where they are saved.

![](images\1_Stfk4nlJbS2ymLCX4YR5cA.png)

### \*.XP Database

The main model file is the \*.xp database. \*.xp file saves model information as text command.

![](images\1_TFq3348VEy0POGnhHpCp8Q.png)

When lots of changes are made to a model, \*.xp database tends to grow significantly in size. Due to the complexity of the database format, not all the data added are used by the engine when running the model, and thus can cause unexpected issues. By rebuilding the database, we can purge the “junk” information out and this usually will fix the issues. Even if we get errors, usually they are much easier to fix because the process exposes the corrupted data items in the database.

### Scenarios

When rebuilding a model, special care is needed to ensure all scenarios are carried over. Scenario is managed using both the \*.xp database and a \*.sqlite database.

The main \*.xp database stores the base scenario. When a new scenario is created, XPSWMM compares the scenario to the base scenario, and saved the changes to the \*.sqlite database. So when rebuilding a model, the old \*.sqlite database need to be also renamed to match the new model.

RTC rules works differently than objects, where individual settings can vary in different scenarios. To apply a different RTC setting, a new rule needs to be created and enabled.

### Global Storms

Global storms saved in the global database will be carried over in \*.xp. If [ensemble](https://help.innovyze.com/display/xps/Tutorial+10+-+Creating+Design+Storms+and+Using+Global+Storms) is used, the \*.json file should also be copied.

### Rebuilding Model Procedures

Rebuilding a 1D model is a fairly straight forward process,

* Switch to the base scenario

![](images\1_ixARPSHkKbQL7BDRQ4fCQQ.png)

* Export the base scenario as \*.xpx file

![](images\1_rRl9SbbiM2pvNTB2KpcOIA.png)![](images\1_zNp6_jXjPtYkyHR-rQX4Vg.png)

* Start an empty model, and save it

![](images\1_Du2kcDvD_Cxpx8GkjnUWnQ.png)

* Import the \*.xpx file and save it

![](images\1_2u7wPFj4mndZ1C4ZVdMIAQ.png)

* Close XPSWMM
* Copy the old \*.sqlite model to the same folder as the new \*.xp file
* Rename the \*.sqlite to match the new model name

![](images\1_tO-GMlIizSGE5gmRsFJxFA.png)

* Open the new \*.xp file, save the model

### Review the new model

Many times, this is all you need to fix the issues. Sometimes, there will be additional work involved to get the model working.

Sometimes, this will expose corrupted data items and you should be notified in the warnings about missing values. By comparing with the old model, most of these errors can be fixed.

You can also bring some of the Xptables and styles by saving the existing model as a template and then apply it as the template, refer to the [template tutorial](https://help.innovyze.com/display/xps/Tutorial+11+-+Importing+Rainfall+from+Templates).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 18, 2021](https://medium.com/p/1629d7192cfe).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-rebuild-a-1d-xpswmm-model-1629d7192cfe)

Exported from [Medium](https://medium.com) on March 18, 2025.