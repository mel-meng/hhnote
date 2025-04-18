# How to calibrate a Live Model?

When I started live modeling about a year ago, I thought live modeling is nothing but automated modeling, once I get myself familiar with…

---

### How to calibrate a Live Model?

When I started live modeling about a year ago, I thought live modeling is nothing but automated modeling, once I get myself familiar with the IT aspect of things, I should be good to go.

It turned to be a lot more exciting than I expected, the more I know about live modeling the more I realized how different live modeling is from traditional modeling.

I’ll share my experiences and thoughts in a few blog posts, and I would like to hear what you think.

I’ll start with calibration, the task I am working right now.

### Calibration Goals

When working on planning projects, the things we care most are the “exceptions”, the time when the system start to fail. However, for live modeling, our focus is the “normal” conditions, what the system should look like on a day to day basis. Therefore, when it comes to calibration, our focus changes from matching the peak values to matching the average values.

In other words, the value proposition of a model changed from making sure the model can accurately fail the system when it rains, to making sure on an typical day the model shows what the system supposed to behave.

With that in mind, I devised two new calibration goals,

* the general shape should match
* the daily average flow should be within +/-10%

### Challenges

When calibrating for storm events, we have only a handful of events to calibrate. However, when it comes to a typical day of a year, we have thousands of days to calibrate. It has two implications,

* We need to handle a lot more data when doing the calibration
* We need to automate the calibration reporting process, there is no way we can manually check the calibration on a day to day basis

### Experiments

To address the data challenge, I rolled out my own implementation of calibration reporting. I used SQLITE as the backend database, and writing python scripts to generate the calibration reports. The reasons for customization will become more obvious once I show the type of reports I will need to create.

When it comes to calibration, I might have 10 ideas on how to improve the calibration, the ability to glance through the results and knowing immediately if it increased or decreased the calibration is key to how many iterations I can work on a flow meter.

So I need to create figures with the results jumping at me without me even thinking about it.

As shown below, I created this customized graph. It might look really busy at first glance, but I’ll show you how the information is layered for both fast glance and in-depth examination.

* both the simulated and observed flow data are shown
* the green dashed line is the daily average error, calculated as the daily average of : (sim-obs)/obs. It uses the secondary axis
* the purple fill is the [NSE](https://en.wikipedia.org/wiki/Nash%E2%80%93Sutcliffe_model_efficiency_coefficient) score, which measures the goodness of match between the observed and simulated for each day. If there is a bad match, then the day is filled in purple.

![](images\1_yLlkpROMZ_UQIt7T1-bvCg.png)

When I look at the graph, my first glance only focus on two things

* the green dashed line should be within the +/-10% band
* there should be as few purple days as possible

![](images\1_ba585mBst6XXU4av3Fyk6g.png)

Once I see something is not meeting the calibration goal, I’ll focus on the observed vs simulated lines to see why they are not matching, is that because the wet weather flow, or a shifting in the ground water infiltration, etc.

### Automation

As the example below shows, I can pack more than 90 days of 5 min flow calibration data in this one graph, and it takes me only seconds to understand its meaning.

With such visualization, I can go through my calibration of 50+ meters in 10 minutes and having a very good idea how it is doing during the calibration.

![](images\1_htYd_EGBUp00E1PwPvBxWw.jpeg)

Here is one thing I would like to point out, these graphs are not created for the final report. They are used to help the modeler to gain a feel of how the calibration is doing, so that the modeler can keep improving the calibration.

With that in mind, we cannot afford to manually create such visualizations because if we would like to try say 3 iterations for each flow meter, and for more than 50 flow meters, we’ll need to create more than 150 graphs, that can take days to do manually. Therefore, such tasks must be automated because the whole point of doing this is that it will save the modeler time to get a feel of the calibration.

### Conclusion

In this article, we discussed the need of calibrating a model for extended period for live modeling applications and its challenges. We also presented a customized graph that can pack a lot of detailed information while requires very little effort from the modeler to judge the calibration.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 21, 2021](https://medium.com/p/6fed9d6d113f).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-calibrate-a-live-model-6fed9d6d113f)

Exported from [Medium](https://medium.com) on March 18, 2025.