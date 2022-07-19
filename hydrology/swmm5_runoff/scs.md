---
title: SCS Infiltration
---

SCS infiltration is different from SCS hydrology method. It is often
used in place where SWMM runoff method is preferred as the routing
method, and to replace horton’s or green-ampt as the infiltration
method.

It is still based on the same equations of the SCS hydrology method.

# SCS Infiltration Method

It is possible to use SCS infiltration without using the SCS hydrology
method. Refer to the SWMM5 hydrology manual for the implementation.

There are several major differences between the SWMM5, XPSWMM and ICM
implementations,

-   SWMM5 doesn’t support the use of initial abstraction, which is the
    equivalent of setting initial abstraction as 0 in XPSWMM

-   XPSWMM doesn’t support the recovery of the infiltration capacity.
    For a single event simulation, this makes no difference

-   ICM is similar to XPSWMM that is supports the inclusion of the
    initial abstraction but does not support recovery of infiltration
    capacity.

SWMM5 assumes initial abstraction should be 0 when using the SCS
infiltration method, therefore the equation looks like the following.

<img src="media/image1.png" style="width:1.91643in;height:1.02071in"
alt="Diagram Description automatically generated with low confidence" />

<img src="media/image2.png" style="width:1.81227in;height:0.85406in"
alt="A picture containing diagram Description automatically generated" />

Q: total runoff (in)

P: total rainfall (in)

S: maximum infiltration capacity (in)

The total infiltration is defined as F = P – Q.

By tracking the total loss at each time step we can calculate the
infiltration rate.

<img src="media/image3.png" style="width:1.64563in;height:0.79157in"
alt="Chart Description automatically generated with medium confidence" />

<img src="media/image4.png" style="width:1.07278in;height:0.36454in" />

i: rainfall intensity in/hr

dt: time step (hr)

<img src="media/image5.png" style="width:1.94767in;height:0.9478in"
alt="Text, letter Description automatically generated with medium confidence" />

<img src="media/image6.png" style="width:1.42691in;height:0.47911in" />

f: infiltration rate (in/hr)

For continuous simulation, S is constant for each storm event, however,
for each new event, S is updated by reducing its capacity from previous
storm(s), and regenerating when there is no rainfall.

# SWMM Model

We have a single subcatchment 100% pervious without any depression
storage.

<img src="media/image7.png" style="width:4.91991in;height:4.18192in"
alt="Graphical user interface, table Description automatically generated" />

Unlike the Horton method, the infiltration is always smaller than the
rainfall when it rains.

<img src="media/image8.png" style="width:4.26402in;height:4.52752in"
alt="Chart, histogram Description automatically generated" />

# XPSWMM Model

For the XPSWMM model, it has the same setup as SWMM5 except for the SCS
infiltration we need to set initial abstraction as 0 (7) to match what
SWMM5.

<img src="media/image9.png" style="width:6.5in;height:4.41736in"
alt="A screenshot of a computer Description automatically generated with medium confidence" />

The results are almost the same as shown below,

<img src="media/image10.png" style="width:5.36276in;height:3.26042in" />

<img src="media/image11.png" style="width:5.71928in;height:4.60623in" />

If you are interested in how to manually calculate the infiltration
using the equations in the SWMM5 manual, see the excel file for more
details.

<img src="media/image12.png" style="width:6.5in;height:2.77778in"
alt="Table, calendar Description automatically generated" />

# InfoWorks ICM

Curve number is defined in two places in ICM. CN number is defined in
the subcatchment property(left), and the rest is defined in the runoff
surface for pervious land cover (right). To be consistent with the SWMM5
method, we set initial abstraction to 0, we set the initial loss to 0
for the runoff surface.

<img src="media/image13.png" style="width:2.76007in;height:2.88506in"
alt="Graphical user interface, table Description automatically generated" />
<img src="media/image14.png" style="width:2.95796in;height:2.40595in"
alt="Table Description automatically generated" />

The results are close, but noticeably different. One obvious limitation
in ICM is that the infiltration stops when the rain stops.

<img src="media/image15.png" style="width:5.23958in;height:4.28011in"
alt="Diagram Description automatically generated with medium confidence" />

<img src="media/image16.png" style="width:5.18239in;height:3.1875in"
alt="Chart, line chart Description automatically generated" />
