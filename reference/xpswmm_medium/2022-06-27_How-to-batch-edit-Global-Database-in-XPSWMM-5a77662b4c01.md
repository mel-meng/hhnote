# How to batch edit Global Database in XPSWMM

source: Innovyze Support Portal

---

### How to batch edit Global Database in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-batch-edit-Global-Database-in-XPSWMM)

XPSWMM provides a very intuitive point and click user interface, which makes it very easy for users to start building a model.

However, when it comes to batch editing tasks, the window centric workflow might not work too well.

In this article I’ll show you how to use XPSTables to batch edit Global Database in the spreadsheet like user interface. This applies to most of the database types.

### RDII Database

For sanitary sewer modelling projects, the rain derived inflow and infiltration are defined in the RDII database.

![](images\1_b93BvsT8j6_C0fLXehvdww.png)![](images\1_qjwtdyCze7HhT6GOoFUhYA.png)

If you have 20 basins to calibration, it can feel quite tedious to change the rainfall for all of your profiles. An easier way is to use XPTables.

### RDII Database in XPTables

Go to XP Table and create a new RDII table under Global Database.

![](images\1_lH15Als6772qNG7FdpD8bw.png)![](images\1_N-z0aijaflwi4TICwjPAJQ.png)

Populate the table with all the fields in RDII,

![](images\1_9SoZT_gVfrTjykVqn8xopQ.png)

You might need to close the XPTables tab and reopen it to see the new table.

To change the rainfall profile in batch,

1. select the rainfall column
2. Click the block edit tool
3. set it to the new rainfall profile

![](images\1_rwlLPlNN5P-tZlzLsxwrLg.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 27, 2022](https://medium.com/p/5a77662b4c01).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-batch-edit-global-database-in-xpswmm-5a77662b4c01)

Exported from [Medium](https://medium.com) on March 18, 2025.