# Roadway overtopping in XPSWMM

source: Innovyze Support Portal

---

### Roadway overtopping in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Roadway-overtopping-in-XPSWMM)

![](images\1_lxH7v6DrJ0YHe4GG_iN9GA.png)

The flow overtopping a roadway is modeled as a [weir](https://help.innovyze.com/display/xps/Broad-crested+Weir+Coefficients) in XPSWMM. The corresponding parameters are shown below.

* weir length: the section of road where flow will overtop
* weir crown: it is the max WSEL for the bridge, it should be set high enough so that no orifice flow will occur, refer to [help](https://help.innovyze.com/display/xps/Links#Links-BridgeLink) for more information.
* weir coefficient: a constant can be entered, or XPSWMM can use the FWHA chart to determine.

![](images\1_TW8OkaCm9PL-ihs6g2PhFQ.png)![](images\1_f676Ghv-yMdCy_UF-crkiQ.png)

To illustrate the impact of the “max. WSEL” on the results, a sample model is created. The model can be found on [Github](https://github.com/mel-meng/xpswmm/tree/master/models/bridge_weir). There are two identical river models below, the only difference is the max WSEL were set at 980 and 990. So when water level is overtopping the bridge, the max WSEL =980 option will switch to an orifice equation when the water is higher than 980 over the bridge.

![](images\1_ycioMLNb7nKstI08JAfNyQ.png)

The flow over the roadway as weir is compared below. The dashed lines are depth and using the right axis, and flows are solid lines.

As shown below, before the depth raises above the 980, the two models behave exactly the same.

The flow is through the opening from 0 -4:30am, from 4:30 the road is overtopping, and at around 6:30am it reaches 980ft, and the model starts to diverge. With a max WSEL of 980, the 980 option switches to an orifice equation and allows less flow through as shown in the orange flow line. The 990 option continues to use the weir equation and the flow is higher and level is lower as the grey solid line and yellow dashed line shows.

![](images\1_KJVxCPdC3pNbzw3ve9Hm6A.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 23, 2020](https://medium.com/p/290ecf7e404a).

[Canonical link](https://medium.com/@mel-meng-pe/roadway-overtopping-in-xpswmm-290ecf7e404a)

Exported from [Medium](https://medium.com) on March 18, 2025.