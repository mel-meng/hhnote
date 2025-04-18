# Paths in XPSWMM

source: Innovyze Support Portal

---

### Paths in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Paths-in-XPSWMM)

XPSWMM generates lots of files when running simulations. Getting familiar with the folder structures and how the results are organized can be helpful if you need to “hack” your way to get the results outside of the XPSWMM UI.

### A Simple Example

A typical XPSWMM model is managed in its own folder as shown below,

![](images\1_pOrdjcBeBkpwuTuqW2cRmw.png)

There are a few files share the base name of the model, “model.\*”, they are the main [database](https://help.innovyze.com/display/xps/The+Database) of the model,

* model.xp is the main database of the model
* model.sqlite stores other information, most important is the scenarios
* model.json has rainfall data

The modeling results are saved in the 1D and 2D folders.

For models without scenarios and global storms, the results are saved under the subfolder of 1D or 2D with model base name as shown below,

![](images\1_I4d3ISeRUCPqUby_8NA0rw.png)

* the \*.dat file is the 1D input file
* the \*.out is the 1D log file
* other files are results files

The 2D folder, results are organized in subfolders

![](images\1_-eqne24fpeFdICLXZBKvhA.png)

* Data: the input data folder for the 2D model
* Log: the log of the 2D results
* Output: the 2D simulation results
* Check: you might have a check folder if the check files are generated

**NOTE**: you can have multiple models in the same folder, and each will create a subfolder in the 1D/2D folder to store its results

### Scenario & Global Storms

When using scenarios and global storms, XPSWMM will run a combination of the two for a list of simulations. For example if we have 3 scenarios, and two global storms, you’ll get 2\*3=6 simulations

![](images\1_JcW6O5pkd-6UCmInHHiqQA.png)![](images\1_q0-l0NtX4h3FATC8_QZhkw.png)

After running the model, we’ll have the following runs in the 1D folder,

![](images\1_0EtLO4MbwH7vmI3zvr9DPw.png)

The name of results folder for each run is defined as, “base\_scenario\_global storm”. **Therefore, it is important to make sure the names of the model, scenario and storm is not too long, the path can grow very quickly.**

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 28, 2021](https://medium.com/p/ee42bbdd1003).

[Canonical link](https://medium.com/@mel-meng-pe/paths-in-xpswmm-ee42bbdd1003)

Exported from [Medium](https://medium.com) on March 18, 2025.