# WaterTalks — Calibration Tools Part 2

Nathan: why calibration is so hard?

---

### WaterTalks — Calibration Tools Part 2

Here is the link to [part 1](https://medium.com/@mel.meng.pe/watertalks-calibration-tools-part-1-e9e5bf5b364d).

**Nathan:** why calibration is so hard?

**Mel:** Great question. I hope my example makes sense. One annoying thing my son started to do since last year was flipping a half full water bottle so that it will land standing up. The noise just drives me crazy. Calibration is quite similar to flipping a bottle. There are so many different ways to flip a bottle, but just a small percentage of my flips will end up with a standing bottle. Based on my own experiences and some of the published numbers, calibrating a flow meter takes about two days, so it is in general not a very easy task.

**Nathan:** So how can we speed it up?

**Mel:** The same advice for flipping a bottle apply, practice makes perfect. After trying it for a while, I’ll get a feel what works and what is not. So the key is how fast I can learn from my experiments. That’s exactly how PhD students do their research. Form a hypothesis about how things work, do some experiments, then learn from it. I just keep doing it until figure it out.

**Nathan:** Can you give us a few examples?

**Mel:** This picture shows a good example, I can easily see that the 3 triangles control the overall shape of the results, the red line. By adjusting the timing of the 3 peaks of the triangles, I can easily change the shape of the results.

![](images\1_AoXwldj0HiKOcbYhBeLVWQ.png)

From a good example you can learn a lot

However, from the figure below. There is very little I can learn. So I need to be smart how I setup my experiments, so that I can learn faster and easier.

![](images\1_m30DxBVdtY_Scn29ca6Z9w.png)

**Nathan:** so you need to learn in a intentional manner, right?

**Mel:** All parameter changes should be intentional, I should have some rough idea how it will improve the match. If it doesn’t work as expected, I need to revise my hypothesis, test it and learn something about it. I should be able to say if I change this guy here, this part of the results will match better.

**Nathan:** now we have permanent flow meters, how can that improve a model?

**Mel:** One misunderstanding is that I will need a lot of data to calibrate a model. For planning purposes, I can calibrate a model pretty well with just a few good storm events. Since the models we use are deterministic models, meaning we assume things work in very specific ways, all we are doing is to tweak the parameters used by the equations. If we look at each individual event, we might be able to further tweak the model to match better. However, if we are looking at 5 or 10 events, there is not too much we can do to improve the match for one event without hurting the match for many other events.

In this sense, more data will not make a model better. But with more data, we can answer another important question, how much can we trust the model, the more data we have, the more opportunity for us to evaluate the model’s accuracy.

**Nathan:** how do you select calibration event?

**Mel:** It might not be obvious what to look for when selecting a calibration event, here is what I usually do,

•I would like to calibrate as few events as possible

•I would like to calibrate as few parameters as possible for one event

That translates into the following requirements,

* Reduce the number of parameters to calibrate for each event
* Pick event that is dominate by just a few parameters

**Nathan:** can you give us a few examples?

**Mel:** Yes. If you look at the chart below. Red line is observed flow, and the green line is the dry weather flow without modeling ground water. And the purple line is after considering ground water. Say I want to calibrate an event in June. Instead of calibrating ground water, I’ll just add some constant flow to match the dry weather flow for the week of the event. Once I get that event calibrated, I can then work on ground water calibration. Calibration can be done in stages.

![](images\1_0oOzRSFE4bFxe5srk9eAkA.png)

<https://www.chijournal.org/C406>

Below is another example, if I look at all the events, which one should I choose to calibrate. I will choose the one looks simple. comparing with other events, the highlighted event has a well defined shape that I can easily relate to the RTK parameters. While other events I cannot say that.

![](images\1_yVG4Gc6BOVcXFAUkPfLIzQ.png)

**Mel:** since each basin is different, sooner or later, things will get messy, and I need to run experiments using the model to learn the impact of different combinations of parameters on the calibration results. And this step is also called sensitivity analysis.

As shown below, this is not a great event to calibrate.

![](images\1_pblhnyQxjNa14fULAdD-gQ.png)

But it can be a great event for calibrating initial abstraction. Because the first rain event is a very small event, and we can kind of tell when the initial abstraction happened.

![](images\1_FvYP6DJGdKhVI8Wfjr8sTw.png)

By running model with different dmax values, the amount of rainfall will be absorbed by soil initially, I can get a sense of its impact on the results. Unfortunately, it is not very clear. The smaller value gets the timing better, but higher values get the general shape better. So my best bet is to look at other similar events to see if one is obviously better than another.

![](images\1_7lAgRRzir31P47lUkEAE1A.png)

**Nathan:** Have you used a really long 3rd rtk to simulate very long tail?

**Mel:** It depends. RTK method is not a sophisticated approach for modeling ground water impact. You might be able to get RTK to work or you might not.

For the RTK method, there are some workarounds. I’ve seen people setting up two sets of RTK values one for dormant season, and one for growth season. also use monthly initial abstraction parameters. And they can help to some extent.

And you might try to use the ground water module.

On the other hand, it also depends on your modeling goals. For example, I’ve worked with client that they only need to a 5 yr design storm for spring condition. And if spending two more days getting the long tail calibrated doesn’t impact the peak flow, you don’t really get too much return from that effort.

**Nathan:** Here are the references Mel provided for calibration,

* [Rule’s for responsible Modeling](https://www.chiwater.com/Files/R184_CHI_Rules.pdf)
* [A Detailed Procedure for Separating RDII Stages and Generating a Single Set of RTK Hydrographs for Continuous Simulation](https://www.chijournal.org/R241-11)

**Nathan:** here is a question from the audience. I have multiple pressure zones in the model, should I have different diurnal patterns for each pressure zone?

In general, the more resolution the better. I would say, yes. I would isolate them. Sometimes you have a pump station between different zones that has no flow meter. In these cases you’ll need to apply mass balance across the lumped area wherever you can isolate.

**Nathan:** Can you explain how info360 plot pump curves from Can you explain how info360 plot pump curves from flowrate and suction and discharge pressure?

We just plot the head vs flow curve. And the head can be calculated from the pressure sensors.

Sometimes such data are only available for the pump station, and it can get tricky to get individual pump curves. So in Info360 I can just filter out the data when only that pump is one.

![](images\1_p492ve8PvBTrvSJoVY5m1w.png)

**Nathan:** how does IWLive fit in on the water side?

We have two families of water modeling software. InfoWater, which has been used a lot in the US, uses the EPANET engine. WS Pro, which is used a lot in the UK and round the world, uses our proprietary WS engine. IWLive was built to be on top of the WS engine,it is great for detailed modelers that don’t mind a more complex environment. Sometimes to model complex systems, you need advanced tools. , it is great for real-time modeling. If you would like to do forecasting, it is a great system. Say if we know the condition of the day, what will the pressure be like for the rest of the day.

On the InfoWater side, it is not as streamlined when working with IWLive, the model needs to be converted to WS first to be run in IWLive. If you don’t need the real-time dynamic forecasting, then Info360 is a great option to link to your SCADA system to view real-time data.

**Mel:** Here is another question, should the model be segmented for calibration or the whole model should be used for calibration?

If your model takes 2 hours to run, then it is just not practical to wait for 2 hours every time you change the parameter, in this case, I’ll need to figure out a way to get the model run much faster, and create a smaller submodel is one way. I can also try to simplify the model and try other things.

Another thing is that, at some point of the calibration, your goal is to learn what parameter controls what part of the results. And you don’t need to have a full model to learn, or in some cases, having a full model can make it harder to learn. So you might just create a simple model help you to learn that, which doesn’t even look like the model you are working on. If you are familiar with SSOAP, many modelers start their RTK estimation directly from the flow data without even building a model.

**Nathan:** the question is how does Info360 licensed and deployed?

Info360 can be deployed on premise, but can also be deployed in the cloud.

**Nathan:** there are several questions on the scripts.

It is written in Ruby. And for the model, it is a 5-month simulation, and I’ll figure out a way to share the scripts.

![](images\1_ozF3ePzAgIhQ2wsQrAN5Tw.png)

**Nathan:** Thank you very much for your time.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 10, 2020](https://medium.com/p/a5cda12456ce).

[Canonical link](https://medium.com/@mel-meng-pe/watertalks-calibration-tools-part-2-a5cda12456ce)

Exported from [Medium](https://medium.com) on March 18, 2025.