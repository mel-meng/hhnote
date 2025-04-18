# Break large long pipes in SWMM

source: Innovyze Support Portal

---

### Break large long pipes in SWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Break-large-long-pipes-in-SWMM)

When modeling very large pipes, make sure to break them into segments of a few hundred feet, otherwise, SWMM won’t be able to get the correct results.

The SWMM engine assumes the flow rate is the same within each pipe, and we assume a straight water profile when solving the equations, an assumption probably is wrong for a 1200ft pipe with a 5-ft diameter. As the example below shows, when modeled as 4 segments, the water profile is not a straight line.

![](images\1_uSDdP-ZmV2C1GiLJrwtl8Q.png)

While modeling it as a single pipe, you will not be able to know the actual profile within the pipe, and it will also give strange if not wrong results.

If we compare the stage of Node1 and Node1\_Long\_pipe, the starting node for both scenarios, the results are very similar.

![](images\1_Ww-NMVHzRerOeI3e3zHykw.png)

However, if we check the 1D log in table E18, Node1-Long\_Pipe has a remaining volume (the volume of water in the node at the end of the simulation) is almost 10 times as Node 1. A sign that there is an error introduced when solving for that pipe.

![](images\1_tdjSkem0uzAa0Fq8XGEy_g.png)

In summary, you should break you pipes into segments of only a few hundred feet, especially for large diameter pipes in SWMM.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [March 19, 2022](https://medium.com/p/d2297572cde5).

[Canonical link](https://medium.com/@mel-meng-pe/break-large-long-pipes-in-swmm-d2297572cde5)

Exported from [Medium](https://medium.com) on March 18, 2025.