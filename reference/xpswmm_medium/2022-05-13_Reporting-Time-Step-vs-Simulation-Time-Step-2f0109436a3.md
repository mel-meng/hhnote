# Reporting Time Step vs Simulation Time Step

source: Innovyze Support Portal

---

### Reporting Time Step vs Simulation Time Step

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Reporting-Time-Step-vs-Simulation-Time-Step)

If you are new to modeling, very quickly you’ll find the peak flow can be different in your graph and your model results summary. How can that be, which one is correct?

The difference lies in how the peak flow is calculated. The engine keeps track of peak flow for each pipe for every calculation it does, and report the values in the model summary log. While plotting the results, the peak flow is calculated from the reported values.

To illustrate the difference, we created a very simple model. Let’s load a hydrograph at Node 1, and let it flow through this pipe.

![](images\1_rQgEQQJcEC-mJIk05ZQzHw.png)

For the same model, if I use different reporting time step of,

* Base 20 min
* 5min: 5 min
* 1min: 1 min

![](images\1_B0RRz5IObebq5IzA0rkWJA.png)

I will get the following flows from the same pipe.

![](images\1_fDvPiekM-UZwKW08k5hV1w.png)

Because the simulation time step is 120 sec, when reporting every minute, I will almost get the same results from all simulation steps (XPSWMM will adjust the timestep if needed, it can go under the 120 sec.)

When reporting every 5 minutes, it looks almost the same, but when reporting every 20 minutes, we missed the critical part of the flow.

Another thing to notice is the reported peak flow in the graph is different for each scenario, it is from the reported data directly.

If you check the XPTables, which reports the true peak flow the engine reported which tracks every time step, they are all the same for the 3 scenarios.

![](images\1_QHTgxgpj8EyU-aOexbqe1A.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 13, 2022](https://medium.com/p/2f0109436a3).

[Canonical link](https://medium.com/@mel-meng-pe/reporting-time-step-vs-simulation-time-step-2f0109436a3)

Exported from [Medium](https://medium.com) on March 18, 2025.