# How does date and time work in XPSWMM

source: Innovyze Support Portal

---

### How does date and time work in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-does-date-and-time-work-in-XPSWMM)

For most of the XPSWMM models, we are assuming a model will run with a design storm starting from midnight. And that works pretty well most of the time.

However, from time to time we need to run models with historical rainfall data, or we would like to run a design storm that starts at a different time of the day.

In such situations, things can get complicated, and we need to have a deeper understanding how XPSWMM defines date and time for the input time series, and simulation start and end time.

Here a quick summary,  
\* rainfall/user inflow time series are entered using hours instead of date time, therefore, the meaning of 0 can mean different things depending on the settings.  
\* For rainfall, you need to specify how 0 is defined, the start of the simulation or a date defined in the rainfall profile  
\* For user inflow, it is always the midnight of the first day of the simulation, so if you’ll need your inflow to happen on the 2nd day, enter 0 for the first 24hrs

### Rainfall Date Time

By default, rainfall start time is defined by the starting time of the simulation.

(5) is checked by default to force the rainfall to start at the same date and time as the simulation.

![](images\1_JtOirvJNOkacnFrHIkXo6w.png)

And with (5) checked, the starting date time of the rainfall is disabled.

![](images\1_RbrkPUzWYBKwb_SUarWVWA.png)

If (5) is unchecked, then you can specify the starting time of the rainfall.

![](images\1_A4YHiOswU19Xuai-9txLVA.png)

When the rainfall data is entered, the Time is counted from the starting date and time, NOT midnight.

![](images\1_EKu8joPBs5IdJMJZ9zJNdw.png)

As shown below, when a constant 1in/hr rainfall is loaded,

(1): use the start from simulation start time

(4): an one hour constant rainfall from the start of the simulation

![](images\1_ZoLtLsVYb3pXFO1AKERF8g.png)

By adjusting the starting time of the simulation, we can move the rainfall.

* midnight\_sim\_start: the simulation started at midnight
* 5am\_sim\_start: the simulation started at 5am

![](images\1_oTTs2Ew8kFIARg7q4V1KxQ.png)

If we don’t use the simulation start time, the start time can be changed in the rainfall profile,

![](images\1_yCj4jUAW9XeY3STLjQdCMg.png)

And the results of starting the rainfall at 1am, 4am is shown below,

![](images\1_FsJZo3d8BYgXnOjVlcIWIQ.png)

### User Input Hydrograph

For the user input hydrograph into a node, **it is always assumed time 0 is midnight**, and the starting date is the same as the simulation start date regardless of the hour and minutes.

A pulse of flow was loaded at 11am into Node1.

![](images\1_kzz21GcYU8mPPA1bAXbnFw.png)

We changed the start time from 0 to 5am,

![](images\1_uMJt1ldojlPjSXhjFJyPIQ.png)

And the results look exactly the same because user inflow always starts from midnight regardless of the time the simulation starts.

![](images\1_QDYvJ8jABaUwyTzBE9clYw.png)

### Runoff date time vs Hydrology date time

Probably the most complicated aspect of XPSWMM is getting the RNF and HDR model to work together.

In most cases, you should use the run simultaneously [option](https://mel-meng-pe.medium.com/how-to-run-hydraulics-and-runoff-simultaneously-in-xpswmm-b1ca20870b89). That will make the RNF/HDR essentially one seamless model. It is good practice to ensure the simulation start/end time are entered the same in both modes.

As shown below, the rainfall starts at midnight for one hour. If we start the RNF at 3am, then there will be no flow in the model as shown below, even though for the HDR, we started at midnight.

![](images\1_vcWvlUnyG1rqXymGFyaXow.png)

### Use different date time for RNF & HDR

Sometimes you might want to run the hydrology and hydraulics with different time. For example, you just need to route the flow for the second storm but you do need the hydrology to run for the infiltration for both storms.

As shown below,

* back\_to\_back\_2nd: only simulated the storm after 12PM

![](images\1_yx8zE3WSd9Yl-fmXEqp7Qw.png)

This is achieved by adjusting the start time for the scenario to 12pm. Switching to the RNF model, we can see hydrology was run for the full duration for both storms

![](images\1_Dm3U3q3QN90dnF7Kc--ZLg.png)

A more practical approach would be using the interface file, the way how SWMM worked in the very early days when computer doesn’t have enough power to run the simulation simultaneously. This still can be relevant today for continuous simulations that can take a very long time to run.

By decoupling the RNF and HDR, we can treat the RNF results just as another input source, and run only for the periods we are interested. This can be very appealing for continuous simulation. To run a hydraulic model for a few months can take a long time and the results can become very big. If all we are interested are the few big events, then we can run the RNF for the whole duration, and only run HDR for the few big events.

A continuous RNF run is needed because processes such as infiltration will require simulating the precedent condition long before the event of interest.

To use an interface file,

![](images\1_l2bUtigHfIk5KWufY90WBg.png)

1. we recommend to use relative path, it will make it easier when transferring the model
2. give it a name to save the runoff results into the interface file
3. make sure the same file is referenced for HDR to read the runoff

![](images\1_vB4WJd4jMsnfvTkCuZbJQQ.png)

Make sure (2) is unchecked, so that we’ll only read the interface file.

![](images\1_a_wR_P-2XziPwQm_bsvxaw.png)

We should run the RNF and HDR separately,

![](images\1_NWEzglxnW9yhbZTj7v4t3g.png)![](images\1_xGmtyAjt783MZ2FesMhUVg.png)

Next, we switch to RNF and run the model to generate the runoff and save it in “data.int”.

After that, we can switch to HDR model and run the model only for the events we are interested.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 28, 2021](https://medium.com/p/b1584f473c09).

[Canonical link](https://medium.com/@mel-meng-pe/how-does-date-and-time-work-in-xpswmm-b1584f473c09)

Exported from [Medium](https://medium.com) on March 18, 2025.