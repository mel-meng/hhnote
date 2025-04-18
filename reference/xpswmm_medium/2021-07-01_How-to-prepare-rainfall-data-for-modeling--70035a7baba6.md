# How to prepare rainfall data for modeling?

source: Innovyze support portal

---

### How to prepare rainfall data for modeling?

source: [Innovyze support portal](https://innovyze.force.com/support/s/article/How-to-prepare-rainfall-data-for-modeling)

A common task for modeling is preparing rainfall data, and it could be complicated. In this example, we will learn a few tips of managing rainfall data.

Most common rainfall data are recorded from rain gauges, which is reported as totals for each time interval. For [tipping bucket rain gauges](https://www.reddit.com/r/meteorology/comments/hmd4md/tipping_bucket_rain_gauge/), a very clever mechanical device, it counts the number of bucket tipping, since each time it tips, it is a fixed volume, the total rainfall can be calculated.

![](images\1_4VR4x_so5ZpDSQgHI-sn8A.png)

If the rain gauge reports the rainfall every 15 minutes, the data will look something like this.

![](images\1_h_hAlTE8f_iPberhwFOLLg.png)

### Rainfall Units

Now, the first thing we need to do is rainfall unit conversion. Depending on the program you will use, it could ask you either intensity or total volume.

If it is intensity, it will be inch/hr or mm/hr. In our example above, the intensity will be calculated as total (volume/time interval). So for 1 in rain collected in 15 min, it will be 4 in/hr (1 in/0.25hr).

This might take some testing with your software package if it doesn’t provide obvious clues of the units to be used.

A simple way to check is comparing the total rainfall from the modeling output with your source data.

### Date Time formats

Date time formats conversion can be more challenging. There are so many date formats,

* Jan 1 2020, 11:20am
* 2020, 1, 1, 11, 20
* 11/20/2020, 11:20
* 11/20/2020 11:20
* etc

Another thing to look out for is the time interval, most modeling package requires fixed interval time series data, and we might need to clean up the data first.

For date time format, Excel has excellent functions for the task.

As shown below, the common tasks are,

* combine date time from multiple columns into one column
* separate date time from one column to multiple columns

![](images\1_3I-CrH7r8dND5lN0zHebjw.png)

As shown below, excel treat date time as numbers,

![](images\1_hFSe3nAmIpJI7QlRb2ZcoA.png)![](images\1_uD9C-BkTcvcvnM-B7_HtJg.png)

So to combine date and time into a single column is as simple as adding them together

![](images\1_lY-uqFqEBZCyP1GmA85ZLQ.png)

Then choose the right style,

![](images\1_qUD9qoHy_6NzXOgHMBlbCQ.png)

Now we have date time in a single column, how to get a single date time into multiple columns? we can use the TEXT function to format a datetime number,

![](images\1_iKheTywb8sPd_d0hAwHx2Q.png)![](images\1_ifoEFOauuUPbeu62ADzAQQ.png)

Next, let’s see how we can enforce a fixed time interval for rainfall time series.

First we need to verify the time interval by calculating the delta between two time steps,

![](images\1_K5w_oOBJte6lTEa-qM9d9w.png)

Then we can use the filter to see how many different time interval we have, and if we have multiple intervals, we can go ahead and fix these irregular time intervals.

![](images\1_NAUWnsJzeqF1D7zjSP2OnQ.png)

For rain gauges without a synchronized clock, usually the time stamp is just off by a few minutes, and if it is 15 min interval, we can simply move the time to align with the closest reading, which should give us pretty good data.

For this, we can build a spreadsheet with manually populated time stamps at fixed intervals, then “calculate” the value from the source data.

1. we need to build a time index with fixed interval. Start the first two rows, then drag it. Be careful, sometimes Excel might get the calculation wrong, make sure you review the intervals using the method above and fix any errors.

![](images\1_6NA1KzoxBd3SD5Uo7t2x-A.png)

2. Then we can use the **vlookup** function to grab the data closest to the time interval. Make sure the last parameter of the vlookup is “True” so that it will look for the closest time in the red area rather than an exact match.

![](images\1_zywR6jh1gZ4Cf2gyUyC9Zg.png)

### An XPSWMM Example

With the above tips, you can turn most raw rainfall data into any format a modeling program asks for.

Here is an example adding rainfall data to XPSWMM as a user defined file.

First let’s create a rainfall entry for RG01

![](images\1_peqFDAKjZUPkVbwEt98-eQ.png)![](images\1_MUztNbzIfHwvaBRl_sgPtQ.png)

For the File Format, it should look like this.

![](images\1_8Pcec8thWnzR9DkBQdqqoQ.png)

And that is the format we are going to build.

![](images\1_1Wq9rkon27CGIpf1E33KaA.png)![](images\1_yZWSknjc3CuF_JQfdHWbEQ.png)

Column C should be total instead of intensity in inches

Column D is needed, and it is the station name.

![](images\1_3MaI0W26W81IGvOTfctaMQ.png)

With this setting, we have the results shown below,

the rainfall is,

* 4 in/hr for the 1st hour (1in/15min=4in/hr)
* 8in/hr for the 2nd hour.

![](images\1_OPERpOkjF1bIrG5uiwhsSw.png)

You can find the model and excel example on [github](https://github.com/mel-meng/xpswmm/tree/master/models/rainfall/user_defined_rainfall).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [July 1, 2021](https://medium.com/p/70035a7baba6).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-prepare-rainfall-data-for-modeling-70035a7baba6)

Exported from [Medium](https://medium.com) on March 18, 2025.