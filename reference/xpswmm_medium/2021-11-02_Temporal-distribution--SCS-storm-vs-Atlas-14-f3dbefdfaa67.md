# Temporal distribution: SCS storm vs Atlas 14

When I first learned about ensemble storms and its benefits, I was wondering did I do all my models wrong in the past. Why did I use only a…

---

### Temporal distribution: SCS storm vs Atlas 14

When I first learned about ensemble storms and its benefits, I was wondering did I do all my models wrong in the past. Why did I use only a single design storm for my past designs?

Then I learned that when using synthetic design storm such as SCS Type II, you don’t need to use ensemble.

Here are the key points of how the SCS design storm works, refer to Jimmy’s blog [post](https://rashms.com/blog/nrcs-rainfall-distributions-based-on-noaa-atlas-14-precipitation-depth-and-duration/) for more details.

* The Atlas 14 temporal distribution is developed from real storms, by grouping recorded rainfall events into different categories, and then applying the statistical methods to derive the temporal distribution to account for a wide range of possible storms.
* SCS temporal distribution is a synthetic storm distribution, which aims to generate a perfect storm, say for a 10 year storm, during the 24hr period of this storm , you’ll experience not only a 24hr 10yr storm, but also a 5min 10yr storm, 1hr 10yr storm, etc. The peak depth for each of the duration from 5min to 24hr will match the values listed in Atlas 14 PFD table for a 10 year storm.
* The reasoning behind this is that it is believed the peak discharge of a watershed is determined primarily by rain falling in a duration equal to the watershed time of concentration. By nesting peak rainfall for all the different duration at the center of the design storm, we can be sure the watersheds of all different sizes within the model will reach peak discharge at about the same time, and therefore, it will give us the worse possible scenario when sizing a project.

In reality, we will rarely have storms like the SCS distribution. Therefore, using a SCS temporal distribution will result in an oversized design that will be very safe. However, for many applications, oversizing is simply not possible, for example, how do we address flooding issues in a developed neighborhood, knocking out many homes to build a big pond will be a tough sell; helping a farmer to deal with flooding issues in his fields, safety might not be the most important factor to consider.

In such situations, designing with storms similar to historical events can have significant impacts on the sizing of the project. With ensemble analysis, we can be more confident of the possible risks.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [November 2, 2021](https://medium.com/p/f3dbefdfaa67).

[Canonical link](https://medium.com/@mel-meng-pe/temporal-distribution-scs-storm-vs-atlas-14-f3dbefdfaa67)

Exported from [Medium](https://medium.com) on March 18, 2025.