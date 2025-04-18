# How to use rainfall interface file in XPSWMM

source: Innovyze Support Portal

---

### How to use rainfall interface file in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-use-rainfall-interface-file-in-XPSWMM)

When running very long simulations in XPSWMM, you might find an rainfall interface file. A rainfall interface file is a quite old type of data format for rainfall, developed in the early days of SWMM. The main benefits of an rainfall interface file is that it can pack a lot of data in a very small file. It a binary file with only the rainfall data when it rained.

The downside of a rainfall interface file is that you cannot read the rainfall data directly, and you can not have any other type of rainfall data in a model if a rainfall interface file is used.

We’ll cover the following topics in this article,

* How to use a rainfall interface file in the model
* How to convert a rainfall interface file to user input rainfall

### Use a rainfall interface file

To use a rainfall interface file,

* reference the \*.rin file
* create a rainfall global data entry

![](images\1_YyGKRkP-XXtZHL0RDEsDlg.png)![](images\1_dcu480l598NCr3FvQNp9iQ.png)![](images\1_xK6XQlv3kZXxKPwybgiH3g.png)![](images\1_Og90BJd8O2_zoNviT1V3NQ.png)

After that, you can reference the rainfall in your subcatchment.

![](images\1_FTlTNiAR1Wkwss46z5Jabg.png)

### Convert a rainfall interface file

In some situations, you might want to use multiple sources of rainfall data or you only need a portion of the rainfall from the interface file.

* extract the time series from rainfall interface file
* create a global rainfall item using variable time step

Launch the InterfaceUtils.exe,

![](images\1_BN5fFgNQ5nwoRzFaCTAhsw.png)![](images\1_ltITzCVDi3sagwTkG9zqfQ.png)

This will create the csv file for rain gauge station 128187. As shown below, only the non-zero rainfall values are reported, and each row has its date, time and the time step duration and the rainfall intensity (in/hr)

![](images\1_eLjX4F74dsIUNv54qdwSqg.png)

To convert the table to a rainfall record in XPSWMM,

![](images\1_pcP0Z62vFEHLbBVaN1z2sw.png)

We’ll get into the details how to convert the time intervals below,

time interval is the time from the start in minutes

* start date is 1/1/1992 (1992001), (1992002–1992001)\*60\*24 is the minutes from 1/1/1992 to 1/2/1992 (1992002)
* 39600/60 is the minutes since the start of the day
* and the total is the minutes since 1/1/1992 in minutes for the time step

duration is the time step length, it is 60 min for all the time step

rainfall is the intensity, the same as the interface file export

![](images\1_uejVCLBYeMwRy6hkRhtNCA.png)

You can find the example on [GitHub](https://github.com/mel-meng/xpswmm/tree/master/models/rainfall_interface).

Base uses the RIN file, and converted scenario used the converted results.

![](images\1_iaNfhOAVb1WjH-musmWJ3g.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 27, 2021](https://medium.com/p/c9423b8dc446).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-use-rainfall-interface-file-in-xpswmm-c9423b8dc446)

Exported from [Medium](https://medium.com) on March 18, 2025.