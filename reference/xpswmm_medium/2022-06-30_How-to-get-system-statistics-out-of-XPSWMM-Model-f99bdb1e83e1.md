# How to get system statistics out of XPSWMM Model

source: Innovyze Support Portal

---

### How to get system statistics out of XPSWMM Model

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-get-system-statistics-out-of-XPSWMM-Model)

XPSWMM generates lots of system statistics such as total inflow and outflow of a node, peak flows through pipes.

Many of the statistics cannot be easily accessed through the user interface, and it will require a little bit extra work to get them.

### Interpolation vs Computed

It is important to understand the the differences between the computed and interpolated values.

As shown in the figure below (credit: SWMM5 hydrology reference manual), the circles are the values computed by the engine, in general, it is reported at each simulation timestep (Trout: routing timestep, some of the engine will half the timestep if the error doesn’t converge, therefore, the timestep might not be fixed). Since exporting all the computed timestep can be an overkill for most applications, time series for flow and depth are usually reported at bigger time intervals, which is interpolated from the computed values as shown in squares, it is just a simple linear interpolation between the two closest computed values.

![](images\1_5XrYRLQc-OwCEtWsgyCIjw.png)

For example, you might compute every 1 second but choose to report every 5 minutes.

#### The implication is system statistics can only be accurately calculated by the engine.

For example, the peak value is calculated by updating the max value at every time step. You can calculated the peak flow from the reported time series, however, you might miss the true peak if it happened between the two reporting timestamps.

For a collection system, ideally we would like to see flow and depth changes gradually, and as a result, statistics calculated using a reporting interval of 5 min should give very similar results as the system reported statistics using all the computed values. Therefore, it is always a good idea to compare the reported peak with system computed peak.

![](images\1_iCPxuLGcE3CylpDn4T05mA.png)

### System Statistics

The best place to find system statistics is the 1D log.

![](images\1_zI2fiQlYM_mWa82kV5Vk5Q.png)

For hydrology information, refer to the RUNOFF Tables

![](images\1_Pt0LZitGbYG0YzvWePwjxg.png)

For hydraulics information, refer to the Hydraulics tables,

![](images\1_2l0KYygZ7_4UhIONHma9yg.png)

For example, we would like to get the summary of total inflow and outflow through the outfall nodes. Then we go to Table E19. As shown below, to get the total volume of the flow through this simple model is not easy manually. We will have to calculate it from the reported time series and input data. Since the inflow/outflow time series of a node is not reported, we don’t have too much from the results to calculate the inflow to a node. But if we check table E19, it is all there.

![](images\1_l_mRrDH97twY16GFlST2Qg.png)

One problem with the 1D log is that it is not that easy to extract that information, a better way is to use the XPTables to extract the information automatically from the results.

### System Statistics XPTables

First open the XP Table tab,

![](images\1_HTHQt03-HBnwYaa376IUUw.png)

Next, we create a table to report the volume for nodes.

![](images\1_9ctEqwjHzrPSzGDh9mIs5Q.png)

It will take some time to figure out which variable is the one in the Table E16, but you only need to do this once.

1. edit the variable of the table
2. find the inflow/outflow volume folder
3. drag the folder to the box on the right side

![](images\1__NYHmJjT9G1Y-RtGE6fYUg.png)

Now we have most of the values populated in this XPTable,

![](images\1_w3UeZOW-_txbllK9OAeXZg.png)

### Use the default template

Most of the system statistics and summaries are built into the default template. Using one of these templates probably will be easier than rolling out your own.

If you are starting a new project, choose “Use Default Template”,

![](images\1_YFih8elA36c3cynvMA9--w.png)![](images\1_6Qae859OOP6b_Bpm--7Okg.png)

You can see a long list of the XPTables. You can hide the ones that you are not interested by unchecking these tables.

![](images\1_WIv1YlgT5jwlvVDp4Izikw.png)

#### Import only the XPTables into an existing model

If you are already in the middle of a project, you can merge the XPTables from another model.

For example, you can create an empty model using the default template, then merge it into your existing model.

![](images\1_Us3TutnDlV_jKta1hcBv8A.png)

Only check the global Databases, this will import XPTables, and other records such as rainfall from the other model.

![](images\1_VtSyUvdJNDNvT3mLYmrtGg.png)

You can find more templates from the [online resources page](https://help.innovyze.com/display/xps/Resource+Downloads).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 30, 2022](https://medium.com/p/f99bdb1e83e1).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-get-system-statistics-out-of-xpswmm-model-f99bdb1e83e1)

Exported from [Medium](https://medium.com) on March 18, 2025.