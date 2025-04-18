# WaterTalks - Calibration Tools Part 1

Many thanks to Nathan for inviting me for the WaterTalks sharing my calibration stories. I will summarize our talk in two parts, part 1…

---

### WaterTalks - Calibration Tools Part 1

Many thanks to Nathan for inviting me for the WaterTalks sharing my calibration stories. I will summarize our talk in two parts, part 1 focuses on the tools available for model calibration, and [part 2](https://medium.com/@mel.meng.pe/watertalks-calibration-tools-part-2-a5cda12456ce) is the Q & A session.

Nathan started by an overview of the various tools involved in building a water model and then get it calibrated.

![](images\1_eCCbtr-bcw_Oxb_X08Ebcw.png)

Info360 has the capability to prepare modeling input directly from real-time data, the diurnal curve, pump curve, pump controls and loading data for calibration.

![](images\1_lOhNldjG1igWn0BlEEJ7Lw.png)

For updating demands in real-time, we need to do the patterns a little bit differently. Since we are going to push the diurnal patterns from Info360 to the model, we’ll need to make the pattern using absolute values at the flow meter, and then distribute it spatially.

![](images\1_ctgVxvpLXVduRnfe1bgc7w.png)

We can compare the pump performance in real time against the modeled curves.

![](images\1_oBGIYV6e1Up6g7gkXpA9bA.png)

We can also use the actual pump on/off data to update the model with the control pattern.

![](images\1_uzJH1stjJLcO0lKzAuXMiA.png)

Finally, calibration with real-time data.

![](images\1_2eVv0fBtSCbICFgYb7SMCg.png)

Here is a summary of other tools we have,

* InfoWater Calibrator uses genetic algorithm to calibrate the pipe roughness
* InfoSWMM Calibrator works in similar matter
* InfoSWMM RDII Analyst helps modeler using the RTK method to extract the dry weather and RDII components of the flow data, then using the genetic algorithm to fit the RTK parameters

![](images\1_EvaL4vsZLFzAV5-hqWz1_Q.png)![](images\1_QgwKYMMOkLslcBLw_vRUuA.png)

InfoWater Pro Live Data Adapter can connect to SCADA database

![](images\1_bxKeWG9-nzbJ073kYLyXbA.png)

ICM TSDB can connect to a wide range of data source, then directly feed the data into the model

![](images\1_nAg5kxOpxAQAHL93e_imWg.png)

ICM now supports ADS Prism Data Connection

For more advanced applications, Nathan showed a sample script using ICM Exchange. With the following ruby script, hundreds of scenarios were created with different ground water model calibration parameters, then the results were compared to calibration data to narrow down the parameters with the best calibration results.

![](images\1_CmEQaCQ3pAG7eDI3Hq7xLg.png)![](images\1_7MN28oYMR6akREBQQx-Opg.png)![](images\1_n6fS2Vq4Dr0MFc-Y0uX81w.png)

With similar techniques, one of our clients was able to build a fully automated process of building network from latest GIS, calibrating with latest data and publishing a water model every night. You can find more information about that in the link [here](https://www.innovyze.com/media/4050/luca-serena-innovyze-anglian-water-the-journey-to-integrating-hydraulic-models-to-their-data-sources.pdf).

![](images\1_viBHc04kzVSW7NQx6DRrdQ.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 9, 2020](https://medium.com/p/e9e5bf5b364d).

[Canonical link](https://medium.com/@mel-meng-pe/watertalks-calibration-tools-part-1-e9e5bf5b364d)

Exported from [Medium](https://medium.com) on March 18, 2025.