# How to get detailed simulation information for river reaches in XPSWM

source: Innovyze Support Portal

---

### How to get detailed simulation information for river reaches in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-get-detailed-simulation-information-for-river-reaches-in-XPSWM)

XPSWMM has a few “secret” tools for advanced users who really need to look under the hood to see how the engine does its calculations. In this article, we’ll show a few tips for getting very detailed information about river reaches geometry, hydraulic characteristics, and simulation results.

### 1D Log

1D log has lots of detailed information for each river reach in the model. You can find the geometry summary with length, max. areas.

![](images\1_gRyDUm0fPbJjiYyVCxFzaQ.png)

In Table E15, you can find the water volume.

![](images\1_91Ui9nhfqBAeMOb3bF3sXA.png)

In Table E14, detailed channel summary

![](images\1_-uElb9hcFFIX0KYWO4RySQ.png)

In table Conduit Volume, you can find the total volume of all the pipes in the model.

![](images\1_qtWHcOBTeTFht1qBCZyNFA.png)

### Conveyance Curve

To get detailed conveyance curve for each channel, check the “Echo Natural Section Data”. Then you will find the data in the 1D log.

![](images\1_-82P5gBas3YHQAzbNZqaHg.png)

The conveyance curve used for routing flow through each river reach is printed in the 1D log as shown below.

![](images\1_oOEPnqBzXzuGB5eTwnd85A.png)

### Flow Details for river reaches

To print the details of the river reach simulation results, check the “Print Flow Details” for each river reach,

![](images\1_W-IJ4L4W5RgTFMQsku0GKQ.png)

Then in the output control, we can specify how often to print out the details.

![](images\1_SUUhF3PCNxcx3VyeNONl1g.png)

In the 1D log, detailed flow condition for the selected river reach is printed.

![](images\1_P9JG8rrL-nh4kipGp_iH-w.png)

### Export the results into a CSV file

use the configuration parameter EXTERNAL\_CSV to direct the results to a csv file instead of the output file.

![](images\1_5DkYz_5Ag39vIpEX9zQ0Fg.png)

The detailed flow information will be directed to a csv file in the 1D results folder,

![](images\1_Vf3dgPZI8d1HtVbPyi-Aug.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [March 29, 2021](https://medium.com/p/f7c4e828c5ea).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-get-detailed-simulation-information-for-river-reaches-in-xpswm-f7c4e828c5ea)

Exported from [Medium](https://medium.com) on March 18, 2025.