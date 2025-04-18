# Working with multiple Spatial Rainfall Sources in ICM

source: Innovyze Support Portal

---

### Working with multiple Spatial Rainfall Sources in ICM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Working-with-multiple-Spatial-Rainfall-Sources-in-ICM)

When running a real-time live model, there is a need to collate the rainfall from multiple rainfall sources to get the best rainfall data.

A typical situation in the United States is using the rain gauges installed in the study area when data are available, and then using the radar rainfall (NEXRAD) when needed, and for forecasting use HRRR from NOAA.

Since we don’t have the time to review the rainfall data manually every time a real-time model is running, ICM has built-in functions to help identify data gaps, and then apply rules on how to choose the best data source when data are missing.

### Identify missing and bad data

For rain gauge data stored in a scalar TSDB(time series database),

* missing data are identified based on the time interval
* bad data are identified based on the threshold definition in the data stream

![](images\1_ZIR_BEQ_2pvRUOT4JQXUfA.png)![](images\1_GVxQLNpiG0lHuaDWPjmA5Q.png)

As shown below, when we deleted two rows in the time series, the data are shown as missing in the plot with missing triangles data points. Also with the extend option, each data pointed is showing as a step.

![](images\1_RFRrYnQ28dzf0aVuydGZIQ.png)

### Setting logic rules on which rainfall sources to use

The logic rules are defined in the “Spatial rain source” tab of the “New Polygons Window” grid.

When ICM calculates the rainfall for each subcatchment it will start with the high priority source (with the lower priority number). Then it will process the data point one by one, if there is missing data, it will look for the data from the next priority source.

We can also restrict the range of the rainfall data using the start/end seconds relative to origin. With this setting once the rainfall is out of the range, ICM will move to the next source for rainfall data.

![](images\1_oO2gMJJe9XloSIws9xGw-Q.png)

### Example Model

In our example, we have 3 sources of rainfall data,

* Rain Gauge (15 min)
* NEXRAD: radar rainfall (~10min)
* HRRR: rainfall forecast (hourly forecast)

The model network is shown below,

* a simple network with two subcatchments
* one spatial rain gauge polygon
* NEXRAD/HRRR were used as additional spatial rainfall sources

![](images\1_9Gr2CN1k8xxiEVZs0Rj1bQ.png)

As shown below, the rainfall sources look quite different.

* from 12/17 12:00: NEXRAD recorded more rainfall
* from 12/18 18:00: the rain gauge and HRRR recorded more rainfall

![](images\1_iYVkzZYd-c_gqwz6gnWcFg.png)

We’ll do a few experiments and learn how ICM chooses rainfall data.

As shown below, if we only change the priority order, then the source with the lowest priority number will be used as the rainfall source.

This one below will use the Rain gauge

![](images\1_8QRwxWqxVr8wDDu_0olvQw.png)

This one below will use HRRR.

![](images\1_I84FidFNmROvW7Fy2s-wow.png)

What if we change the settings of the start/end relative to the origin,

In the setting below,

* The origin is 12/18 12:00

![](images\1_jmnoVr8OgZzYh2RKAz-jjg.png)

The results are shown below,

* the green line is the rain gauge data
* the blue line is ICM calculated rainfall
* (1) is the run origin
* (2) priority 0 is RG\_NET, and it is from start to -24hr (86400 second). In this region, rain gauge data was used
* (3) in this region, it is outside of RG\_NET range, so NEXRAD data was used
* (4) in the region, HRRR data was used, and the rain gauge data were ignored.

![](images\1_lIshLTiqruentYJYOHPb2A.png)

Next we’ll see what will happen when data are missing,

We manually deleted a few rows of data from the rain gauge database. And ICM will replace the missing data with the next priority source

![](images\1_sYBDNvDMn8PWafUZHXCw0Q.png)![](images\1_IvHjvujE5_MWYB_wPx6j5Q.png)

With the following spatial rainfall source settings,

* Before the origin, the missing data will be replaced with NEXRAD, the next priority
* and after the origin, the missing data will be replace with HRRR, NEXRAD will stop at origin, so the will move to the second priority source.

![](images\1_NURFoJQZLEPpFTXm1WENBw.png)![](images\1_fnQgMq37Bv3gbFLiXpZ4iQ.png)

The model can be found on [github](https://github.com/mel-meng/icm/blob/master/models/rainfall_tsdb/spatail_rainfall_sources.icmt).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 25, 2021](https://medium.com/p/b226814c9a5e).

[Canonical link](https://medium.com/@mel-meng-pe/working-with-multiple-spatial-rainfall-sources-in-icm-b226814c9a5e)

Exported from [Medium](https://medium.com) on March 18, 2025.