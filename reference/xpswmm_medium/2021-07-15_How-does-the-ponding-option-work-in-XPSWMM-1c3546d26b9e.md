# How does the ponding option work in XPSWMM

source: Innovyze Support Portal

---

### How does the ponding option work in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-does-the-ponding-option-work-in-XPSWMM)

Ponding options for nodes can be confusing. You can find more about it from the online [help](https://help.innovyze.com/display/xps/Hydraulics+Node+Data#HydraulicsNodeData-PondingPonding).

Here is a quick summary,

* None: any overflow will disappear
* allowed: a quick and dirty way to get water stored above the node, and later the flow back to the system. Usually a more conservative way of sizing your system during very early stage of planning or design. In more detailed modeling, this option will be replaced with more realistic storage curves
* sealed: if it is a sealed manhole or a structure that doesn’t allow overflow

![](images\1_jiajwc3IpsjUdyv6wnMApQ.png)

So what about link to 2D surfaces?

* link spill crest to 2d: most of the times this is how a manhole should be connected to 2D
* link invert to 2d: for river and open channel where the node is “imaginary”, this usually is the right option.

One thing I would like to share is how we can learn from the model directly. To become an experienced modeler, the most important skill is to gain insights from the model, in other words, we need to be very good at using model as a learning tool.

In this case, we would like to learn more about how we can model overflows from a node. The easiest thing to do is to run a model with all the options and see what happens next.

As shown below, we setup a model with a node for each ponding option,

* invert is 0ft
* rim is 10ft
* a constant inflow of 10cfs
* each node is named after the ponding option
* the model has no 2D components

![](images\1_x_V8ej0K-ecqG3OqP7Wtvw.png)

The results are shown below,

option 2, 3, 4 are the same: so we know when there is no 2D but we are choosing the 2D options, it acted as “allowed” option.

option 1 is “None” and option 5 is “Sealed”.

* we can see the overflow amount is the same for all options except sealed because it doesn’t overflow at all
* for option 1 none: the level stopped at 10ft where the rim is
* for option 2, 3, 4: it follow the storage curve of the allowed storage

![](images\1_QcSGAouWwUNPl6etU8igGw.png)

You can find the model on [Github](https://github.com/mel-meng/xpswmm/tree/master/models/ponding_options).

I hope you find this simple model very helpful in understanding how different ponding options work. You can use similar models to learn how a model works directly from the results.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [July 15, 2021](https://medium.com/p/1c3546d26b9e).

[Canonical link](https://medium.com/@mel-meng-pe/how-does-the-ponding-option-work-in-xpswmm-1c3546d26b9e)

Exported from [Medium](https://medium.com) on March 18, 2025.