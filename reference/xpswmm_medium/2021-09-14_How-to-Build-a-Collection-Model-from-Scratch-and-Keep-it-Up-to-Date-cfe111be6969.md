# How to Build a Collection Model from Scratch and Keep it Up to Date

Many thanks to the opportunity of sharing my experiences of building collection model at the Water Talks today (9/14/2021) with Ryan Brown…

---

### How to Build a Collection Model from Scratch and Keep it Up to Date

Many thanks to the opportunity of sharing my experiences of building collection model at the Water Talks today (9/14/2021) with Ryan Brown. Here is a summary of the talk.

### Life Cycle of a Model

The life cycle of a model always starts with a problem. The owner of the utility or the customers of the utility are experiencing some “pains”, and need to improve the collection system to solve the problem.

So they reach out to a consultant who will assign a junior engineer to build a model and generate some results.

Then a senior engineer will review the results and propose a few recommendations for the utility to consider.

It takes a team to complete the cycle, and it is important to acknowledge that not a single person on the project has the full understanding. It is usually the senior engineer’s job to ensure everyone is on the same page.

The next dimension of this cycle is how many cycles it will take to get the problem solved. For planning projects, every 5 to 10 years there might be a need to update the model and find better solutions to the problem. While for most design project, there is only one cycle and no need to repeat the same process.

![](images\1_vPE5q84XyFd4tgEyuOT-9w.png)

### Typical type of problems

The kind of questions will determine how much values we can get out of a model. Common type of problems using a model include,

Planning Problems (system, 5 years/cycle)

•Identify capacity issues

•Evaluation different solutions

Optimize solutions for cost across the whole system, over several decades

Design Problems (site, 1 cycle)

•Identify conveyance needs

•Size different solutions and compare performances

Operation Problems (here and now, 6months/cycle)

•Predict possible capacity issues

* Identify capacity issues in real-time

Depending on the type of problems, the life cycle of a model can be quite different. The focus of this talk will be on building system model over a long time.

### Building a model from scratch

As shown below, when building a model from scratch, we spent most of time building the model, and very little time performing analysis, the part that gives us values.

![](images\1_NbKQSafYcZ6b3lpo7rG72g.png)

Fortunately, with proper planning and following best practices, updating and keeping a model update to date can look more like an inverted pyramid.

![](images\1_RipPhgg2ggmmBguFXA3UlQ.png)

And that is the main topic of today, how can we invert the pyramid?

### Increase the value of a model while keeping the cost down

By revisiting the life cycle of a model, we can identify the value and the cost. We only achieve values when we learn from the results (reports), everything else is a cost.

![](images\1_fxcrzAXb60tZyRe1H_UCCg.png)

There are a few ways we can increase the value of a model,

* refining the questions: asking the right questions that a model can answer very well
* asking more questions using the same model
* increase the quality of the answers, reducing the uncertainty of the model

When it comes to reduce cost, we need to identify the bottleneck and remove it.

An example is shown below, say for this fictional project we estimate the effort for each tasks. It becomes obvious building and calibrating the model are the bottlenecks.

![](images\1_Ebd05XxoBuy26-66ptGQPg.png)

So we should start by figuring out ways to remove these bottlenecks first. Common traps to watch out,

* Don’t start optimizing something simply because it is easy or interesting. For example, we might be able to greatly improve the analysis task by building automated reporting tools, however, its impact will be quite limited because analysis is not the bottleneck yet.
* Be cautious to roll out complicated customized tools aiming to be used across multiple projects. Maintaining software tools and provide training and support could cost a lot more than developing the tools over long time, without a long term plan, it can be hard to justify the effort.
* There are things that can not be easily automated, need to be realistic about the effort involved and budget the resources accordingly

### Case study: removing network building bottleneck

In the rest of the talk, we’ll use building network as an example to demonstrate the tools and tips for removing the bottleneck. Calibration is another bottleneck, but we will not have time to discuss that in this talk.

General suggestions,

•Look beyond building a single network, build a process that can keep the network up to date.

•Automate the Import/Export process

•Building interactive tools to automate repetitive editing tasks

* Using Versioning & Flags & Scenarios to keep the model up to date

A word about GIS. Ideally we would like to have the GIS flow into the model seamlessly, however, based on my own experiences, it will take some time for us to get there for most utilities. A more practical perspective is to focus on the problems we are trying to solve and try to maximize the value while reducing the cost. It is OK to have a less than perfect data import process between GIS and the model as long as most of it can be automated.

### Commonly used tools for automating the import include,

* using data import wizards which can save the field mappings for repeated updates. This is the most flexible way of updating data in batch, most modeling software has this kind of capability. The modeler might need extra documentation to add extra steps of cleaning up the data after the data is imported.

![](images\1_YMhgGfMsYpS9U5wJli0NpA.png)

