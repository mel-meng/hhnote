# How to compare NEXRAD with rain gauge data in ICM? — Part 1

---

### How to compare NEXRAD with rain gauge data in ICM? — Part 1

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-compare-NEXRAD-with-rain-gauge-data-in-ICM-Part-1)

When using NEXRAD data, the first thing you might want to check is to compare NEXRAD rainfall to your rain gauge data.

In a series of mini tutorials, we will go over several common methods to bring rainfall data into a model using TSDB (time series database), and then compare the rainfall from different sources.

ICM supports both spatial rainfall and simple rainfall time series. When using the rainfall time series, the rainfall data is referenced in the “rainfall profile” field of a subcatchment. It can be a number or a text that matches the rainfall profile name defined in a rainfall object or a TVD connector.

![](images\1_Ydci0dQHbINPoox9Ns7IWw.png)

ICM also supports spatial rainfall, the rainfall for each subcatchment is calculated based on how close it is to the rain gauges around it. And it will be covered in part 2.

### Using Rainfall Profile

The easiest way to get rainfall into the model using TSDB is using the rainfall profile,

* create a scalar TSDB with rainfall data
* create a TVD connector to bring the rainfall into the model
* assign the TVD connector name as the rainfall profile
* run the model with the TSDB

### Create rainfall TSDB

First we need to prepare the input data. For quick prototyping and testing, we are using the csv format. According to the help file, we need to convert the time stamp to “dd/mm/yyyy hh:nn” format,

![](images\1_P-UB5diYEhafEOFs6KMEsw.png)

It can be easily done in excel,

![](images\1_PCW5AW6OPu_Zg3SMvI8qAA.png)

Next we set up the TSDB,

1. Create a new scalar TSDB

![](images\1_Inm4oIMmK84Sa1iwnKWEGw.png)

2. set the data source

![](images\1__I7aDVk_m59rAli0F1VoWw.png)

3. set the folder where the csv files will be stored, and set the time zone for the time used.

![](images\1_Eqm2Is3FKbsoY3NLlrkLEQ.png)

**NOTE:** ICM TSDB doesn’t honor daylight saving time, therefore for US customers, in the summer the time is off by one hour when the local time zone is selected.

Next we set the observed stream tab,

1. Give each rain gauge a name
2. ICM can only use rainfall intensity for simulation, set the units to intensity
3. Review you data for the interval, we have 5 min data, so use 300 sec
4. And the source is the CSV we just created in the data source tab

![](images\1_iNLW1G0AqORIn2GSkvI9Kw.png)

Here are some complications of the data,

* the data is total rainfall for every 5 min instead of intensity, so we need a factor of 12 to convert it to in/5min to in/hr
* ICM TSDB doesn’t honor daylight saving time, and in the data it is the local data, so during the summer we need to move the time 1hr backward, that is -3600 sec

The last step we select the table that stores the rainfall data for each rain gauge.

![](images\1_dt4yekWzHMd4oLu1oZOm-A.png)

To load data into the TSDB,

![](images\1_1RVQkF6Dsk9YO-IXzy_mnw.png)

**TIP:** If you found some error in your source data, if you haven’t run a model, you can delete all the data imported.

![](images\1_NgyrQ7diGNDlKNyJqcwWEg.png)![](images\1_9ziK8BwImXdR4EpMggtkgQ.png)![](images\1_oKb1FNeHcGIPdosqfJVSEQ.png)

If the data is already used by a simulation, then you cannot delete. In this case you have to manually update the data by specifying the range to be replaced.

![](images\1_fQq-Nen7GnfvL5FT71Vogg.png)

Pick the data range the data needs to be updated.

![](images\1_qIb6nLatRSbw2GOq4IZRPA.png)

### Create the network

It is much easier to create a dummy model to test the rainfall than converting your existing model.

First, make sure the projection of your system is correct since we are going to use NEXRAD which has to match the model’s coordinate system

Open your existing model, set the correct coordinate system

