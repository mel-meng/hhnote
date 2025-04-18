# How to add rainfall to ICM using TSDB ? — Part 1

Source: Innovyze Support Portal

---

### How to add rainfall to ICM using TSDB ? — Part 1

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-add-rainfall-to-ICM-using-TSDB)

TSDB (time series database) provides a streamlined workflow for getting real-time data into ICM models. It can greatly reduce the time needed to run a model with real-time data from external sources by automating the data connection, retrieval, conversion and validation.

In this article we’ll focus on the commonly used methods to connect rainfall sources to ICM. We will cover the following 3 scenarios,

1. Bring existing calibration rainfall data into ICM
2. Bring new rainfall data sources into ICM
3. Bring spatial rainfall into ICM

### Bring existing rainfall data into ICM

As shown below, we have an existing model using a rainfall event. And we would like to turn this into a TSDB.

![](images\1_nYvItIqolrWRX7nwF31JfA.png)

ICM has built-in tool to import event files into a TSDB and creates tvd connectors in the network.

1. create a new TSDB
2. create a new scenario called “with\_tsdb”
3. drag the TSDB into the Geoplan, you should see “scalar\_tsdb [Target])”showing in the title bar.

![](images\1_LrGhVhnLqcwATg4hKr5FJA.png)

Then call for the import tool,

![](images\1_m8Ie37131rsRfU99C4w-mw.png)![](images\1_8QwWAOfv8tljpZqCJySIPw.png)

Now check the TVD connectors created,

![](images\1_6JIlpEbgPFWlr4BA42w0pg.png)![](images\1_WbzVxqU6wgQ66VK3QSPCcA.png)![](images\1_UKIve-UnSpD3P2sej4pQqw.png)

The import tool did the following,

1. import the rainfall into the TSDB
2. created TVD connector reading the rainfall from the TSDB
3. making sure the TVD connector name matches the rainfall profile name

![](images\1_EHyfQWdEVICjBL6Py54d9A.png)

Now we can rerun the model, the only difference is that we need to turn on “Use TSDB” and drag the TSDB into the box.

![](images\1_ivKV0oxgPGnGZJu18xRfhw.png)

and it shows the same results.

![](images\1_ivKV0oxgPGnGZJu18xRfhw.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 7, 2021](https://medium.com/p/d385645d66d).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-add-rainfall-to-icm-using-tsdb-part-1-d385645d66d)

Exported from [Medium](https://medium.com) on March 18, 2025.