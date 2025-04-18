# Testing XPSWMM 1d/2d inlet flow exchange

When I started my modeling career, I thought if I need to know how a model works, then I’ll need to understand all the differential…

---

### Testing XPSWMM 1d/2d inlet flow exchange

When I started my modeling career, I thought if I need to know how a model works, then I’ll need to understand all the differential equations. But a few years into it, I realized that I can get by with knowing just enough which are much easier to learn by myself.

In this post, I will share how I get answers by doing experiments with models. Although it is an XPSWMM model, the concept is the same for any type of models.

### The problem

As I am working on XPSWMM 2D models, I found that it is not that clear how flow is exchanged between a 2D cell and a 1D node.

![](images\1_RhRlosNblpU4fg55wIZyyw.png)

As shown above,

* using the inet capacity settings (1)
* using 2D inflow Capture (2)
* if nothing is selected, it uses the default option

And I found the “default” option can be confusing, according to the [help](https://help.innovyze.com/display/xps/2D+Job+Control+Settings#id-2DJobControlSettings-2DInflowCapture), 2D inflow capture is the preferred option and the “default” option is a pretty old method that shouldn’t be used.

![](images\1_OlSpQwFgGuNPW7pwC-rJfQ.png)

The ‘pre-2009 method’ is dependent on the 1D/2D sync time, **if you half the time step, the flow rate will double. Not a great choice for 1d/2d flow exchange.**

As a modeler, I found situations like this happen quite often. I don’t always find answers from the documentations. And it is just the nature of software. As the software evolve, things start to change, bugs are being fixed, then things got complicated. I don’t have a good solution to avoid this from happening, but I think experimenting is the best way I know can sort things out.

So I set out to make sense out of all this seemingly confusing statements.

I will setup a few models to test what XPSWMM does when using the default option, Q=Area of Manhole X depth/time step.

### Tests

The tests are quite boring, so I’ll just show my findings,

* I used XPSWMM 2019.1.2 for testing.
* The default setting is not reliable. It looks like if I ever set the 2D flow capture option, even if I turn it off. The “default” will be using the 2D inflow capture instead (dirty models).
* The default 2d inflow capture is Q=13.382\*depth ^.5, even though I didn’t enter anything in the settings
* For a clean 2D model (I never turned on 2D inflow capture), when using the default setting, the 1d/2d sync time does impact the flow rate as shown in the help file (clean models).

The results are shown in the figure below,

* All the dashed lines are manually calculated using the equation from the help file, and they match pretty well with the simulated results.
* Only the default\_1sec\_clean/default\_2sec\_clean showed the expected behavior for “default” settings, which is a clean model without ever setting 2D capture
* All other models show the same results using the default 2D flow capture, although I checked it off

![](images\1_MpLQJNbGCJAfQHYfeFugog.png)

### How I setup experiment

You can read more if you are interested how I did the experiments.

You can find the models and notebook on [github](https://github.com/mel-meng/xpswmm/tree/master/models/1d2d).

I usually start with my problem. My goal is to test if the relationship between the Q and 2D cell depth is indeed what is used in XPSWMM, then I need to have a figure looks like above to test it. However, the challenge is that XPSWMM doesn’t give me Q and depth for a manhole. So I need to figure out a way I can get enough Q and Depth pairs to produce a plot like that.

After some experimentation, I found the following,

* 2D cell depth can be reported using a point
* Flow into a manhole can be tricky as it is not reported for manhole

I can add a pipe, but it can be quite different from the inlet flow. I can also use a storage node, then I can calculate flow from the stage of the storage.

Next, I need to get a good range of depth and flow so that I can correlate Q and Depth. So if I vary the flow and depth of the flow over my 2D grid, I should have enough data points.

### Model

Here is how I setup the model and developed the curves.

#### 2D surface

I just need some water ponding on top of the inlet. I created a flat surface with 90ft elevation, then I added inflow at one end and a boundary at another end.

#### Storage

There is no good way to get the inflow into a node without using an inlet. So my hack is to setup the node as storage with constact area, so that I can calculate inlet inflow from the stage.

I added a storage node with

* fixed area of 10000 sf
* invert of 85ft
* link to the crest the same as the 2D 90ft

### Scenarios

All models are using the extreme engine and the same 1d/2d settings except,

“dirty” models, I turned on the 2d flow capture and run the model, then checked it off, this seems to set the default to use the new 2D capture equations

* default\_1sec: 1d/2d sync time step = 1 sec
* default\_2sec: 1d/2d sync time step = 2 sec

“clean” models

* default\_1sec\_clean: 1d/2d sync time step = 1 sec
* default\_2sec\_clean: 1d/2d sync time step = 2 sec

Other models

* default\_2sec\_classic: using the classic engine
* 2d\_capture\_default: using the 2d inflow capture option

### Results

I exported the Stage and 2D water surface time series for the comparison to develop the relationship between Q and Depth.

I copy and pasted the results from XPSWMM to an excel file: default\_inlet.xlsx. Then did some calculations to get,

* flow: Q = (stage@time step 2 — stage@time step 1)\*area/time step
* Depth D= water head — node rim elevation

You can find the calculation in this [notebook](https://github.com/mel-meng/xpswmm/blob/master/models/1d2d/Default%20Inlet%20Capture.ipynb).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 24, 2020](https://medium.com/p/29c6dad2b899).

[Canonical link](https://medium.com/@mel-meng-pe/testing-xpswmm-1d-2d-inlet-flow-exchange-29c6dad2b899)

Exported from [Medium](https://medium.com) on March 18, 2025.