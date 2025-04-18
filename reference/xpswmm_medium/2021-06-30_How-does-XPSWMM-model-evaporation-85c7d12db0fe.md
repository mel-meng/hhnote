# How does XPSWMM model evaporation

source: Innovyze Support Portal

---

### How does XPSWMM model evaporation

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-does-XPSWMM-model-evaporation)

Evaporation in XPSWMM applies to the SWMM runoff. As shown below, SWMM uses the non-linear reservoir to model runoff for subcatchment.

ds is the depression depth, d is the water depth on the subcatchment. When it rains, water will start to pond on the subcatchment surface, and at each time step, and standing water will lose depth based on the evaporation rate. If the evaporation is given as 0.1 in/day, then it will translate into a depth based on the time step for the water to be removed from the subcatchment. At the same time, infiltration will happen based on the infiltration method used. Then the flow can be calculated using the Manning’s equation like formula.

![](images\1__iynv6HaQsXIP5PNL-Aw6Q.png)

That description is for one type of subcatchment. SWMM runoff allows more detailed description of the subcatchments into pervious and impervious, and the area with and without depression.

![](images\1_Kt-n6Kwt04P7ql8I8xTKcA.png)

For continuous simulation, evaporation might have significant impact on the runoff. Especially for depressed area, evaporation can dry these areas up quickly and thus allowing the infiltration to recover sooner. Once the subcatchment is dry, evaporation no longer has impact on its hydrology.

Here is an example, we set up different evaporation rate for Jan and Feb. Feb is 5 times as high.

![](images\1_-v6Iu1QpfeARMG2cXzYrQQ.png)

A simulation from 1/30–2/5 that rained one day in Jan and one day in Feb.

![](images\1_8RXYlpZ-E4Sh6tZNVJautA.png)

The following scenarios were compared,

* base: the base line
* depression: increase the depression area
* no evaporation: set evaporation at 0

The runoff is shown below,

![](images\1_3nlp_R_jJ2FN65C47-RZKA.png)

If we zoom in closer to the first peak,

* no evaporation has the highest peak: the surface water not evaporated becomes flow
* depression has the lowest peak: some of the rainfall was stored in the depressed area

Next, let’s compare the infiltration rate,

For the first storm it looks almost the same except,

* depression has standing water longer on the surface, therefore, the red line dropped to zero the last
* base dried out the first because it has less water on the surface to drain than the no evaporation scenario

![](images\1_nbKqNCM6sfLZJyPHjg3NAg.png)

Now if we look at the second peak, the factors impacting the second peak are,

* the evaporation rate is different this time
* the infiltration capacity is different because of the first storm event
* everything else is the same as the first event

base has the highest peak infiltration rate because of the evaporation allowed the subcatchment to dry earlier thus recover more capacity

depression has the lowest peak infiltration rate because it has standing water on the surface longer, thus has less time to recover to full capacity.

![](images\1_RWMZgo6AeagnXK4E1OOQwA.png)

In conclusion, although each of the processes of precipitation, evaporation and infiltration is quite simple. Once combined, it can generate complex flow patterns.

You can find the model on [github](https://github.com/mel-meng/xpswmm/blob/master/models/evaporation/evaporation.zip).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 30, 2021](https://medium.com/p/85c7d12db0fe).

[Canonical link](https://medium.com/@mel-meng-pe/how-does-xpswmm-model-evaporation-85c7d12db0fe)

Exported from [Medium](https://medium.com) on March 18, 2025.