# How to do a capacity analysis in InfoWorks ICM? — Part 2

In part 1, we went through a few examples of how to identify capacity issues in an model. In this article, we’ll go ahead and fix the…

---

### How to do a capacity analysis in InfoWorks ICM? — Part 2

In [part 1](https://mel-meng-pe.medium.com/how-to-do-an-capacity-analysis-in-infoworks-icm-part-1-d3e498aeea98), we went through a few examples of how to identify capacity issues in an model. In this article, we’ll go ahead and fix the issues and learn a few import ICM tricks.

* How to track changes when sizing the model?
* How to show the changes of the results in a profile?
* How to map the changes of the results?

### How to track changes?

When making changes to the model, it is very easy to lose track of what changes we have made. Here are a few good tips to take advantage of ICM’s advanced database features,

* use scenarios to create different copies of the solution
* use user text to record the original values
* user data flags to highlight the values that changed

First, let’s create a new scenario for sizing the solution.

![](images\1_yludR3E1bEGKXiOgVoZo_A.png)

Next, we need to create a flag and turn it on, so it will flag automatically anything we changed.

![](images\1_MIsEPtlI2m8Ju38A96-Iaw.png)

Next, we make a copy of the original values in the user text field.

1. open the link window
2. copy the width column
3. paste to the user number 1 field

![](images\1_vzgdXYaKNtVSSo2_xXUTSg.png)

next, change the heading of user number 1 to “old width”

![](images\1_nBqcVw8UFlNz-hEKVRKzRQ.png)

### How to show the changes?

We can work with the existing condition results with our alt1 network directly. We’ll load the results and then identify the pipes out of capacity,

1. drag the results to the GeoPlan
2. make sure the scenario is “alt1”
3. drag selection list to the GeoPlan
4. open the long section window

![](images\1_AoyE9mZfNvvsvUHEDCSjGw.png)

Working from downstream end, we look for the surcharge state that is 2 and upsize the pipe to 12 inch, we can modify the profile settings to show the old and new diameters. As shown below, you can quickly identify the changes with just a quick glance with this setup.

![](images\1_lT1qcnJ46Kb13BiUnlHZdg.png)

### How to compare the results?

Next, we’ll run the model and compare the results to see how much improvement the change made.

Validate and save the network, then create a new run with both base and alt1 scenario.

![](images\1_wH4dCZxIzfogcuVOJpQSAA.png)

The compare the before and after results,

1. open the alt1 results in the GeoPlan

![](images\1_kO7gJjprl-ckK6ExppgwdQ.png)

2. Open the base results as alternative results (DWF is base scenario)

![](images\1_M1Be7B5hH_X-gxQQL8JcrA.png)![](images\1_xmJwoQnYJIEjokLT3SnjeA.png)![](images\1_BD3WIdieZmcRPAvTE1NAmw.png)

To get a list of different lines, check the profile properties layout.

![](images\1_Bi2XlWa8cTPTfP8vifs-Ww.png)![](images\1_l4-MvF0QrG4R-qDq7Qfrqg.png)

We just repeat the same process from downstream to upstream, until all the pipes have a surcharge state less than 1.

Similarly, we can also compare the time series, below is the the before and after depth of the pipe. As shown below, the upstream/downstream end depth lowered from the base scenario.

![](images\1_bWOPKUnZ71AsBHDpmtBl2Q.png)

### How to theme the map by comparing two alternatives?

It is great to see the before and after results in the profile and when viewing the time series. How can we quickly identify the changes from the map?

In ICM we can use SQL to create new expression that calculates the difference before and after the changes, then theme the map with the variable.

As shown below, we can quickly identify the pipes that have the biggest change of flow and depth before and after the change using expressions.

![](images\1_x9Enwsx0SfA4U3TqHWnQ7w.png)

The trick is to create an SQL expression for the conduit theme.

![](images\1_h0xqC6dXr8X-w0SCDH3JtA.png)

You can find the model on [github](https://github.com/mel-meng/icm/blob/master/models/capaticy/capacity_analysis.icmt).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [January 19, 2022](https://medium.com/p/6f01aa077cbb).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-do-a-capacity-analysis-in-infoworks-icm-part-2-6f01aa077cbb)

Exported from [Medium](https://medium.com) on March 18, 2025.