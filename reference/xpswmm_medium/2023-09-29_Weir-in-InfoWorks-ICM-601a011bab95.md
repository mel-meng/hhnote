# Weir in InfoWorks ICM

source: github

---

### Weir in InfoWorks ICM

source: [github](https://github.com/mel-meng/hhnote/tree/main/hydraulics/weir%20in%20icm)

### [Introduction](https://github.com/mel-meng/hhnote/tree/main/hydraulics/weir%20in%20icm#introduction)

Weir equation is used in various InfoWorks ICM model building scenarios, such as special structures like weirs, orifices, and sluice gates in 1D networks. In 1D/2D networks, weir equations are used to regulate flow exchange between 1D objects and 2D elements, including 2D manholes, river bank lines, inline banks, and more.

In the United States, the [weir equation](https://en.wikipedia.org/wiki/Weir) is usually defined as below,

![](images\0_oh11Tok_U7HTsp5p.png)

One issue with this format is that the units are not consistent on both sides of the equation. As a result, the coefficient varies depending on the units used. The SWMM5 help file provides typical values for both SI and Imperial units.

![](images\0_Fm7jgNlb421z-zom.png)

In InfoWorks ICM, the [weir equation](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-6A47B0A6-D57A-4FF7-AFBC-C0433A9151C4) is expressed as,

![](images\0_283yhfxBsDDsZk2x.png)

To ensure consistency regardless of the units used, InfoWorks ICM introduces the term g^0.5 in the equation. This makes the coefficient (Cd) a constant. The conversion between the commonly used coefficient © in the United States and Cd used in InfoWorks ICM is:

Cd = C/g^0.5 (where g=32.2 ft/s² for imperial, and g=9.81 m/s² for metric)

### [Setup Weir in InfoWorks ICM](https://github.com/mel-meng/hhnote/tree/main/hydraulics/weir%20in%20icm#setup-weir-in-infoworks-icm)

Let’s walk through a few examples to demonstrate how to set up a weir in InfoWorks ICM. In InfoWorks ICM, Cd is used for most objects within the 1D only context.

When it comes to 1D/2D settings, C instead of Cd are used for 1D river bank lines and inline banks. Refer to the online [reference](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-50940862-CDB2-4364-A74D-004982072B63) for more information. In this case, the value is in metric.

![](images\0_WfX4PhXtcX0NfzM7.png)

For bank lines in river reaches, refer to [help](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-1160B1F4-814A-4DB6-9897-22458AFDE039) for more information.

![](images\0_fh7MNvjYnLGaSvyM.png)

For inline banks refer to [help](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-15BB6CD3-E42B-446A-B3EF-817398C4F082) for more information.

![](images\0_jWemGLlzl-aGBtXO.png)

### [1D Weir](https://github.com/mel-meng/hhnote/tree/main/hydraulics/weir%20in%20icm#1d-weir)

Here is a typical weir setup. Refer to [help](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-2200B2A4-0C87-42C4-8A8A-4AE5C7C3E4B0) for more information. Notice that Cd is a constant regardless of the units of the model.

![](images\0_JQjycXzL32ScLNHD.png)

### [2D Manhole](https://github.com/mel-meng/hhnote/tree/main/hydraulics/weir%20in%20icm#2d-manhole)

When the flood type is set to “2D” for a 2D manhole, it utilizes the weir equation. To set the width, adjust the shaft area, and Cd is “flooding discharge coefficient”. Refer to [help](https://help.autodesk.com/view/IWICMS/2024/ENU/?guid=GUID-18DCDEB6-621C-4127-8C04-365D3CDC4C7E) for more information.

![](images\0_d5cyFXtsXnQT7XsA.png)

### [Appendix](https://github.com/mel-meng/hhnote/tree/main/hydraulics/weir%20in%20icm#appendix)

To validate InfoWorks ICM calculations, we compared the following, refer to the github notebook and example models for verifications.

* sim: weir depth vs flow curve from the InfoWorks ICM simulated results
* with g: flow calculated from simulated depth using equation: q = cd\*g⁰.5\*b\*d¹.5
* without g: flow calculated from simulated depth using equation: q = c\*b\*d¹.5

The plots below show that for 1D weir, the equation with g is used regardless of the model units.

![](images\0_UHa0n4ewViM1iFio.png)![](images\0_0CmKkZtMG38A1u_X.png)![](images\0_P3PlIHLf2zEu9wJp.png)

For the 2D manhole, the flow calculated from simulated depth using weir equation with g matched well to the simulated results. However, due to the complexity of 1D/2D interactions, there is noticeable differences between the two calculations.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 29, 2023](https://medium.com/p/601a011bab95).

[Canonical link](https://medium.com/@mel-meng-pe/weir-in-infoworks-icm-601a011bab95)

Exported from [Medium](https://medium.com) on March 18, 2025.