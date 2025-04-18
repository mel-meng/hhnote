# What happens when a river is overflowing in XPSWMM?

source: Innovyze Support Portal

---

### What happens when a river is overflowing in XPSWMM?

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/What-happens-when-a-river-is-overflowing-in-XPSWMM)

Water flows through a river in a very different way than flowing in man made structures. When a river overflows, it is through the banks. Unlike storm sewer, through an overflowing manhole. So how does XPSWMM handle that?

The XPSWMM engine is built with the assumption of a closed pipe network, there is no special treatment for a channel or river. Let’s review how XPSWMM solve the hydraulics. As the diagram shown below, the momentum equation is applied to each pipe and calculated at the mid-point of the pipe, and the continuity equation is applied to the “node assembly” which includes all the half-pipes connected to the node.

![](images\1_APucOv05IsEHcX-ByQFirw.png)

There are a few important implications of this approach,

* Only a single flow and velocity is calculated for each link at the mid-point
* The HGL inside of the a link is not calculated within the link, but assumed as a straight line connecting the head of the upstream and downstream nodes
* Overflow can only happen at nodes, not in the link

However, such assumptions might not be ideal for a river system,

* A river system is not closed, and it doesn’t have nodes, and when overflows, it is through the banks not the “node”
* The assumption the HGL within each pipe is a straight line holds very well for most man made structures, however, might not be the case for a winding river.

Before getting into the recommendations, let’s get into more details of how XPSWMM will simulate a river when it is overflowing.

### River as closed pipe

A river link behaves exactly the same as a closed circular pipe. The only difference is that the cross section of a channel is irregular.

As far as XPSWMM engine is concerned, the cross section of a channel or river is a closed shape. Water cannot rise above the top of the section.

When the channel is flowing within the cross section, it is the same as a pipe flowing half full. When a channel is flowing above the height of the defined cross section, it will operate exactly the same as a surcharged pipe. A imaginary lid will be placed on top of the cross section of the channel, and all the flow will be forced and pressurized through the channel.

### What happens when a river is overflowing

As we just discussed, it will behave exactly the same as a surcharged pipe. The flow will be pressurized and therefore, the water depth in the nodes will be elevated above the crow of the pipe to push more flow through the channel.

Apparently, that is not what we would like the river link to do. The ideal outcome should be that the water will overflow through the lowest point of the bank.

If we are building a 1D/2D link, we can build the 1d/2d interface lines to represent the banks, and we can let the water to overflow along the bank lines.

If we are building a 1D only model, then we’ll have to make some assumptions where we would like the overflow to go.

As we explained, the only way to lose flow is through the node. So when a river overflows, we’ll have to lose the flow through the nodes. If we believe that all the flow above the top of the cross section will simply be gone, we can simply use the ponding option of “None” at the node.

![](images\1_NSzte4wCYZtDv3pOw4DNPw.png)

### Recommendations

Based on the discussion above, we have the following recommendations.

If river overflowing is critical to the modeling project, review the limitations and choose the appropriate measures to address it. For example, setting up a 1D/2D model to simulate the overflow through the banks, or develop a storage curve for overflowing through a node.

Understand different configurations when a pipe is surcharged.

Typically, you should setup the node ground elevation the same as the top of your cross section, and then choose the ponding option when there is overflow. In this manner, XPSWMM doesn’t need to make any assumptions.

If you set your node ground elevation higher than the top of the cross section, XPSWMM will have to make some assumptions,

* Assume the cross section have a lid on top, and will flow surcharged. Unless you are modeling the link as a bridge, this is rarely what is desired. When choosing this option, make sure the VERT\_WALLS=OFF is used.

![](images\1_P1WqTO49r0oA2pB8CyB8qw.png)![](images\1_F7pnxleOLp67rM5X9VuOUg.png)

* Or setup the max depth to use only part of the cross section as a closed pipe

![](images\1_oEd-HuzuFFmCjmIDz4DT3A.png)![](images\1_s04-sB44FNnV9Qwp4zVUtQ.png)

* Another commonly used option during the initial phase of a modeling project is to add vertical walls on the cross section to keep the water contained in the channel without overflowing, this will be the worse situation as far as the max. water depth is concerned.
* Set the VERT\_WALLS=ON (by default this is turned on)
* Set the node ground elevation higher than the expected HGL to contain all the water in the channel
* Set max depth=0

![](images\1_vSlOg_CZx3ApU4FpLLR-WQ.png)

Blow is a comparison with the VERT\_WALLS both on/off.

If the 1D log table E11, the green one is the off option, and the channel is treated as a closed pipe, the max area is 13 sf. While with the ON option, vertical walls are added to the cross section to match the ground elevation, therefore, the max. area is 17.6sf, bigger than the area defined in the cross section.

![](images\1_1NRjf8uxKNKQumt7l-fxzQ.png)![](images\1_PVcDKN-pPXhK_cEtWJRJ7Q.png)

### Conclusion

XPSWMM models the river the same way as a closed pipe, and are less sophisticated than river modeling packages such as ICM and HECRAS.

Understanding the river modeling approach and limitations of the XPSWMM can help when converting models from other packages into XPSWMM, and choosing the appropriate approach modeling river.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 1, 2021](https://medium.com/p/425578f9bb00).

[Canonical link](https://medium.com/@mel-meng-pe/what-happens-when-a-river-is-overflowing-in-xpswmm-425578f9bb00)

Exported from [Medium](https://medium.com) on March 18, 2025.