* hard code repeated data update process using scripting languages. This depends on how often the data will need to be updated. If you only need to update the data every few years, this is not something will save too much time. However, if you plan to update the data every few months, an investment in hard coding a script might pay itself very quickly.

![](images\1_PGJcWyX9jqlilpVbVbLaPQ.png)

* using out of box routines to fill missing information. For example using the inference tool in ICM to get the rim elevation from group model and using the SQL query to update missing values based on other attributes

![](images\1_JU7bW277D9_1PEQ-iZNiBg.png)![](images\1_KyDTC4qMFdwUCIlvjYL0MA.png)

* Another trick I found quite useful is to break down more complicated data operations into a few SQL queries, which can also server as documentation on the process the first time I did it, usually the queries can be easily modified to reuse the next time I need to do similar updates. As shown in the example below, every time I update my populations in my subcatchments, I also need to update my planning scenarios. So I created two queries for this operation, 100 will select all the subcatchments that I will need to update the population in the base scenario, and 200 will recalculate the populations in other planning scenarios

![](images\1_FKa0o9DjxyP4JcpeJCEecQ.png)

### Interactive Tools

If you are the first to build a model from the GIS data, most likely you’ll spend a lot of time reviewing individual pipes to fill in missing data and fix errors. In these situations, you’ll need to build tools that you’ll use interactively.

Make it easy to see the problems

Instead of going through tables to identify missing values,

1. create a theme to show the problem on the map
2. save the theme and reuse it by simply dragging it to the map

![](images\1_z6X-v3XSVvk34VBejMGu-A.png)

Build simple queries that automate calculations,

1. drag the theme to the map to show missing values
2. use the profile view to check the pipe, we see the only information is missing is the downstream invert
3. drag the query that calculates downstream invert from upstream invert
4. enter the slope, then it is done

![](images\1_yEt0V3_Cv60B3myrZYPbaw.png)

### Versioning/Scenarios/Flags

To keep a model up to date for a long time, you’ll need the right tools. Below are some common issues when continuously updating a model,

•I accidentally deleted a pipe. **Make backups**

•For this proposed section of pipe, we changed the design several times. How did we end up with this design? **Keep a history**

•I totally forgot what I did 6 months ago to this model. Can you check what changes were made to the model then? **View changes**

•I would like to try something I think that might work, but I don’t want to make it in the base model. **Experimenting**

* We have a deadline next Monday, we need have more people working on this model without stepping on someone’s toes? **Collaboration**

### Flags

Flags can be very helpful to track the source of the data and its quality. As shown below, the different color shows the sources of the data. So at a glance the modeler can easily tell how much to trust the data.

* blue(#D): default flag, length is calculated from GIS length
* orange (#GIS): data imported from GIS
* red (#INF): data inferred from ground model
* green (#NG): data edited by Nathan (his initials)

![](images\1_nTrbYd1ErQnVLgcNoLXNwg.png)

The nice thing about the flags are it usually takes only seconds to set them up, however, it will stay with the data forever until next time you change it.

### Versioning

We’ve all seen file names like “final final model…”. When working on a model for a long time, we need a better way to handle the different versions than keep adding “final” to the last file names. ICM has a very clean way of doing this. Every time you save the model a new version will be saved with a comment automatically, and you can easily go back to a previous version with just a few clicks.

As shown below, Matt built the workshop models in ICM, and he saved the model at the end of every workshop. So during the training, I can easily go back to a version matching the students progress without the need of finding an old copy of the model.

![](images\1_52zIjyhAC-oBAmkjqCNCHQ.png)

Versioning also provides detailed tracking of values and flags at object level.

![](images\1_uwJltX09-Ps3jy_dtcI3og.png)

It can also compare different versions of the model if the comments are not detailed enough.

![](images\1_d0It8gZoSPsbzpXpAsC9Sw.png)

### Q & A

**Q: If the GIS doesn’t match the model, any suggestions?**

A: If the goal is to keep the model updated from GIS on a regular basis. It means you didn’t have a plan developed yet on how to automate the import from GIS to the model. In the short term, you can work with your GIS staff on some “hacking” to reconcile the differences. However, in the long run, you should rethink the process, and design something that can be largely automated.

**Q: How often should I update the model?**

A: If you refer to the life cycle diagram. It all starts with a problem. Usually the person who has the problem will have pretty good idea if a new model is needed or not. It could be regulation driven, or by the increasing number of complains of the system capacity. At the end if the cost of building a model is less than the value it can brings, you should update the model. And as we have demonstrated here, there are quite a few things we can do to reduce the cost and increase the values.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 14, 2021](https://medium.com/p/cfe111be6969).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-build-a-collection-model-from-scratch-and-keep-it-up-to-date-cfe111be6969)

Exported from [Medium](https://medium.com) on March 18, 2025.