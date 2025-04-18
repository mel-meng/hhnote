# How to load external flow from interface file in XPSWMM

What is an interface file in XPSWMM? It is just a binary file that stores a bunch of time series, it could be flow and pollutants…

---

### How to load external flow from interface file in XPSWMM

What is an interface file in XPSWMM? It is just a binary file that stores a bunch of time series, it could be flow and pollutants, temperature, evaporation and wind, etc. The reason a binary format is used is because it is much smaller than a text file.

Why do we need an interface file? We need an interface file for two reasons in the swmm3/4 days of the 80s and 90s when computer was not powerful enough for hydraulic simulations,

* not enough memory to hold all all the data, and the CPU was not powerful enough to crunch all the numbers
* not enough storage to save all the results on the disk

To deal with limited computing resources, we had to divide the problem into smaller pieces. Instead of calculating the runoff from the rainfall and then route the flow through the pipes simultaneously, let’s calculate only the runoff from the rainfall and save the results of the runoff. After that we can route the runoff through the network using the hydraulic engine, in this manner, the computer doesn’t need to keep track all the hydrology and hydraulics variables in the memory, and only need to do one type of the calculation.

The binary format makes a lot of sense because it can greatly reduce the file sizes, at a time when the most common storage was the the floppy disk with just a few MB storage, every KB matters.

Fast forward to today, neither makes too much sense. The computer is fast enough to run both hydrology and hydraulics at the same time, we no longer need to divide the simulation into two steps with an interface file. File storage is not longer a concern, external time series stored in a text format is much easier to work with than the binary format. Therefore, in most cases, interface file shouldn’t be the first choice as an input and exchange time series format.

However, XPSWMM does have some limitation on the number of rows a text file time series can have, and in this case, an interface file is the only option to load a very long time series.

Here is an example of encoding flows into an interface file. You can find the model and data on [Github](https://github.com/mel-meng/xpswmm/tree/master/models/interface_writer). The write interface tool can convert flow and pollutant time series into interface files.

1. launch the write interface file tool

![](images\1_pj1q4T2vO2l7HCYf6PhRmA.png)

2. setup the conversion settings as shown below,

![](images\1_zerwzNBhnfa_iolytoQfsQ.png)

3. Setup the interface file for flow routing

![](images\1_fxRokwEeRxmdSTYR6kKcgw.png)![](images\1__Y9GBcYmbALFPEaS-ewtBw.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 22, 2020](https://medium.com/p/85090539d2d6).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-load-external-flow-from-interface-file-in-xpswmm-85090539d2d6)

Exported from [Medium](https://medium.com) on March 18, 2025.