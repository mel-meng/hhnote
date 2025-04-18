# Why do you need ensemble Analysis?

For me the worst feeling of being an engineer is this, if I did something wrong with the design of the drainage system, someone can get…

---

### Why do you need ensemble Analysis?

![](images\0_BBRm0lhIZvUOskIa)

For me the worst feeling of being an engineer is this, if I did something wrong with the design of the drainage system, someone can get hurt or even killed. Every time when that crossed my mind, I’ll ask myself what can I do to be sure that won’t happen?

Since nobody can predict the future, the best we can do is to look back and say if the future will be similar to the past, we can answer a different question, will this design keep us safe in the past?

Say if we have all the rainfall data from the past, then we can run a model for the past 1000 years, and then we can say, OK based on the past 1000yrs of simulation, the system failed 15 times, does that sound safe enough?

That is what in theory we can do, in practice, usually we don’t have that much data, and a computer that can run such a model in reasonable time. Also, it will take a lot of time to analyze the results.

The alternative is using design storms developed from historical events. Design storms such as the Atlas 14 are developed using statistical models and methods to generate rainfall profiles representative to each region using historical rainfall records. Instead of running models with hundreds of years of rainfall data, we can run a handful of design storms to represent a range of possible rainfalls to get an idea on how the system will behave over the next 50 and 100 years.

This may sound like a strange idea to you if you are familiar with design methods using steady state methods such as the rational method, or the SCS method. Such methods are generally quite conservative, it has a fairly big safety factor built into the methods and therefore, a more detailed statistical analysis of the risks is not needed(I’ll provide more details in following posts).

However, for challenging design situations where we cannot afford to build a system with such conservative safety factors due to cost and physical constraints, the chances of system failure is a lot more likely, and therefore, statistical methods are often used to evaluate the risks of a tight design.

[Statistical ensemble](https://en.wikipedia.org/wiki/Statistical_ensemble_%28mathematical_physics%29) helps the modeler get a feel of the possible output of the model as the rainfall changes, thus helping the modeler to be more certain about the uncertainty of the design. As shown in the figure, instead of running a single model, we run a group of models with possible rainfall to estimate the range of the peak flow of the system for 1 percent storms (100yr) with the duration of 1hr, 2hr and 3hrs, and we can plot the results as box plot to show the range of possible results.

In the next post, I’ll cover how Atlas 14 is developed and why using a group of rainfall will give us much better idea of the risks involved than a single run.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 28, 2021](https://medium.com/p/cba0ee0a22a3).

[Canonical link](https://medium.com/@mel-meng-pe/why-do-you-need-ensemble-analysis-cba0ee0a22a3)

Exported from [Medium](https://medium.com) on March 18, 2025.