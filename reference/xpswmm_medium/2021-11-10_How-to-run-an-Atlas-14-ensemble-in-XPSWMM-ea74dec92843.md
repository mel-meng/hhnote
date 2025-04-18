# How to run an Atlas 14 ensemble in XPSWMM

In my previous posts we discussed why do you need ensemble Analysis and what are the NOAA Atlas 14 Precipitation Depth and Temporal…

---

### How to run an Atlas 14 ensemble in XPSWMM

In my previous posts we discussed [why do you need ensemble Analysis](https://mel-meng-pe.medium.com/why-do-you-need-ensemble-analysis-cba0ee0a22a3?source=your_stories_page----------------------------------------) and what are the [NOAA Atlas 14 Precipitation Depth and Temporal Distribution](https://mel-meng-pe.medium.com/noaa-atlas-14-precipitation-depth-and-temporal-distribution-7d7c26690d68?source=your_stories_page----------------------------------------). In this article we’ll go over an example of setting up an ensemble model in XPSWMM in San Marcos, TX, USA.

### Getting the data

You can find all the data from the [NOAA Atlas 14 website](https://hdsc.nws.noaa.gov/hdsc/pfds/pfds_map_cont.html), enter the address or coordinates to go to the project area.

![](images\0_4FCh38D7w30bPsLg)

### PF Estimates

The rainfall totals for different durations and frequency are listed in the PF Tabular tab.

![](images\0_DbSjYh2xUFtUNrbU)

It can be downloaded as a csv file.

![](images\0_qcGzAlwwS4h8_7zW)

### Temporal Distribution

For this location, there are 4 temporal distributions (6, 12, 24, 96hr) downloads. They can be also be downloaded as csv files.

![](images\0_BhCRZN_Pg4ncEeIV)

To learn more about the correct temporal distribution, visit the [temporal distribution page](https://hdsc.nws.noaa.gov/hdsc/pfds/pfds_temporal.html). As shown below, the rainfall profiles for Texas is provided in Volume 11, and the state is divided into 3 regions, and the temporal distribution are specific to each region.

![](images\0_XVjMnGT8QYyB7k-F)

### XPSWMM Resources

For commonly used rainfall profiles, you can find the temporal distributions converted to XPSWMM xpx format from the XPSWMM [online help](https://help.innovyze.com/display/xps/Resource+Downloads).

From the NOAA website, we know we’ll need the temporal distribution for Atlas 14 volume 11, region 2.

![](images\1_zyOTTCoXZJZMlCI_3665LQ.png)

Download the zip file, and unzip it. For each quantile, and duration there is an XPX file.

![](images\1_l1m9XZN4NLCVwyJqoUD58w.png)

For each xpx file, it contains the percent of occurrence from 10% to 90% probability.

![](images\1_MqGmSscvgdBbNMKtpFoRKg.png)

An example for the percent of occurrence is shown below. The x-axis is the duration, and the y-axis is the cumulative precipitation. For example, when x=20%, for the 10% curve, it almost has 100% of the precipitation accumulated, and for the 90%, it only rained about 5%. These curves were developed based on real-storm events so that as shown in the graph on the right, for the 10% curve, 10% of the events are in the red area, and 90% of the events are in the green area. Roughly speaking, the lower the percentage, the more intense the storm at the beginning of the event.

![](images\1_OGoLlj5ulVmgE0spwkWNbA.png)

The profile name is organized as,

AT14-V11–1Q-10P-6Hr

* AT14: Atlas 14
* V11: volume 11
* 1Q: first quantile, the majority of the rainfall is in 1st quantile
* 10P: the 10% of the occurrence temporal distribution
* 6hr: the duration of the storm

To import the temporal distribution into XPSWMM

* Import XPX file

![](images\1_y1LMcPTYISSE3cWVr2BHgA.png)![](images\1_0DRsqL9ZvXerBYoFyOzwfg.png)

* Review the rainfall profile in global data

![](images\1_jPPdU1_b8EvUplpYnt8Pqg.png)![](images\1_PW8ArV3HqzYjHHIFgIsEVw.png)

### Global Storm and Ensemble

With global storm, we can run the same model with different rainfall profiles. By assigning an ensemble name, we can calculate ensemble statistics within XPSWMM for each ensemble.

To create global storm,

* switch to runoff mode
* go to job control
* go to global storms
* create ensemble names
* build a list of global storm
* (6) is the temporal distribution imported from xpx file
* (7)(8) we get the PF frequency rainfall from the NOAA website and apply that to the temporal distribution
* (9) for each ensemble, XPSWMM will calculate the statistics

![](images\1_rmK_l6LbNlqeJ4eRIi4Cdg.png)

Use the solve manager to run the simulation in parallel.

![](images\1_VOhNgvvRZUgXcpl5HGBGZA.png)

Once it is completed, to show the ensemble statistics,

![](images\1_yft2w5O4KH3tRwVjpnJWrQ.png)![](images\1_dNYbBqXTsevqo2htrUj_pA.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [November 10, 2021](https://medium.com/p/ea74dec92843).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-run-an-atlas-14-ensemble-in-xpswmm-ea74dec92843)

Exported from [Medium](https://medium.com) on March 18, 2025.