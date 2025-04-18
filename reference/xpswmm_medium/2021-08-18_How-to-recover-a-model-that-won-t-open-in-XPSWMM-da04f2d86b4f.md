# How to recover a model that won’t open in XPSWMM

Source: Innovyze Support Portal

---

### How to recover a model that won’t open in XPSWMM

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-recover-a-model-that-won-t-open-in-XPSWMM)

If your XPSWMM model won’t open, here are a few things you might be able to do to recovery the model.

### XPSWMM Model Files

Refer to the help for more information about the structure of the model database, and how model edits are saved to the files.

[**The Database**  
*XPSWMM maintains an internal database that integrates the spatial data associated with an object with the attribute…*help.innovyze.com](https://help.innovyze.com/display/xps/The+Database "https://help.innovyze.com/display/xps/The+Database")

Here are a few important facts related to recovering a corrupted model,

* XPSWMM stores the model data in a few files. When an XPSWMM model is open, everything is loaded into the memory, until the model is saved the model will not be updated on the hard drive.
* XPSWMM also creates a copy of the model file when it is open with the extension of \*.bak. In case the model crashes, the \*.bak file will have the copy before the crash.
* When a model is opened with a newer version of XPSWMM, a copy of the original \*.xp file will be created with the suffix of the database version.

### Recover a model

Below are the options,

* If there is a \*.bak file in the model folder, change the name of the \*.xp to \*\_copy.xp, then change the \*.bak file to \*.xp. See if the backup model will open.
* If there is a \*.xp file with the suffix of a database version. Change the name of the model \*.xp file to \*\_copy.xp, rename the \*.xp file with the suffix to the model name, see if that model opens.
* Some models can be partly restored by making a new model and then merging incrementally the links and nodes, the Job Control and the Global Database records if no .bak is available.

![](images\1_aUuaYsabx2kTraL6uDfo0A.png)![](images\1_8jPQppMo7yDUjlOFzDjVXA.png)

### Recommendations

As an XPSWMM model grows in size over time it is important to be prepared for possible data corruption. Making copies of the model at key milestones such as the end of each phase is good practice. Using the “transmit model” tool to create zip files for a snapshot of the model.

![](images\1_c4qIuQSCnJfbBY6vGGGB_w.png)

For models with a long history spanning many versions of XPSWMM the model might need to be rebuilt from time to time to purge out the unused objects in the database. Next time you pick up an old model, check its size. For most XPSWMM models, its size should be well under the 50M mark. If you have a model larger than 50M, it is a good idea to [rebuild it](https://mel-meng-pe.medium.com/how-to-rebuild-a-1d-xpswmm-model-1629d7192cfe).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 18, 2021](https://medium.com/p/da04f2d86b4f).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-recover-a-model-that-wont-open-in-xpswmm-da04f2d86b4f)

Exported from [Medium](https://medium.com) on March 18, 2025.