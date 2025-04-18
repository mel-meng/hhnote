# How to model a pump station?

Set up a pump station is one of the more complicated modeling tasks. So what is a pump station, and how does it work. I found this 1 min…

---

### How to model a pump station?

Set up a pump station is one of the more complicated modeling tasks. So what is a pump station, and how does it work. I found this 1 min. sump pump video quite helpful.

As you can see a pump station does a few things,

* It collects the water in a sump or a wet well
* When the water is high enough it starts to pump
* when the water level is low enough it stops pump

Let’s think about why it works this way. The purpose of a pump is to move the water from a low spot to a high spot. Ideally, it should just pump whatever gets into the wet well without the complication of storing the water and having a logic to trigger the pump on and off. So why do we need to do all these extra things?

The main reason is that it costs money to operate a pump, and we would like to keep the cost of operating the pump low.

A pump operates very similar to a car, if you want to keep your car at optimal operating condition you would like it to cruise on the highway at a nice speed , if you would like to save money on gas, then you need to avoid getting stuck in the traffic, moving at a very slow speed with lots of stops.

With the use of a wet well, we can achieve both objectives,

* we’ll store enough water in the well so that we can keep the pump working longer without interruption.
* We can operate the pump at an optimal range by controlling the on/off levels

The above approach works pretty well for most of the pump stations that the pumps are off most of the time. For pump stations that are on most of the time with a wide range of flow, variable speed pumps might work better.

### Theory

Let’s review how a mechanical propeller pump works. A [typical pump station](https://swmm5.org/2016/09/04/pump-calculations-for-infoswmm-and-swmm5/) is shown below, to conserve energy, the head the pump added to the flow (hp), should balance out the friction losses through the pipes and elevation difference (z2-z1), plus the velocity difference for the kinetic energy changes.

![](images\0_TtdpZ4HwyjHkM0qQ.jpg)

The way a propeller pump operates can be defined as a pump curve. As shown in the figure below, as the flow increases, the pump head will decreases. This makes sense as the more water you are trying to move up, the heavier they will be and therefore, the lower you’ll be able to lift it.

![](images\0_VVSCZ6sZ5WxEej52)

A pump curve is usually provided by a manufacturer, sometimes we have pump curves from field measurements.

When designing a pump station, we want the pump to operate under an idea condition ( like cruising on a highway for a car). This is achieved by overlaying the system head curve on top of the pump curve. Imagine we have an ideal pump that can pump at any flow rate, using the energy conservation equation we can then calculate the needed pump head for any discharge flow rate (the headloss through the pipes + elevation difference on either side of the pump station). The intersection is the operating point for the selected pump, and we need to make sure that the pump is at its highest efficiency.

### Modeling a pump station

I hope now you have some idea what the pump station should behave in a model. For most of the pump stations, it should behave very similar to a sump pump. The pump should be off most of the time, once the wet well is full, it will pump continuously for a while at an almost constant flow rate until the wet well is empty.

A common issue with pump in a model is the pump cycles on and off very quickly. As we have discussed, most likely it is not how the pump should work in reality, if the pump cycles on and off every 30 seconds, probably it will not last very long. Ideally, the pump will pump at a much lower flow rate a lot longer.

A common source of error is that the pump curve usually is for the pump alone without taking into account of all the head losses through the pump station and the force mains. Therefore, the modeled pump is pumping more flow because it only needs to overcome the elevation difference without counting the head losses.

Accurately estimating the headloss through a pump station is usually a design task for mechanical engineer specialized in pump station design, and most modelers are not familiar with such calculations. Therefore, it is important for modelers to set clear expectations on how accurate the model can simulate the flow through a pump station.

Fortunately, for most planning projects, accurately modeling the pump station is usually not a crucial objective when the calibration meter is far from the pump station. This is because for most systems, once the pumped flow is mixed with other gravity flow, and goes downstream for a while, the dilution and attenuation effects will mostly smooth the pump flow and result similar flow patterns if we feed the inflow to the system without a pump station.

In the next post, we’ll focus on how to more accurately model the headloss through the pump station and force mains.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 13, 2022](https://medium.com/p/f0a177798b43).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-model-a-pump-station-f0a177798b43)

Exported from [Medium](https://medium.com) on March 18, 2025.