![](images\1_Cyyvhpm4tX4FQCSmlplXtA.png)![](images\1_B6x9cp95Q3Ai45MkkuXpPQ.png)

To check if the projection is correct, verify the location in Google Maps.

![](images\1_Bzzf9TSZo0eHXNPFgyPP1Q.png)

You can copy a few subcatchments and pipes from your existing model, and paste them into a new model to build a very simple model, making sure you set the same coordinate system.

![](images\1_pi1t5Cxvm4Vqg-BYHS-6sQ.png)

### Add rain gauges as TVD connectors

To test the rain gauge data, we’ll need to create TVD connectors.

Drag the TSDB into the Geoplan so that the TVD connector can recognize the streams

![](images\1_e_y-dgQ2E1GeNDMjJmAJ5w.png)

Create TVD connector at the location of the rain gauge

![](images\1_K9otkj2mj7Z8ImizRP-nDA.png)![](images\1_iBpNvHuczvwWJ0OjufeJMg.png)

Name the TVD as the rain gauge name, and set the correct units and stream name, the “#” indicates it is from the TSDB.

![](images\1_5SzuSRJLs0m9uei4obqnXQ.png)

Update the rainfall profile for subcatchments,

![](images\1_LytZuf6bBPrNbpYKSP2wIA.png)

### Run simulation with rainfall as profiles

Setup the run,

1. drag the TSDB into the run
2. use the latest version of the database
3. set the correct time zone for the results
4. make sure all the streams are showing
5. review your rainfall data and pick a period with good data

![](images\1_eo9GfoQDQJhUOdUjxASVDA.png)

we can compare the results from the two subcatchments using two streams from the TSDB.

![](images\1_RbCHbyDSqqQaJQ2OXSElLw.png)

### Create the NEXRAD TSDB

Refer to this [article](https://mel-meng-pe.medium.com/how-to-download-archived-nexrad-rainfall-data-into-a13e2653fa46) for more information on how to create a TSDB with NEXRAD data. Here is the configuration for this tutorial.

![](images\1_FBoJDi0RE1s7toZEo1GNGg.png)

Drag the NEXRAD TSDB into the Geoplan, move the cursor up and down through the rows to play the radar rainfall animation,

![](images\1_mEWoRvw7_Rw2RFJrpepo8A.png)

If you don’t see the rainfall showing,

![](images\1_mppX9x2qJY3r8zhsUaG5DQ.png)![](images\1_w0nhVlEiQDhx5xuDGMSd3Q.png)

If you still don’t see the results, you might have the wrong projection or cropped the wrong extent.

### Run the model with NEXRAD

To run a model with NEXRAD rainfall, all you need is to drag NEXRAD into the run.

![](images\1_GtnPbfLn-x1J_Kjjnx8AwA.png)

Since we don’t want to use rain gauge data in this run, we need to delete the TVD connectors, and that is the “no\_rainfall\_profile” scenario.

### Comparing the results

To compare the results, we’ll use a custom report.

First we need to select all the subcatchments to be compared and create a selection list.

![](images\1_76ItIASUJc6G-o1Xpz2LOw.png)

Next, we create a custom report.

![](images\1_jpxApCob67yD_62e9aX6Dw.png)![](images\1_5dtujQ34ZfN2zmdjS56YYg.png)

For easier graphing, we change the name of the simulation results to be more meaningful

![](images\1_a3177VUv3wT3fpFU751-aQ.png)![](images\1_DUm3QTvkIaiWkMWzkpIXgw.png)![](images\1_Oi-o2Ddk0Umr2HdfSQ4DXg.png)

Now we can compare the results.

![](images\1_3vF9rmcEW6LzOgH4Oalerw.png)

The example model can be downloaded from [github](https://mel-meng-pe.medium.com/how-to-compare-nexrad-with-rain-gauge-data-in-icm-part-1-605c63437b94).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 21, 2021](https://medium.com/p/605c63437b94).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-compare-nexrad-with-rain-gauge-data-in-icm-part-1-605c63437b94)

Exported from [Medium](https://medium.com) on March 18, 2025.