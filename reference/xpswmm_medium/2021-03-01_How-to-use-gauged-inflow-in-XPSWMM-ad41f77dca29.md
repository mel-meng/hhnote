# How to use gauged inflow in XPSWMM

source: Innovyze Support Portal

---

### How to use gauged inflow in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-use-gauged-inflow-in-XPSWMM)

Gauged inflow can bring in flow data saved in text file as the data source into XPSWMM. This option is flexible and easy to understand. Unless you are dealing with very large dataset, this should be the preferred option.

### Prepare

To setup gauged inflow, first prepare your flow data in a text format. CSV is a good format since it is supported by Excel. The csv file should have the following information,

* Date and Time: it can be one or several columns
* Flow: the flow field
* Station: the station field, you can have multiple flow time series saved in the same file.

As shown below,

1. check “Gauged Inflow”
2. Select a “File Format”, and the station name
3. Define the “File Format”
4. Map each column, for date time fields define the format

![](images\1_ge0VoLiGikTQLkxupiGH9A.png)

### Review

It is recommended to setup an XPTable to review your settings,

1. check the variables
2. bring in all the “Gauged Input Data” columns
3. Bring in the flag of gauged flow

![](images\1_A0nhw0FSMpN7aYvC4sNC3g.png)

### Package

One of the drawbacks of using external files is that the modeler needs to package the external files with the model when sharing with other people. XPSWMM made it easy with the transmit model tool. The “Transmit Model” tool will check the external sources and package the files in the zip file.

![](images\1_8btunv5xvQjfNLJjflndkg.png)

The sample model can be downloaded from [Github](https://github.com/mel-meng/xpswmm/blob/master/models/external_files/gauged_inflow.zip).

If you are interested using python to batch import the gauged flow, here is the [code](https://github.com/innovyze/Open-Source-Support/tree/main/01%20InfoWorks%20ICM/03%20Python/004%20hechms%20time%20series).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [March 1, 2021](https://medium.com/p/ad41f77dca29).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-use-gauged-inflow-in-xpswmm-ad41f77dca29)

Exported from [Medium](https://medium.com) on March 18, 2025.