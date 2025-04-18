# Water Talks — Sanitary Sewer Modeling Best Practices Part 2

In Part 1, Nathan talked about ICMOne and I shared my personal stories how I got into modeling and some of the lessons I learned. Then…

---

### Water Talks — Sanitary Sewer Modeling Best Practices Part 2

In [Part 1](https://medium.com/@mel.meng.pe/water-talks-sanitary-sewer-modeling-best-practices-part-1-4210a692a41f), Nathan talked about ICMOne and I shared my personal stories how I got into modeling and some of the lessons I learned. Then Nathan showed the exciting application of modeling in real-time operations.

In the next part we answered questions from the audience.

**Mel:** I’ll answer this question “**What is the best practice for incorporating RDII in modeling?**”

Here is my answer: For whatever I/I reduction method you are going to propose, you’ll need to have a way to measure that in the model. If you cannot do that, then you will not have too much confidence on your results. One project I worked on we would like to disconnect the downspouts that connected directly into the sanitary sewer. So we surveyed all the homes in the modeled area, then we modeled the inflow from the roof into the system as subcatchments, and we got pretty good results using the observed roof areas from the field. In this case, we have very high confidence when we say if we disconnect another 20% of the downspouts what will happen.

If you haven’t done the survey of the roof and simply using the RTK method to calibrate the model, it will be very hard to tell what kind of I/I reduction you will have by disconnecting 20% of the downspouts.

One area we started to see more and more is the use of groundwater for calibrating RDII for sanitary sewer systems. The groundwater method has a huge advantage over the RTK method because groundwater method uses detailed land use and soil type, so instead of changing the calibrating parameters of R, you change physical parameters of the land use, thus the model has more predicting power.

**Nathan:** we have more users using ICM with groundwater module. I know Thames water (our UK client) uses ground water sensors to set boundary condition for their real-time model.

**Nathan:** Here is another question. “**Does Innovyze have tools for model calibration?**”

We have the RDII Analyst as part of the Executive Suite for InfoSWMM.

![](images\1_8CHjHIwFCpQYhQ67q071Ng.png)

For ICM, we don’t have a similar tool yet. Part of the reason is that for most of our ICM users, they are not using the RTK method. I hope it will be available some day as ICMOne brings SWMM5 to the ICM platform.

For ICM, we do have a scripting API that can be utilized for automation. Here is an example for one of my clients. It is a very simple exercise, we need to size the pump correctly so that there is no overflow.

![](images\1_Qr-cbmd9GVWRHVfM_w8Rzg.png)

Running this script will create 50 new scenarios, run all of them, and tally the results in a excel spreadsheet, with just one click.

![](images\1_A3_QlRYzYqIDCZp5ZI2wig.png)![](images\1_Jba9iDWF1kxGl2AvwfcYlg.png)

And here is the winning solution picked from the spreadsheet. So as we are talking, the script does all that for us.

![](images\1_W2T4GKbEhsCBxvNHlxWyVw.png)

**Mel:** that is awesome! One thing I want to add is that there is no magic bullet for calibration. There is no tool that can get the model automatically calibrated for you. Due to the complexity involved in building a model, you will not always be able to calibrate the model within the desired accuracy. When that happens, you as the modeler need to decide how good is good, and how bad is bad until you see it. Think about it, if you cannot even define what a good calibration is, how can a tool get it done. Also in the big scheme of things, spending 2 hours versus spending 2 days calibrating a model doesn’t make too big a difference for the life cycle of a model.

**Mel:** Here is another question Nathan I think you can answer. “**Are there any suggestions on how we should manage modeling files?**”

**Nathan:** As Mel mentioned modelers can be the kind of people with messy desks. So you can imagine what will happen to our modeling files, it can be a real challenge to find the right modeling files one year after the project is completed.

![](images\1_IZ4ZbQV-SKiDacQ_rqS25Q.png)

**Nathan:** With ICM we have this multi-user system where we can store models in a centralized database, and having multiple people working on it at the same time. And this approach solved many of the challenges using file based systems.

![](images\1_T_BVPhbGSgustBzSBtMcOw.png)

**Nathan:** Here is another question “**what is the difference between ICM/ICMOne for the database?**”

For ICMOne you can still use the centralized database, but you can only have one person connected to the server at any time. Also you cannot run remote simulation.

Also I would recommend using data flag.

![](images\1_WKizcjjr8JcTIq2lDHmrlQ.png)

At the end of the talk, Nathan run a poll to get some idea on future topics.

![](images\1_Sc0K96sj6omtLwvgiUbpig.png)

That’s our first Water Talks on Sanitary Sewer Best Practices. Our interview session got a little bit too long and we didn’t find enough time to answer all the questions. Stay tuned, join our next talk!

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 4, 2020](https://medium.com/p/1a69abc66598).

[Canonical link](https://medium.com/@mel-meng-pe/water-talks-sanitary-sewer-modeling-best-practices-part-1-1a69abc66598)

Exported from [Medium](https://medium.com) on March 18, 2025.