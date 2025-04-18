# SCS Hydrology XPSWMM vs HEC-HMS — Part 2

In part 1, we reviewed the basic ideas behind SCS hydrology method. In this post, we will setup a model in both XPSWMM and HEC-HMS.

---

### SCS Hydrology XPSWMM vs HEC-HMS — Part 2

[Part 1](https://mel-meng-pe.medium.com/scs-hydrology-method-part-1-44d6825d7599), [Part2](https://mel-meng-pe.medium.com/scs-hydrology-xpswmm-vs-hec-hms-part-2-914bbc65861f), [Part 3](https://mel-meng-pe.medium.com/scs-hydrology-in-infoworks-icm-part-3-3e7324fc4266)

In part 1, we reviewed the basic ideas behind SCS hydrology method. In this post, we will setup a model in both XPSWMM and HEC-HMS.

### XPSWMM

In XSWMM, for each subcatchment, you enter the following,

· Area

· Imp (%)

· Shape factor

· Initial abstraction

· CN

· Time of concentration

![](images\1_rIeLfjQmExtl7PK7odnyew.png)

“Width” and “slope” are not used for SCS hydrology.

When impervious (“Imp. (%)”) is entered, XPSWMM will calculate an area weighted composite CN using 98 for impervious areas. See the figure below for the comparison.

· CN50Imp50\_Split — combined flow from two subbasins one is CN=50 Imp=0%, and another CN=98, Imp=100%, this is the weighted Q method

· CN50IMP50TC8 — One subbasin CN=50, Imp=50%, Tc=8min

· CN74IMP0CT8 — composite CN for CN=50, Imp=50%, Tc=8min assuming CN=98 for impervious, composite CN=50\*.5+98\*.5=74, Imp%=0

As the results shown below,

· CN50IMP50TC8 and CN74IMP0TC8 are the same

· CN50Imp50\_Split has a much higher peak

![](images\1_k-AjJ72KXX-C9ldUpcrL6w.png)

According to National Engineering Handbook, when having impervious area, a weighted Q method is preferred. This can be done using the split tool.

![](images\1_cHZZPESbHbLEXCCJ0_SCLQ.png)

As shown below, the tool split the old subcatchment 1 into 2, and 3

· 2 is 50% of 1, and it is the pervious part

· 3 is 50% of 1, and it is the impervious part

![](images\1_DRsiRvTkBuuYzR_19tzlxg.png)

As shown below, with the split, a higher peak is simulated.

![](images\1_jXBsOjsxJ-2PWRDq7HHZ5w.png)

### HEC-HMS

HEC-HMS is widely used in the United States, and it support SCS hydrology.

HEC-HMS takes the following parameters,

· Area

· CN

· Impervious (%)

· Shape Factor

· Lag Time: it is important to notice that it is not Time of Concentration. Lag time = 0.6\*Tc

· Leaving the initial abstraction blank will use the default Ia=0.2\*S.

![](images\1_MnHvcBrEDLc298T7c-slmQ.png)

[**HECHMS**](https://www.hec.usace.army.mil/confluence/hmsdocs/hmsum/4.10/subbasin-elements/selecting-a-loss-method#id-.SelectingaLossMethodv4.10-SCSCurveNumberLoss) implements impervious area differently from XPSWMM, instead of calculating a composite CN, the impervious area is calculated as a separate area without any losses of rainfall.

> The **Percentage of the Subbasin Which is Directly Connected Impervious Area** can be specified. Any percentage specified should not be included in computing the composite curve number. No loss calculations are carried out on the impervious area; all precipitation on that portion of the subbasin becomes excess precipitation and subject to direct runoff.

For impervious area, HEC-HMS directly routes the rainfall using the SCS Unit Hydrograph. The results are shown below,

· CN98 — pervious area with CN=98 Imp%=0

· CN50Imp100–100% impervious area, CN number is not used

CN98 shows some loss at the very beginning, but after that the results are almost identical. It should be noted that you cannot enter a CN number larger than 98 in XPSWMM (you can use the configuration keywords of [CN-x](https://help.innovyze.com/display/xps/Configuration+Keywords#ConfigurationKeywords-C) to increase the impervious CN to 99).

![](images\1_RmzKaVT_oOcj0PTSBfs_jg.png)

When the imp% is greater than 0, HECHMS will route the previous and impervious as separate subcatchements instead of calculating a composite CN.

· CN50Imp50\_Split — combined flow from two subbasins one is CN=50 Imp=0%, and another Imp=100%

· CN50Imp50 — One subbasin CN=50, Imp=50%

· CN74Imp0 — composite CN for CN=50, Imp=50% assuming CN=98 for impervious

As the results shown below,

· CN50Imp50\_Split and CN50Imp50 are the same

· CN74Imp0 has a much lower peak

![](images\1_gHc0CZtTQhmFvFQ3sH-y0A.png)

### Compare Results

### HECHMS vs XPSWMM

Due to the difference in the SCS implementation in HECHMS and XPSWMM,

· When the impervious percentage is greater than 0, HECHMS treated the pervious and impervious as two different subcatchments, therefore, it is equivalent to the split option in XPSWMM.

· When impervious percentage is 0, it should produce the same results

The comparison is shown below,

· CN=74, Imp=0%, comparable results (2% peak flow)

· CN=50, Imp=50%, modeled as two separated subcatchments, comparable results (1% peak flow, however the average is around 10%, due to the fact HEHMS has no loss for impervious area.)

![](images\1_XowZ5FKN1RMZwC1OCdJA7w.png)![](images\1_QnV7ddE9d0EEa8bsVbUxqw.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [February 8, 2023](https://medium.com/p/914bbc65861f).

[Canonical link](https://medium.com/@mel-meng-pe/scs-hydrology-xpswmm-vs-hec-hms-part-2-914bbc65861f)

Exported from [Medium](https://medium.com) on March 18, 2025.