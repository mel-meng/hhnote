# SCS Hydrology in InfoWorks ICM— Part 3

In part 1 we covered the basics of SCS hydrology (CN method and SCS UH), and in part 2 we showed how to set it up in XPSWMM and HEC-RAS. In…

---

### SCS Hydrology in InfoWorks ICM— Part 3

In [part 1](https://mel-meng-pe.medium.com/scs-hydrology-method-part-1-44d6825d7599) we covered the basics of SCS hydrology (CN method and SCS UH), and in [part 2](https://mel-meng-pe.medium.com/scs-hydrology-xpswmm-vs-hec-hms-part-2-914bbc65861f) we showed how to set it up in XPSWMM and HEC-RAS. In this post we’ll go through the steps of setting up SCS hydrology in an InfoWorks ICM network.

### InfoWorks ICM subcatchment

InfoWorks manages land cover input parameters in a hierarchical manner. At the most detailed level, it is runoff surface, which defines most of the hydrology parameters such as how to calculate rainfall losses, and routing the flow.

![](images\1_U0EYyK_MaDvTOtRzu16xUg.png)

InfoWorks ICM Subcatchment Land Cover Management

Next, the runoff surfaces are grouped into land uses such as residential and industrial with typical pervious and impervious areas.

At last, the land use can be assigned to a subcatchment where the percentage of each runoff surface can be adjusted.

### SCS Parameters Cheat Sheet

Since each subcatchment has only one CN number, you cannot separate areas with different CN values as separate runoff surfaces. If the CN values varies greatly among these areas, a weighted Q approach should be used, refer to part 1 for more details. If the CN values are close, calculate the weighted composite CN for the subcatchment, and model the whole area as a single runoff surface.

As shown below, there are many input parameters, you only need to populate the highlighted attributes to use SCS methods.

![](images\1_7aw4Phl6-9LEh5LOm_q6xw.png)

### XPSWMM vs InfoWorks ICM

InfoWorks ICM doesn’t support the parameter of “impervious percentage” found in XPSWMM.

![](images\1_0FkN1HXLUDloAQTDzhgH7Q.png)

XPSWMM Impervious percentage attribute

To get the same results in ICM, a composite CN value should be calculated.

CN\_comp = [CN\*(100-imp%)+98\*imp%]/100

Since ICM can only have one CN value for each subcatchment, for node in XPSWMM with multiple catchments, two subcatchments should be created.

![](images\1_DfleBMbCB_j5lYXaCg78cA.png)

As the figures below show, ICM produces very similar results as HECHMS, XPSWMM and SSA for both scenarios,

* subcatcment with one composite CN value
* two subcatchments with different CN value

![](images\1_X9ZYF6yEN-BY77OeJWQYKQ.png)![](images\1_02EhDasLPJBZs_asQzMZcg.png)

### Conclusion

We showed how to enter SCS hydrology parameters in InfoWorks ICM, then explained how to setup ICM using typical XPSWMM SCS model parameters, and at last we compared the results and confirmed ICM produces very similar results. By following these steps, you can effectively use SCS hydrology in InfoWorks ICM for your stormwater management projects.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [February 23, 2023](https://medium.com/p/3e7324fc4266).

[Canonical link](https://medium.com/@mel-meng-pe/scs-hydrology-in-infoworks-icm-part-3-3e7324fc4266)

Exported from [Medium](https://medium.com) on March 18, 2025.