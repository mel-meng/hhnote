# Sanitary Sewer Model Calibration Review

As I am working on updating the training manuals for calibration, I realized I couldn’t find anything that is accessible for new modelers…

---

### Sanitary Sewer Model Calibration Review

As I am working on updating the training manuals for calibration, I realized I couldn’t find anything that is accessible for new modelers. So I hope this piece will make a good easy introduction to calibration.

### Theoretical Framework for Calibration

The [Rules for responsible modeling](https://www.chiwater.com/Files/R184_CHI_Rules.pdf) is a **MUST** read if you are taking modeling seriously. Even graduate level education doesn’t cover the basics of modeling complex system, therefore, most modelers don’t have the tools and vocabulary to communicate and investigate the most fundamental question, how much can I trust the modeling results?

The [Users Guide to SWMM5](https://www.chiwater.com/Files/UsersGuideToSWMM5Edn13.pdf) did a great job summarizes these concepts in the chapter: The continuous modeling philosophy. Here are a few highlights,

### Language used for calibration

I don’t think I ever met a person using all of the terms below describing the calibration process. However, I do believe a good understanding of such concepts can help communicate calibration results more effective.

* parameters: such as pipe diameter, manning’s n
* calibration parameters: such as RTK parameters, dry weather parameters
* input functions (IFs): my understanding is that any input data that is a function of time qualifies. The rainfall data is most common, or maybe the control rules. Usually such functions have the biggest impact on modeling results
* response functions (RFs): it is the simulated flow, depth and velocity for a meter location
* objective function (OFs): statistics of the observed or simulated time series, e.g. peak flow, volume, etc.
* performance evaluation functions (EFs): it compares the simulated and observed objective functions, and calculate the errors or differences. e.g. peak flow error, NSE for shape match.

Here is an example,

Calibration goals expressed as EFs:

* EF1: peak flow within +/- 10% ([sim — obs]/obs]
* IF1: storm for event 1
* RF1: simulated flow
* OF1: max(flow)

Isn’t this a much better way to define and communicate calibration? I think so.

The general calibration process is shown below,

Calibration Loop

* I prepare my calibration model, and the event rainfall data
* I feed a starting calibration parameters
* I run the model
* Then I compile my RFs (flow, depth time series)
* And calculate my OFs (peak flows, timing of the peak)
* Then I use the EFs to compare sim to obs (peak values, shape of the matches)

![](images\1_8KAshbyqtAZG-DwiOVG0xg.png)

If the EFs are OK, I am done with calibration. If not, I’ll need to go to the parameter selection loop.

Parameter selection Loop, (I added a few of my own comments)

* the goal is to develop rules like, if I change parameter X, then I can change the response in Y. (e.g. If I change T1, I can shift the timing of the peak)
* make a guess, say I think increase T1 by 1hr, the time of peak will shift by 1hr
* sensitivity analysis, I run a few models with different T1 values, then I see if indeed time of peak will shift by 1hr
* parameter optimization, most likely my guess is off so through the process of doing sensitivity analysis I usually can refine my calibration,
* my time to peak is off by 1.5hr, based on my sensitivity analysis runs, by simply adjusting T1 within 30min — 1hr I can get it to match better

### Inference

Inference is such a big word, the definition works for me is this, given data and calculate probability.

In our case, given a calibrated model and long term flow monitoring data, what is the probability the model can predict a xxx (design storm, proposed scenario, etc) event?

In practice such analysis only appear in PhD dissertations and scientific journals. It is rarely done for planning or design modeling projects. However, there are some low hanging fruits modelers can do to increase our understanding how reliable our models are.

Communicating the likelihood a model can be right or wrong is very hard, because even with enough data and analysis, uncertainty is simply a foreign idea to most people.

What I think might work better is pointing out where the errors can come from, and what that means for the modeling results, and present it as a narrative rather than analysis. In most cases, making everyone aware of the model’s limitations is all that is needed for a project.

Coming from my own experiences, most engineering reports prefer positive words when communicating negative ideas. So errors becomes uncertainty or risks, and therefore I found these concepts are quite confusing.

In this context,

* Error is the difference between a computed and an observed value
* Uncertainty is taken to mean a possible value an error may have

Therefore, for any proposed conditions modeling results, we need to discuss uncertainties, which means the things we know that can go wrong.

So where can errors come from,

Mistakes

* mistakes in preparing the data
* wrong GIS and survey data
* model a structure using the wrong type of object

Errors inherent of a method (simply double-checking won’t fix it),

* observation error, e.g. flow meter can be off by +-10%
* sampling error, e.g. using a rain gage far away from the study area
* numerical error, e.g. spikes caused by stability issues
* structural error, related to dis-aggregation. e.g. modeling a whole basin as a single node, the routing and storage of the area is ignored
* structural error, related to poor formulation of one or more of the component processes. e.g. without modeling ground water, it cannot account for seasonal changes
* propagated error, related to erroneously estimated values of input parameters. e.g. if R1 is off by 10%, what will the error be in the peak flow for the design storm.

### RTK Method

For RDII (rain derived inflow & infiltration), RTK is the most widely used method, and even if you are not using RTK method. I believe RTK is great for learning calibration due to its simplicity. A good review of the RTK method can be found in the [SWMM5 hydrology reference manual](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P100NYRA.txt)

![](images\1_e90-w7Ca1DX6derKZAeRPQ.png)![](images\1_gM8A5HBbVhkpHGkZc8ujiA.png)![](images\1_Dn78Xp5qxKgDkPA3tqACMQ.png)

It also provides a simple example,

![](images\1_9mgmeNko8M8BtnRZNF4Z_g.png)

### Strategy on Calibrating Long Term Simulation

Calibration requires a lot of time trying many different parameter combinations. There are some guidelines and best practices published over the years to help modelers speed up the process. The main idea is to,

* reduce the number of events needed to calibrate the model, ideally we can calibrate a model with just 3 or 4 events.
* reduce the number of parameters that controls a key part of the shape of the response, ideally we can establish rules like t1 controls the peak, and t3 controls the deflection point of the long tail.

Hazem showed a [stepped approach](https://www.chijournal.org/R236-01) to calibrate RTK parameters.

![](images\1_lJzTutLPAv5IrdxdT9xdiA.png)

Step 1 calibrate the second event without IA impacts on RTK values (reduce the number of parameters)

![](images\1_fxJD8EneF_DN_mlzJl69fQ.png)

Step 2 R can be directly calculated since there is no IA (find strong correlation of the parameter and the response)

Step 3 Calibrate T, K for that event

Step 4 Calibrate IA parameters

Initial abstraction can be “observed” if you have good flow monitoring data. For example after a long dry period, then it rained a little and registered some responses. And that total rainfall can be used as the estimates of the Ia.

![](images\1_3pChxegVjamIEv-pcusydg.png)

### Physical Meaning of the 3 RTK Sets

In order to use the model for master planning purposes, we have to project future condition for RDII. Therefore, the calibrated parameters must have real-world meanings, otherwise, we cannot establish the reasoning. For example, if the plan is to remove 20% of direct inflow through disconnection of the downspouts, we need to be confident the R1, T1, K1 is actually modeling the such contribution, so that we can reduce R1 by 20% to represent such improvements.

This [paper](https://www.chijournal.org/R241-11) gives great explanation on the meaning of RTK values.

![](images\1_lv18WPiwYPa5jVH_s2oHyQ.png)

This is a great picture showing how the T, K values are affecting the shape of the final hydrograph.

![](images\1_fn3yjF_j1bkUVSCZw97_8Q.png)![](images\1_SQ64MzA89wsKNj4tYEjC2g.png)![](images\1_tgG6GzQi4TEA5XBVK3O1VQ.png)![](images\1_iDsV9ZZWEqd91AwHEnD6hw.png)

It also has very practical advice on how to calibrate RTK values.

![](images\1__D9ob55peC89nOMsh846og.png)

A good initial calibration event,

* No need to calibrate IA parameters
* winter, soil is saturated and evaporation is low
* 2nd storm of the back to back storm
* the storm event should be dominated by high intensity rainfall time steps, this will generate the shape of hydrograph we can link to calibration parameters

![](images\1_OcwD5XYzmBvVkHntfYazHw.png)

### Challenges of the RTK Method

A great [review](https://www.chijournal.org/R245-08) listed the following,

* AMC(Antecedent Moisture Conditions): it is hard to estimate initial abstraction
* ground water inflow can only be accounted in DWF, not directly in RDII
* Calibration is Time consuming, 20h for each meter (Bennett’s book)
* Parameters and Physical Characteristics
* - RTK is a black box, it doesn’t rely on any physical characteristics
* - No predicting power on system design to reduce I/I

I found a few papers that addresses the above challenges.

### Seasonal Changes

Without modeling the actual ground water seasonal cycles, RTK is very limited to simulating season changes observed in flow data.

A good way to evaluate the seasonal variation of I/I is using the Cumulative Rainfall(in) vs I/I (in). As shown below, there are 3 distinct parts in the chart below,

* from 4/29–12/3, the same amount of rainfall generates less I/I
* from 12/3–4/29, more I/I is observed

[City of Columbus](https://www.chijournal.org/R241-12) showed one way to get around this limitation by using the following techniques,

* Using seasonal RTK parameters, growth vs dormant
* Using monthly IA parameters

![](images\1_H3WT0e48WH3rebMM1nO7bg.png)

### Correlate RTK with Basin Characteristics

[This paper](https://www.chijournal.org/Journals/PDF/R246-04) from Columbus correlated RTK to basin characteristics.

* age of the basin
* pipe density of the basin

And pipe ages and density showed strong correlation to the total R of the basin. With such relationship, the I/I from unmetered basin can be estimated.

![](images\1_PrsvYEUM3s0LyxsjZ3cxCg.png)![](images\1_YCbLNrI8WtZUip7eF942mw.png)

### Estimating GWI

This [paper](https://www.chijournal.org/Journals/PDF/R246-21) shows a method of correlating previous n days total rainfall with GWI for each month to develop GWI patterns. With this method, a monthly constant GWI component can be more accurately estimated.

![](images\1_rWAzQIBFVWZNL9_RgXgXzg.png)

### Ground Water Modeling

For more complicated ground water impact, using the ground water module has been proved effective.

City of Cincinnati has a good [paper](https://www.chijournal.org/C406) on this topic. It has a good chart showing how different components should be added to a model.

![](images\1_mF7NigbhmBPHWxq4f8-Hgw.png)![](images\1_plExMdufwoddEvgPdTL_pA.png)![](images\1_KhvFA_p-NvfQAySiEitsng.png)

You can find more about the procedures in Cincinnati [modeling standards](http://www.msdgc.org/downloads/doing_business/capital_project_resource_library/modeling/Modeling_Guidance_Rev_4_Draft3_2018-03-01.pdf).

### Subcatchment, Long term aquifer and short aquifer

This [paper](https://www.chijournal.org/C385) shows how to use ground water module in SWMM5 to model RDII using subcatchments to model direct inflow, a long term aquifer and a short term aquifer approach.

![](images\1_Bhj7k8NlfDNnUl8MKuMH4g.png)

### Conclusion

I hope this post will give you some good idea of the sanitary sewer calibration process.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 13, 2020](https://medium.com/p/73b9e2b19b38).

[Canonical link](https://medium.com/@mel-meng-pe/sanitary-sewer-model-calibration-review-73b9e2b19b38)

Exported from [Medium](https://medium.com) on March 18, 2025.