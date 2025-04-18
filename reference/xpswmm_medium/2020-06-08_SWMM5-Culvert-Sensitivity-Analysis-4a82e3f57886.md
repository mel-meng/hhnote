# SWMM5 Culvert Sensitivity Analysis

Modeling culvert in SWMM5 is a lot more complicated than using HY8.

---

### SWMM5 Culvert Sensitivity Analysis

![](images\1_c431uc5lVZe4GWQoz50c2g.png)

Modeling culvert in SWMM5 is a lot more complicated than using HY8.

* SWMM5 is unsteady state while HY8 is steady state.
* Upstream/downstream condition is assumed in HY8 and need to be built in SWMM5
* HY8 only computes using inlet and outlet control equations
* SWMM5 use the same inlet control but for outlet control it uses dynamic wave routing
* HY8 implicitly calculates entrance/exit losses based on the culvert type, while SWMM5 explicitly asks for the loss factors

In this post, I’ll answer the question how can these affect the SWMM5 results for a particular problem.

For more details please refer to the notebook [here](https://nbviewer.jupyter.org/github/mel-meng/SewerAnalysis/blob/master/references/culvert/3%20SWMM5%20Culvert%20sensitivity%20analysis.ipynb), and the code on [github](https://github.com/mel-meng/SewerAnalysis/tree/master/references/culvert).

Here is a quick summary,

### Losses

It looks that only when exit loss = 2 will push the curve upward significantly, all other settings seems to produce the same results. However, an exit loss of 2 is too high for most applications.

Since we already know most of the time it is inlet control, it confirmed my understanding for inlet control culvert, the losses are not playing an important role in deciding the headwater.

![](images\1_502UvqyBh79pvIaOAWAr9Q.png)

### Inlet Setting

Since the headwater is calculated as the water depth of the inlet node of the culvert, I would like to see what will impact its depth.

* base:loading directly to the inlet
* storage:loading directly to the inlet, which is modeled as a storage node
* channel: loading to a big channel which then flows into the inlet

### Storage

Looks like storage has very little impact on the results, SWMM5 is able to use the culvert calculation to set the head at the storage node.

### Channel

For different channel widths, they produce very similar results as the base scenario. At low flow region channel200 and channel50 produced slightly higher headwater. And I think that is most likely a result of unsteady state simulation, for bigger channels at low flow conditions, it takes some time to reach steady state level. When I run a constant flow, the level is much closer to the base scenario.

![](images\1_tR9hl44LSRr0_w9CrQmSbA.png)

### Summary

As shown in this post, it is not that hard to conduct sensitivity analysis. I think the important lesson from this exercise is that rather than focus on finding general statements such as “SWMM5 can accurately model culvert using FHWA HDS5 methods or not.”, just do some sensitivity analysis, I don’t think anyone who wrote the software should be responsible for my modeling results. For the kind of complex system we are modeling everyday, nobody can promise everything will work as intended. So let’s lay out how things should be, test it and work with the issues!

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 8, 2020](https://medium.com/p/4a82e3f57886).

[Canonical link](https://medium.com/@mel-meng-pe/swmm5-culvert-sensitivity-analysis-4a82e3f57886)

Exported from [Medium](https://medium.com) on March 18, 2025.