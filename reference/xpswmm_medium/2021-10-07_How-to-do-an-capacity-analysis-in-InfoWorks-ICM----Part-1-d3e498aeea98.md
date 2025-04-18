# How to do an capacity analysis in InfoWorks ICM? — Part 1

Capacity analysis is the reason most models were built in the first place. For many new modelers, this task can feel overwhelming. Don’t…

---

### How to do a capacity analysis in InfoWorks ICM? — Part 1

Capacity analysis is the reason most models were built in the first place. For many new modelers, this task can feel overwhelming. Don’t feel bad, even for experienced modelers, gaining insights from a model with thousands of pipes is not easy. ([part 2](https://mel-meng-pe.medium.com/how-to-do-a-capacity-analysis-in-infoworks-icm-part-2-6f01aa077cbb))

It is like watching Netflix, it takes time to get familiar with the dynamics of a show with many characters and a complicated plot, it can take quite some time just to get familiar with the faces before you can understand the story.

To solve capacity issues, we first need to understand the causes at both a local level and a system level, and that can be a messy and iterative process, you need to stay patient and curious, keep digging and ask questions.

In this article, I’ll walk through a simple capacity analysis example to showcase a few very useful ICM tools that can make some of the tedious tasks feel like a breeze.

### Introduction

For collection systems, capacity requirements usually is defined as a level of service. For example the system should have enough capacity to convey the peak flows of a 5 year design storm without causing basement backups and overflows.

This is commonly translated into simple modeling requirements, here are a few examples,

* freeboard of the manhole should be more than 5 feet to minimize overflow risks
* freeboard of the manhole should be more than 8ft to avoid basement backups
* pipes should not be surcharged to avoid overflow and basement backup risks, etc.

In general, gravity pipes shouldn’t be surcharged during the peak of the storm, and for large diameter pipes buried deep underground, it can be relaxed a little bit.

The job of capacity analysis is to,

* identify the pipes, and nodes that don’t meet the criteria
* understand the causes for the issue
* propose fixes that can resolve the identified capacity issues

### Identify bottleneck

The key concept of capacity analysis can be explained using the manning’s equation.

As shown below, we have a steady state model (the same constant flow through all the pipes).

* the pipe on the downstream end is open channel flow, and can be described using manning’s equation. The slope of the pipe is the same as the slope of the water surface.
* the two pipes upstream of this pipe, however, are surcharged because according to the manning’s equation the flow exceeds its capacity (it has milder slope than the most downstream pipe). Therefore, in order to push more flow through the pipe, it will need more head on the upstream end, therefore, the HGL slope is higher than the pipe slope.

![](images\1_azcMCvEaAukFpYQL8qrJqw.png)

To identify capacity issue is really easy, comparing the slope of the HGL and the slope of the pipe. If the slope of HGL is greater than the slope of the pipe, it means the pipe is limiting the flow through the pipe and pushing the water higher on the upstream end.

In this example below, the downstream pipe has limited capacity and is backing water up. As a results, for the pipe upstream, the slope of the HGL is less than the slope of the pipe, which means it is not flowing at the capacity according to manning’s equation, because water level on the downstream end is pushed up due to the limited capacity by the downstream pipe.

![](images\1_j14GhdfVI_sQK1_y-wTWxg.png)

To summarize,

* when water can flow freely in a gravity pipe, the HGL slope should be the same as the pipe slope, just as manning’s equation predicted
* when the flow is higher than the pipe capacity according to manning’s equation, to push the flow through the pipe, it needs more head on the upstream end to push through, therefore, the slope of HGL is higher than the pipe slope
* when the downstream is backed up, the pipe flow is restricted, to slow the flow through the pipe, the head through the pipe needs to reduce (HGL the difference between the upstream and downstream node), and that’s why the slope of HGL is lower than the pipe slope

Things will get more complicated for unsteady state situation as the flow is never constant. However, in most cases, all the conclusions we got from the steady state still applies if we plot the HGL using the max. water levels.

### Understand/Resolve capacity issues

For planning purposes, we usually fix bottleneck by either upsizing the pipe or building a parallel relief pipe. And some times, a storage might be needed.

For steady state analysis, this task can be easily solved by calculating the flow through each pipe and using manning’s equation to size the pipe so that the pipe capacity is higher than the peak flow.

However, for most collection system, the steady state assumption is not a good one. It overlooked the fact that it could take hours for the peak flow to travel from one end of the system to to the outlet, many pipes still have room to store water as the peak flow moves around. Therefore, the system can handle a peak flow much larger than the steady state calculation might suggest.

Due to this complicated dynamics happening inside a collection system, it is very hard for the modeler to predict what might happen after upsizing a bottleneck pipe without running the model. Therefore, resolving system capacity issues are usually done in a iterative manner. It might look something like this,

* identify the bottleneck
* understand the local cause, is it due to the capacity of this pipe, or a downstream pipe
* understand the system impacts, if you upsize this pipe, it will move more flow downstream, will that cause more problems. What about the timing of the peak flow from different basins, what kind of impact it has on the capacity issues
* based on the understanding, upsize the pipes you believe will best address the issues
* run the model
* see if the results are as expected, if not, review the results to get better understanding of the causes, and repeat

Because a severely restricted downstream end bottleneck can have huge impact on many pipes upstream, in general, capacity issues are addressed from the downstream end, one stretch of pipes a time, moving upstream.

### Review Plan and Profile Views

ICM offers a wide range of tools to help identify and fix capacity issues.

* a rich set of styles to apply to plan and profile views
* interactive, linked animation of hydrograph plots, plan and profile views
* handy statistics that can reveal capacity issues such as surcharge state

When trying to understand capacity issues, the long section view is a must have tool. You can play the animation to watch how the peak flow moves through the system, and there is so much you can get just by taking a quick look.

![](images\1_M-hwflfrnJrv9IhsOU_mLw.png)

However, for a system with thousands of pipes, it is not feasible to review the modeling results by watching the profiles one segment a time. We need a more efficient way to direct our attention to the areas with capacity issues. The best way to achieve that is using the right statistics and applying a map theme to highlight these areas.

* surcharge state tells the causes of the capacity issue of a pipe, 2 means capacity limited (Shgl>Spipe), 1 means downstream backup(Shgl<Spipe), less than 1 means the percentage full by depth of the pipe.

![](images\1_XVJfeCXsvj95BlsCBt2Zdg.png)

* downstream flow/full capacity: a simple statistic showing how much capacity of a pipe is being utilized. Great for comparing pipes of different sizes and slopes.

For example, we can apply a theme to highlight the surcharged pipes and manholes with low freeboard.

![](images\1_A_lu7LUe6RGs6ypxcUbarw.png)

Freeboard and Surcharge State Map

After that we can zoom into the areas with issues, and review the profile. Here is another tip to add more information to the bottom of a profile table, saving you another click.

![](images\1_vHSqhNzctEugc6d4nPNwVQ.png)![](images\1_c31frdww48nGNJoyml0QUg.png)![](images\1_tKq-e9cyQ5Jg-sizfF-5_g.png)

For large systems, going back to the same location can be hard. So select the areas with problems, and create a selection list for it. So that next time you run the model, you can easily go back and show the profile by dragging the list into the long section window.

![](images\1_GIjpEp9X0N8GHRP539XieQ.png)

### Animate the dynamics

The most powerful thing of an ICM model is that it is dynamic (unsteady state), it reveals the complicated interactions how the peak flow passes through the system that we cannot intuitively imagine.

To develop the intuition how a collection system works, watching how the water flows through the system is probably the only way. Be curious, and try to imagine how things should work and verify that with the model, slowly you’ll get better and better at visualizing how water flows through pipes. This process usually involves checking 3 things interactively,

* the hydrograph or the time series of depth, rainfall, etc.
* the plan view of the system
* the profile view of the system

an example is show below,

![](images\1__oI77mffIdmTkmgFPWAo0w.gif)

The hydrograph on the left is the inflow to the first node (flows from west to east). We introduced a pulse of flow at 30min to 2hr.

The pipes are styled based on the percentage of the flow to the full capacity. You can see a general movement of the peak flow through the system in plan view, which is more obvious if you zoom in on the profile view.

Next, we need to ask the questions why it looks like this? By looking at the profile, we can see the slope changed quite a bit through the flow line. Since the flow is the same through all the pipes, and the pipes are in general of the same size, the slope is the most important factor deciding how much capacity each pipe has, and the flatter pipes are the ones showing the most limited capacity (thickest pipe symbols).

However, we can see the timing of the peak flow through each pipe is not the same. If we overlay the hydrograph of 3 pipes from the top middle and end of the flow path. There is a general shift in time as it takes time for the flow to travel from the upstream to the downstream end. In this case the shift is not too much, however, if you have a major branch coming in, the shift can be quite large, and that can present some interesting opportunities for the system to utilize the storage of the system.

![](images\1_8Q5g9KxfiT5SkhwZj9gMDg.png)

In the next post, I’ll go over an example of sizing a solution using scenario manager, data flags and comparing results.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 7, 2021](https://medium.com/p/d3e498aeea98).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-do-an-capacity-analysis-in-infoworks-icm-part-1-d3e498aeea98)

Exported from [Medium](https://medium.com) on March 18, 2025.