---
title: Screen
---

# Introduction

Screen is modeled using the Kirschmer’s equation in ICM. Refer to this [Reference PDF](https://web.itu.edu.tr/~bulu/hyroelectic_power_files/lecture_notes_09.pdf) on pg 5 for more information.

<img src="./media/image1.png" style="width:6.5in;height:7.28333in" alt="Kirschmer Equation" />

As shown above, it is an empirical equation based on the configuration of the screen. Field measured data probably will be needed for more accurate results(refer to this [study](https://www.duperon.com/Portals/0/Documents/S4/Kirschmer%20Paper-Master%20Manuscript-FINAL.pdf) for more information).

-   The bigger the opening (s/b), the less head loss

-   The head loss is highest when the screen is perpendicularly placed (alpha=90), and decreases as it tilts

## Screen in ICM

ICM screen is a link with the following parameters,

-   invert of the screen. I found it a little confusing since it is called crest. It is the elevation

-   For the angle, it is measured from the vertical line

<img src="./media/image2.png" style="width:7.10209in;height:4.25948in" alt="Diagram Description automatically generated" />

<img src="./media/image3.png" style="width:5.01622in;height:4.02651in" alt="Graphical user interface, diagram Description automatically generated" />

The engine implements the following,

-   The equation is similar to weir equation under submerged condition, the driving force is: (h1-h2)\*\*0.5\*h1

-   The rest of the terms is a constant

-   b: there is an error in the ICM help document in older versions, b is the approaching width of the channel, not the opening.

<img src="./media/image4.png" style="width:7.07639in;height:2.33306in" alt="Diagram Description automatically generated" />

<img src="./media/image5.png" style="width:5.8326in;height:4.07241in" alt="Graphical user interface, text, application, email Description automatically generated" />

The above equation can be derived as shown below,

Q = w\*h1\*v1

Q: approaching flow

W: channel width

h1: approaching depth

v1: approaching velocity

v1 can be calculated using the Kirschmer formula

<img src="./media/image6.png" style="width:4.78065in;height:3.23918in" alt="Graphical user interface Description automatically generated" />

Delta h = h1-h2

The opening shown in the profile is the height of the screen\*cos(angle). h1 and h2 are the depth before and after the screen.

<img src="./media/image7.png" style="width:6.92565in;height:2.63961in" alt="Graphical user interface, application Description automatically generated" />

When the screen is drowned, there is an option in the simulation parameter to use Villemonte equation (TODO: not tested yet).

<img src="./media/image8.png" style="width:3.16627in;height:2.32263in" alt="Table Description automatically generated" />

<img src="./media/image9.png" style="width:6.5in;height:2.8125in" alt="Graphical user interface, text Description automatically generated with medium confidence" />

# ICM Model

Three simple ICM models were created to show how screen works. By adjusting the downstream node and pipe, 3 different conditions were tested.

<img src="./media/image10.png" style="width:7.65749in;height:6.51067in" alt="Graphical user interface, application Description automatically generated" />

-   Normal: use Kirschmer’s equation

-   Weir: use weir equation

-   Drowned: use Kirschmer’s equation when Villemonte option is not ticked

The results are verified by comparing the ICM simulated results with manually calculated values.

<img src="./media/image11.png" style="width:11.72697in;height:4.43912in" />

## Approaching Velocity

The US velocity reported by ICM is the approaching velocity in the channel, not the velocity through the openings of the screen. As shown in the calculation below, the velocity using both the channel width and screen opening were calculated. And ICM reports the approaching velocity (green matches orange).

<img src="./media/image12.png" style="width:4.49661in;height:2.91693in" alt="Text Description automatically generated" />

<img src="./media/image13.png" style="width:3.97676in;height:2.73653in" alt="Chart, line chart Description automatically generated" />

## Normal condition

For normal condition, we compared the headloss reported by ICM (dh), and calculated using the Kirschmer function. Very good match is observed (r2=0.999)

-   dh = h1 -h2

-   dh_eq = KirschmerFn(velocity)

<img src="./media/image14.png" style="width:8.40787in;height:3.22456in" alt="Graphical user interface, application Description automatically generated" />

<img src="./media/image15.png" style="width:9.73999in;height:3.33304in" alt="Chart, scatter chart Description automatically generated" />

## Weir condition

For weir condition, we compared the flow reported by ICM, and calculated using the weir equation from H1.

-   <img src="./media/image16.png" style="width:4.84314in;height:0.84365in" alt="A picture containing text Description automatically generated" />

<img src="./media/image17.png" style="width:6.84835in;height:2.43074in" alt="Graphical user interface, application Description automatically generated" />

Good match was observed (r2=1)

<img src="./media/image18.png" style="width:6.71317in;height:2.41895in" alt="Chart, line chart Description automatically generated" />

## Drowned – use Kirschmer’s equation

Drowned condition should be the same as normal condition since the option was not checked (r2=0.97).

<img src="./media/image19.png" style="width:6.85081in;height:2.6274in" alt="Graphical user interface, application Description automatically generated" />

<img src="./media/image20.png" style="width:6.84355in;height:2.21715in" alt="Chart, line chart Description automatically generated" />

## Drowned – use Villemonte equation

TODO：

When the weir is drowned (h2\>height of weir), the flow through the weir is adjusted using a factor of the free weir flow as shown in the [source](https://cassiopee.g-eau.fr/assets/docs/en/calculators/structures/villemonte_1947.html) below.

<img src="./media/image21.png" style="width:5.71803in;height:3.04129in" alt="Diagram Description automatically generated" />

# Conclusion

In this article, we went through a few examples to verify the calculation of screens in ICM.

-   The Kirschmer’s equation is used for normal condition.

-   The angle is measured from the vertical, not horizontal.

-   The US velocity is the approaching velocity, not the through velocity of the screen opening.

-   When the downstream of the screen is below the screen invert (crest), the weir equation will be used.

-   When the screen is drowned, the situation is more complicated because of downstream restriction might play a more important role.
