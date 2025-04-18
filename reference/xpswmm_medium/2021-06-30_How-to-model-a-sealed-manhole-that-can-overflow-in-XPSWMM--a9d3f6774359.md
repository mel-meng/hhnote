# How to model a sealed manhole that can overflow in XPSWMM?

source: Innovyze Support Portal

---

### How to model a sealed manhole that can overflow in XPSWMM?

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-model-a-sealed-manhole-that-can-overflow-in-XPSWMM)

When the underground system is overwhelmed, significant amount of flow can overflow to the surface through manholes, but the manhole might not be designed as an inlet to collect surface water.

Under such situation how should we model the node?

It turned out to be quite simple,

1. Link the Spill Crest to 2D: this will allow flow to be exchanged between the node and the surface
2. check Inlet Capacity
3. Set the maximum Capacity to 0: this will limit the flow from surface to node to 0

![](images\1_3OVelprFzTPOXVpVnn25Kw.png)

To illustrate the impact, here is an example.

The 2D surface is flat at 90 ft elevation. It has standing water on it. The 1D system is controlled by an outfall with water level rising from 80ft to 100ft.

![](images\1_nlNgOSNimy_9XABHmraIRg.png)![](images\1_oXAF3434uqFVKpd_XDM5nQ.png)

So at the beginning water will be ponding on top of the node 4. Then as the outfall water level increases, water will come out of node 4 to the grid. As shown in the figure about, it is around 2AM, the water level in the pipe is higher than the surface, and there should be overflow to the surface.

Two scenarios are created,

* Base: max. inlet capacity is 5cfs
* Inlet tiny flow: inlet capacity is 0 cfs

As shown below,

* base scenario shows inflow around 5 cfs when there is capacity, and overflow after 2am when the pipe is overflowing
* inlet tiny flow scenario shows no flow until the water in the outfall is higher than the surface

![](images\1_RRnGavZZL2MbY5_ZxxEAKg.png)

The model can be found on [github](https://github.com/mel-meng/xpswmm/blob/master/models/inlet/1d_inlet_no_inflow_only_overflow.zip).

### Using 2D Inflow Capture

Another approach is using the 2D Inflow Capture option.

1. link spill crest to 2D
2. uncheck inlet capacity
3. check 2D inflow capture
4. set the coefficient as 0

![](images\1_6On5SGVhHemh72rtdA6laA.png)

However, by default the coefficient cannot be lower than 0.001, and we need to overwrite the UI validation rule.

![](images\1_JXM2W-YHz79PfUaTSNOBaQ.png)

Then change The lower error to 0 will get rid of the warning.

![](images\1_wzOccdh5Vs8_QvpZTrkBMQ.png)

A tip on getting the key name is by hovering the mouse over the field.

![](images\1_TLlBzky8mvsnHYLrZ2Au7Q.png)

With 2d inflow capture, there is no flow reported at the inlet. Let’s check the outgoing pipe of the sealed manhole,

* blue is base which can accept inflow
* red is when coefficient is set as 0, as it shows, there is no inflow and only overflow (<0)

![](images\1_zSMwjzoDSkPRsTpeuH5Ipg.png)

The model can be downloaded from [github](https://github.com/mel-meng/xpswmm/blob/master/models/inlet/1d_inlet_no_inflow_only_overflow_2d_capture.zip).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 30, 2021](https://medium.com/p/a9d3f6774359).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-model-a-sealed-manhole-that-can-overflow-in-xpswmm-a9d3f6774359)

Exported from [Medium](https://medium.com) on March 18, 2025.