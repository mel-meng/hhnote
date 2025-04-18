# Culvert Design Theory

Planning software such as SWMM5, XPSWMM, InfoWorks ICM are great for modeling complicated system, with enough calibration data, we can…

---

### Culvert Design Theory

Planning software such as SWMM5, XPSWMM, InfoWorks ICM are great for modeling complicated system, with enough calibration data, we can build models that can predict the system performance with high confidence. The critical part of this process is calibrating key parameters.

However, when it comes to design problems or modeling systems without good calibration data, modelers can no long calibrate the model using observed data. For such situations, a responsible modeler will review established engineering publications and build simpler models to verify the more complicated models.

Culvert design is a great example, [FWHA HDS5](https://www.fhwa.dot.gov/engineering/hydraulics/pubs/12026/hif12026.pdf) is a great resource for sizing culvert with detailed background information on the theory and procedures.

With the help of the [HY-8 Culvert Hydraulic Analysis Program](https://www.fhwa.dot.gov/engineering/hydraulics/software/hy8/), a modeler can quickly get the performance curve, which can then be used as a “calibration” source when building more complicated models.

Another great source of culvert design is HECRAS, and the [reference manual](https://www.hec.usace.army.mil/software/hec-ras/documentation/HEC-RAS%205.0%20Reference%20Manual.pdf) has good information on how RAS implements and improves the FHWA method.

### Inlet Control vs Outlet Control

The theory is quite complicated, and the good news is that I don’t need to know the details for most design problems because I can rely on HY8 and HECRAS for quick calculations.

It does help to have some basic understand of inlet and outlet control.

### Inlet control

Inlet control is when the inlet is limiting the flow that can pass through the culvert, so downstream condition doesn’t matter. In this case, empirical equations were developed to calculate the headwater depth. As shown blow, typically the inlet works as an weir or orifice and supercritical flow develops inside the culvert.

![](images\1_AccDKuqBrqJM5b3_5_8IFw.png)![](images\1_4wC_rQUnbhNhTaqoSLtNdw.png)

### Outlet Control

Outlet control is more complicated, both upstream and downstream conditions matters. And it is usually calculated using energy equations. And for SWMM5, it relies on the SWMM unsteady state engine to figure out the headwater depth.

![](images\1_FabteplqZyZ0v0TZTTUUAA.png)![](images\1_zibou2laFtlfckcYvPpwYQ.png)

### Design Problem

HDS5 has the following example,

![](images\1_1q4wK_57qb27M7jVapi7EA.png)

The results,

**54" RCP El hi=108.0ft, V0=15.3ft/s**

Let’s go through that using the nomograph, HY8 and SWMM5

### HY-8

Example: 54" RCP El hi=108.0ft, V0=15.3ft/s

HY-8: El=108.61ft, v0=14.88 ft/s, within 1% difference.

The model is saved to : **./data/hy8/hds5\_example.hy8**

![](images\1_Fjj3OLr57VT-pxhd3y5ZHA.png)![](images\1_DmMiDHgABnBKYdd3XjsR4w.png)

### Nomogrpah

For concrete pipes we’ll use Nomographs chart 1B for inlet control, and chart 5B for outlet control.

Inlet control:

El = 4.5\*2.5=8.8ft

![](images\1_8TWWw1p_vIgj-OKDY01C5g.png)

For outlet control, the reading is the difference between headwater and tailwater, so I got 5ft from the nomograph, and the tailwater is about 3.5ft, which makes the headwater 5+3.5=8.5ft, very close to the 8.2 I got from HY8.

![](images\1_zO-iGDO4t6XAzYefAM3HMw.png)

### Performance Curve

HY8 gives the performance curve for the culvert. The table is saved to **./data/hy8/dg131\_performance\_curve.csv**

* For 0–30 cfs it is outlet control
* for >30cfs it is inlet control
* The difference between inlet/outlet control is around 1.6ft > 100 cfs

When using other models, I am expecting a deviation around 10% of HW (measured from face invert) should be considered a good match(HSD5 states 10% error of the culvert calculations).

![](images\1_GCyeHLEMfyg3_OKuo4tBJQ.png)

Profile in HY8, it shows the profile decreases to the critical depth at the entrance.

![](images\1_s_ZkmkB1DIXw-exX1BG23Q.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 29, 2021](https://medium.com/p/99965aa4efac).

[Canonical link](https://medium.com/@mel-meng-pe/culvert-design-theory-99965aa4efac)

Exported from [Medium](https://medium.com) on March 18, 2025.