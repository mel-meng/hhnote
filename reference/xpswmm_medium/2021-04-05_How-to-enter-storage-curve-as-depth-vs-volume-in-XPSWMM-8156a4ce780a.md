# How to enter storage curve as depth vs volume in XPSWMM

source: Innovyze Support Portal

---

### How to enter storage curve as depth vs volume in XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-enter-storage-curve-as-depth-vs-volume-in-XPSWMM)

When modeling storage, entering a depth storage curve seems to be the only option in XPSWMM. What if you need to enter a depth-volume curve instead?

![](images\1_drx4-b7kQZFnOVkkp34gpQ.png)

Designed for advanced users, we can overwrite default behavior of the XPSWMM using [configuration keywords](https://help.innovyze.com/display/xps/Configuration+Keywords).

![](images\1_hAvYC6CzLT5YJ8gjHf3Bgg.png)![](images\1_Zmv1PVQjmYx7Sdp9YkFlow.png)

With the VE keyword, XPSWMM will take the storage curve as depth-volume. However, setting up a model in this manner can be quite confusing because the user interface still says it is depth vs area, you can only tell this by checking this VE parameter or looking into the detailed 1D log.

Another challenge is that this applies to the whole model, if you have a mix of depth-area and depth-volume curves, then they need to be converted to the same format.

Here is the recommended approach,

1. setup the VE configuration keyword
2. enter the depth-vs-volume curve
3. run the model
4. check the 1D log table 4E and get the converted depth-vs-area curve
5. remove the VE configuration keyword
6. update the cure to the depth-vs-area curve
7. run the model

### Converting depth-volume to depth-area

When the VE parameter is used, XPSWMM starts with the user defined stage information provided, then breaks this into a smaller interval, and uses an algorithm to approximate the equivalent areas for the volume you have provided.

After the running the model, go to the 1D log.

![](images\1_fcnU8mg5GJAMcvtnAVThqw.png)

The section titled: “Storage Junction Data” right after Table E3b has the storage information.

Below is a sample of storage without using the VE keyword,

![](images\1_WygN633OKO-ud7UETrYNSw.png)

With the keyword VE turned on,

![](images\1_7QOTKECz4kPd9a3uRxISmA.png)

As shown above, when the junction type is Elev/Vol, XPSWMM interpolates the curve into smaller intervals to approximate the depth-volume curve as depth-area curve. Pay attention to the units when copying the curve. In this case, we would copy the “depth ft” column and “Area acres” columns as the depth-area curve.

Note that storage volume when using the stepwise linear method is represented as a [Frustum](https://en.wikipedia.org/wiki/Frustum#:~:text=In%20geometry%2C%20a%20frustum%20%28plural,right%20pyramid%20or%20right%20cone.), and the volume is calculated using the following formula for volume of a Frustum:

V = h/3 (B1 + SQRT(B1\*B2) + B2)

where V is the volume of storage  
h is the height  
B1 and B2 the surface areas

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 5, 2021](https://medium.com/p/8156a4ce780a).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-enter-storage-curve-as-depth-vs-volume-in-xpswmm-8156a4ce780a)

Exported from [Medium](https://medium.com) on March 18, 2025.