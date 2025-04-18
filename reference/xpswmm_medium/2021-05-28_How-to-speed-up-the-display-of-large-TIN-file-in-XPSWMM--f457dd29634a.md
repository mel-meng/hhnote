# How to speed up the display of large TIN file in XPSWMM?

Source: Innovyze Support Portal

---

### How to speed up the display of large TIN file in XPSWMM?

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-speed-up-the-display-of-large-TIN-file-in-XPSWMM)

When building large 2D models, loading a high resolution TIN covering the whole modeling area can take a long time, and once it is loaded, every time the view is moved or zoomed in or out, it could also take some time to refresh.

In this article we’ll explore a few options to speed up the display of large TIN files. The basic idea is to use the high resolution grid file for simulation but using a lower resolution or options with faster rendering for display.

* Use the reference grid
* Re-sample the TIN to a coarser resolution

### Use the source grid file in simulation

XPSWMM by default will use the DTM loaded into the model as XPTIN. However, for very large model this could cause performance issues when rendering the TIN. In the 2D settings, we can use an external grid file instead. In that way, XPSWMM will use the external grid file to generate the grid cells. And we no longer needs to load the large XPTIN into the model.

![](images\1_KyxbF_KymCmRGxt3ZnJFtg.png)![](images\1_Lu_6aSRq_SIi2M83zl1h6g.png)

### Reference Grid

If loading the XPTIN is too slow, and dividing the XPTIN into smaller tiles or lower the resolution is too much effort. Reference grid can be another alternative.

The main benefits of a referenced grid is that you can skip the TIN building process. By drawing a polygon in the area of interest, it only renders the TIN for a much smaller area. The main limitation is that you cannot get the Z value simply by pointing your mouse at the location, and the value has to be estimated using contour lines of the color symbiology.

![](images\1_R-FQJ_ABNzEIrCeIjaoqXg.png)

Then you draw the area to be displayed

![](images\1_GMOm680_DN79Ur1KHAGO-Q.png)

Then you can change how it looks,

![](images\1_GN-tDNTkYEYfJdje5P183g.png)

### Re-sample TIN

Loading the TIN file does have a great benefit, you can get the Z value just by pointing your mouse at the location. However, it could slow down the model if the TIN file is too big. One alternative is to re-sample the source data so that its size is more manageable in XPSWMM. Or it can be broken into smaller tiles, and loaded into XPSWM as needed. By turning on one tile a time, it can greatly improve the performance.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 28, 2021](https://medium.com/p/f457dd29634a).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-speed-up-the-display-of-large-tin-file-in-xpswmm-f457dd29634a)

Exported from [Medium](https://medium.com) on March 18, 2025.