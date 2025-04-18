# How to model a screen in InfoWorks ICM

source: github

---

### How to model a screen in InfoWorks ICM

source: [github](https://github.com/mel-meng/hhnote/tree/main/hydraulics/screen)

### Introduction

Screen is modeled using the Kirschmer’s equation in ICM. Refer to this [Reference PDF](https://web.itu.edu.tr/~bulu/hyroelectic_power_files/lecture_notes_09.pdf) on pg 5 for more information.

![](images\0_yK9KZUybiWTnbxUu.png)

As shown above, it is an empirical equation based on the configuration of the screen. Field measured data probably will be needed for more accurate results(refer to this [study](https://www.duperon.com/Portals/0/Documents/S4/Kirschmer%20Paper-Master%20Manuscript-FINAL.pdf) for more information).

* The bigger the opening (s/b), the less head loss
* The head loss is highest when the screen is perpendicularly placed (alpha=90), and decreases as it tilts

### Screen in ICM

ICM screen is a link with the following parameters,

* invert of the screen. I found it a little confusing since it is called crest. It is the elevation
* For the angle, it is measured from the vertical line

![](images\0_tt4oNaTSz0XIVnaX.png)![](images\0_ebCoxdtKyQQdDWR9.png)

The engine implements the following,

* The equation is similar to weir equation under submerged condition, the driving force is: (h1-h2)\*\*0.5\*h1
* The rest of the terms is a constant
* b: there is an error in the ICM help document in older versions, b is the approaching width of the channel, not the opening.

![](images\0_W36kYPV6d2fjmUf8.png)![](images\0_gBDu63MOY0wqC1T4.png)

The above equation can be derived as shown below,

Q = w\*h1\*v1

Q: approaching flow

W: channel width

h1: approaching depth

v1: approaching velocity

v1 can be calculated using the Kirschmer formula

![](images\0_aGSjxGBprinmMmda.png)

Delta h = h1-h2

The opening shown in the profile is the height of the screen\*cos(angle). h1 and h2 are the depth before and after the screen.

![](images\0_lujPSw1m2Zk7zMzQ.png)

When the screen is drowned, there is an option in the simulation parameter to use Villemonte equation (TODO: not tested yet).

![](images\0_meXgr0xrFkdWR909.png)![](images\0_LVx72PU2bF-sIxXs.png)

### ICM Model

Three simple ICM models were created to show how screen works. By adjusting the downstream node and pipe, 3 different conditions were tested.

![](images\0_U5V2IY-S9YS1vT3_.png)

* Normal: use Kirschmer’s equation
* Weir: use weir equation
* Drowned: use Kirschmer’s equation when Villemonte option is not ticked

The results are verified by comparing the ICM simulated results with manually calculated values.

![](images\0_J9HIXBPZ6ulM116F.png)

### Approaching Velocity

The US velocity reported by ICM is the approaching velocity in the channel, not the velocity through the openings of the screen. As shown in the calculation below, the velocity using both the channel width and screen opening were calculated. And ICM reports the approaching velocity (green matches orange).

![](images\0_UKjFbepHIP3-czQZ.png)![](images\0_CXTm70lYiipUNzt8.png)

### Normal condition

For normal condition, we compared the headloss reported by ICM (dh), and calculated using the Kirschmer function. Very good match is observed (r2=0.999)

* dh = h1 -h2
* dh\_eq = KirschmerFn(velocity)

![](images\0_KZINikuJFZPCQWhI.png)![](images\0_atdb76AKaVyO5Prb.png)

### Weir condition

For weir condition, we compared the flow reported by ICM, and calculated using the weir equation from H1.

![](images\0_revL4hMamztebJ32.png)![](images\0_J6HR3BlbIFgTYos8.png)

Good match was observed (r2=1)

![](images\0_WjInerl1u3aH_iwE.png)

### Drowned — use Kirschmer’s equation

Drowned condition should be the same as normal condition since the option was not checked (r2=0.97).

![](images\0_-ERon5Eg1DkD808H.png)![](images\0_5mWppwFp4R6VVNZx.png)

### Drowned — use Villemonte equation

TODO：

When the weir is drowned (h2>height of weir), the flow through the weir is adjusted using a factor of the free weir flow as shown in the [source](https://cassiopee.g-eau.fr/assets/docs/en/calculators/structures/villemonte_1947.html) below.

![](images\0_d0HrMOZW0TYea-Y9.png)

### Conclusion

In this article, we went through a few examples to verify the calculation of screens in ICM.

* The Kirschmer’s equation is used for normal condition.
* The angle is measured from the vertical, not horizontal.
* The US velocity is the approaching velocity, not the through velocity of the screen opening.
* When the downstream of the screen is below the screen invert (crest), the weir equation will be used.
* When the screen is drowned, the situation is more complicated because of downstream restriction might play a more important role.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 5, 2022](https://medium.com/p/47ea08fdd68e).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-model-a-screen-in-infoworks-icm-47ea08fdd68e)

Exported from [Medium](https://medium.com) on March 18, 2025.