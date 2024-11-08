---
title: 1D Dual drainage with Gully and Inlets in InfoWorks ICM
---

# Introduction

When modeling a dual drainage (also called major/minor) systems in a 1D model, you need to use an [inlet](https://help.autodesk.com/view/IWICMS/2025/ENU/?guid=GUID-3FAD07F7-2B29-4B60-888E-AB7FD41E7B2E). A typical set up includes,

- Overland flow on the street

- An inlet captures some of the flow into the underground pipes

- The bypass flow continues down the street

<img src="./media/image1.png" style="width:3.58665in;height:2.37954in" alt="Diagram of a street system Description automatically generated" />

Image source: [SWMM5.2.0 Features](https://github.com/USEPA/Stormwater-Management-Model/blob/develop/doc/New%20SWMM%205.2%20Features.md)

InfoWorks ICM models such a system with,

- Streets as overland channels, the system type must be set as “overland”

- The node that connects to both the overland and underground pipes need to have a flood type set as either “inlet” or “gully”.

<img src="./media/image2.png" style="width:3.72661in;height:2.6113in" alt="Diagram of a diagram of a road Description automatically generated" />

Here is an example, a gully is the same as an inlet with “head” input type.

<img src="./media/image3.png" style="width:6.5in;height:4.74306in" alt="A screenshot of a computer Description automatically generated" />

# Best practice

The flow conditions at the inlet are quite complicated to model directly. They are commonly estimated as simple correlations of the approaching flow conditions. A head discharge curve is commonly used to determine the flow captured from the approach flow depth on the road.

The head discharge curve uses,

- **inflow** as the discharge

- **Flood depth** as the head

<img src="./media/image4.png" style="width:5.17611in;height:3.35784in" alt="A diagram of a pipe Description automatically generated" />

It should be noted the flood depth differs for inlet nodes and manholes without overland connections,

- For inlets: flood depth = Overland level – Ground level

- For manholes: flood depth = Level – Flood level (usually ground level)

Advanced inlet flow capture will be covered in another article. This article only focuses on using the head discharge curve.

# Overflow

When the underground pipes are full, water can overflow from the inlet onto the road. The same head discharge curve is applied to overflows. If the curve doesn’t define explicitly what happens when the flow is negative, interpolation will be used.

When overflow occurs, the water level in the manhole is higher than the water level on the street.

<img src="./media/image5.png" style="width:3.82542in;height:2.48728in" alt="Water flowing water around a sewer manhole Description automatically generated" />

Since the water is coming out of the manhole, both the head and flow are negative. The head is the difference of,

- Street water level is “flood depth”

- Manhole water level is “Level – ground elevation”

<img src="./media/image6.png" style="width:5.70314in;height:2.87472in" alt="Diagram of a diagram of a pipe Description automatically generated" />

You can explicitly define the overflow in the curve,

<img src="./media/image7.png" style="width:2.7383in;height:2.84621in" />

One trick to make an inlet that doesn’t overflow is to keep the flow at 0 for negative head.

<img src="./media/image8.png" style="width:3.78123in;height:2.40286in" />

# Example

In this example, we compare 3 setups for an inlet

- The top one uses a gully

- The middle one uses an inlet

- The bottom one uses a screw pump to mirror the inflow into the inlet

<img src="./media/image9.png" style="width:6.5in;height:2.63403in" alt="A diagram of a machine Description automatically generated with medium confidence" />

All 3 setups share the same profile,

- By raising the water level on the left side, the water level on the street increases, allowing flow into the inlet.

- Once the water level on the street subsides, we raise the water level in the underground pipe to cause overflow in the middle node.

<img src="./media/image10.png" style="width:6.5in;height:2.62222in" alt="A diagram of a channel Description automatically generated" />

The results are shown below,

- For the flow through the links, when it is going into the underground pipe, they all show the results. However, when it is overflowing onto the street, screw pump has no flow.

- The water depth on the street shows similar pattern.

<img src="./media/image11.png" style="width:6.5in;height:2.68194in" alt="A graph on a white background Description automatically generated" />

<img src="./media/image12.png" style="width:6.5in;height:2.68194in" alt="A screen shot of a graph Description automatically generated" />

Therefore, when controlled by the same curve, inlet, gully and screw pump all show the same results except when there is reverse flow, that screw pump doesn’t allow reverse flow. A closer review shows that inlet, gully and screw pump all follow the head discharge curve.

<img src="./media/image13.png" style="width:6.5in;height:1.93194in" alt="A graph with orange and white lines Description automatically generated" />

# Conclusion

When modeling dual drainage systems in InfoWorks ICM, you can capture flow from the road into an inlet by connecting an overland channel and an underground pipe to the same manhole with a gully. By using a head discharge curve, you can define both the flow into the inlet and overflow onto the road as a function of the water depth on the road, and the overflow head.
