# How to add rainfall to ICM using TSDB ? — Part 2

Source: Innovyze Support Portal

---

### How to add rainfall to ICM using TSDB ? — Part 2

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-add-rainfall-to-ICM-using-TSDB)

In [part 1](https://mel-meng-pe.medium.com/how-to-add-rainfall-to-icm-using-tsdb-part-1-d385645d66d) we imported rainfall into a TSDB from an existing rainfall event file. In part 2, we will create rainfall in TSDB from scratches.

1. prepare the source data
2. create a TSDB
3. connect to the data source
4. add TVD connectors

A great way for new users to learn how TSDB works is to import from an existing model (see [part 1](https://mel-meng-pe.medium.com/how-to-add-rainfall-to-icm-using-tsdb-part-1-d385645d66d)), and then study how the import tool sets up the TVD connectors.

In this example, we will recreate the model in [part 1](https://mel-meng-pe.medium.com/how-to-add-rainfall-to-icm-using-tsdb-part-1-d385645d66d) by connecting to a csv file.

### Prepare the CSV files

First, let’s copy the rainfall data from the event file to excel and save it as a csv file.

![](images\1_77PAATemd19pyZLYixMnlA.png)

Refer to the help file “Time Series Database” for more information on other formats that can be connected to TSDB.

![](images\1_-ADU-OuSX4OSXHnlVW2GGQ.png)

For simple CSV format,

* there is no header
* the first column is time, and it should be dd/mm/yyyy hh:mm format
* the second column is value

![](images\1_ET9fZVCshuIdzCv2az_Lrw.png)

It is important to leave the header out, otherwise, it will be treated as a data point from 1900 and the time series won’t plot correctly.

Prepare the time series data for rg1, rg2 as rg1.csv, rg2.csv

### Create the TSDB

Next create a TSDB and setup the data source.

1. Create the TSDB
2. add a new entry in the data sources tab
3. give it a name and choose “Simple CSV”

4. Paste the folder path where the csv file is saved

![](images\1_LszbZiaoMq34VzuWvmZ6Kg.png)

5. It is important to have time zone set, otherwise it will default to system time zone which can vary when the model is running on a different computer. **NOTE:** Since some common external data sources such as radar rainfall uses UTC time, also with the complication of daylight saving time, it is important to choose the correct time zone for all data sources.

![](images\1_LIR5OtnfgIrkBOAyF0oQ7g.png)

Populating the observed tab for each data stream is straightforward,

![](images\1_AKn5OIzdrtXH3E_5ewc_Lw.png)![](images\1_llaHJ07oa51ZmfGHBdvAhA.png)![](images\1_g9NvDOfm-RwZGLdm91VryQ.png)

When we load data for each stream, once the data is loaded, it will move data to the loaded folder and empty the rows in the file.

![](images\1_WpEqKrFWxVaqBdkEuLWRMQ.png)

Now if we check the data folder, we’ll see rg1.csv and rg2.csv are now empty, and the loaded data are copied in the “loaded” folder.

![](images\1_ErGcyRlmsTjgiiUZKhqX8w.png)

The rainfall can be viewed as shown below,

![](images\1__qI59KoT5LPaoiNY4wHMyw.png)

### TVD Connector

To create TVD connector,

1. open the network in GeoPlan
2. drag the TSDB into the GeoPlan
3. create the TVD connectors for the rain gauges

In this example, we will reference the rain gauges only as rainfall profiles in the subcatchment attributes. All we need to do is to create two TVD connectors so that the network is aware of the source of the rainfall profiles. In the following articles, we’ll introduce spatial rainfall sources.

![](images\1_n6fPZ1SLdHk7IiIUJ73bHw.png)

Create a TVD connector near the sub1 subcatchment, the location doesn’t matter, just for easy access of the connector through the GeoPlan.

![](images\1_Wxb8st1Tlshhb7VVOWmbWg.png)

1. Drag the “from\_csv” TSDB to the GeoPlan (should see the target (1) in the title bar)
2. Double click on the rg1 TVD connector and populate the information.

Do the same for rg2.

![](images\1_-76sDxGIbaXde0BREwgmPQ.png)

Compare the TSDB values and the simulated values to make sure the rainfall are correctly added.

![](images\1_qvQgrqSCKx98yxeoDhykEA.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 12, 2021](https://medium.com/p/7fabfdc427d4).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-add-rainfall-to-icm-using-tsdb-part-2-7fabfdc427d4)

Exported from [Medium](https://medium.com) on March 18, 2025.