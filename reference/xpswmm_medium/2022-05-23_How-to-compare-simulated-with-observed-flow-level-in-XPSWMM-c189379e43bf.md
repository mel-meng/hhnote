# How to compare simulated with observed flow/level in XPSWMM

source: Innovyze Support Portal

---

### How to compare simulated with observed flow/level in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-compare-simulated-with-observed-flow-level-in-XPSWMM)

When you are calibrating a model, showing the simulated and observed flow and level in the same plot can be quite useful. This can be easily done in XPSWMM.

![](images\1_kJcvZJNRRnF9chymKjqnbg.png)

As shown above, for a link, just tell XPSWMM to plot the the flow from another file.

![](images\1_UaWcJ290_lFxwZm2D4Ni6g.png)

### Prepare the observed flow data

A typical flow data file is a csv file with the following fields,

![](images\1_1VMxmW-S4fsrdbXR6bf3EA.png)

For the format, we need to refer to the XPSWMM settings.

![](images\1_sOFiysKxqDheDZRiAlSGHw.png)

3: the first row in the csv file is a header

4: we’ll use the free format to let CSV define the time step

5: here we define the format for each column

* STATION: this is a text field, we can have more than one flow meter data saved in this column, and this column define the meter name
* Date: use the mm/dd/yyyy format
* Time: using the hh/mm format
* Flow: that is the value to be compared to the results

A few tips on setting up the date time format in excel.

* generate time series, enter the first two time stamps, then just drag the cells to get fixed time interval time stamps series

![](images\1_cE88jJhgdpiMdSoCZVwZMg.png)

* make two copies of the time stamp columns, one for date, another for time
* use the custom format to get date/time formatted

![](images\1_58LmYreSDhsg2zTokO9FdQ.png)![](images\1_B27tpMK1PaeIxX5TAAJcqQ.png)

* Save the file as csv file in Excel

![](images\1_2rx-xUfIDHqwqn6EQKk4DQ.png)

### Link to the csv file in XPSWMM

In XPSWMM,

1. select the csv file
2. show the list of the stations
3. select the one for the pipe
4. check all dates, and user defined, select the format defined for the csv file

![](images\1_eR34sKGUi3tSJIoVhDqeQA.png)

5. click edit to review or edit the csv file directly

![](images\1_-_JCOXw4Ia59CO-RxNuEKg.png)

**NOTE: If you have trouble editing the csv file. The most likely cause is the wrong encoding of the csv file. Use text editor such as Notepad++ to convert the encoding to ANSI**

![](images\1_kvv6AK85mgXmiEDKM4Rmxw.png)

For more information on using the standard format, refer to this [article](https://mel-meng-pe.medium.com/preparing-time-series-data-in-old-fixed-width-format-with-python-5a1d10dca376).

![](images\1_Ml4pl38_YwpJoGC-RqRQ5g.png)

The model can be downloaded from [github](https://github.com/mel-meng/xpswmm/tree/master/models/gauged_flow).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 23, 2022](https://medium.com/p/c189379e43bf).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-compare-simulated-with-observed-flow-level-in-xpswmm-c189379e43bf)

Exported from [Medium](https://medium.com) on March 18, 2025.