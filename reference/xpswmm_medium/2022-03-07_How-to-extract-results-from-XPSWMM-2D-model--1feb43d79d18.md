# How to extract results from XPSWMM 2D model?

source: Innovyze support portal

---

### How to extract results from XPSWMM 2D model?

source: [Innovyze support portal](https://innovyze.force.com/support/s/article/How-to-extract-results-from-XPSWMM-2D-model)

XPSWMM can aggregate 2D results for point, line and polygon into time series using the **Time Series Outputs** features,

![](images\1_iCumttJ0ctBn1azAX7tdPg.png)

1. select the layer
2. select the tool
3. draw the point/line on the map

After running the model, two csv files will be created to report the time series, and the max. min values in the 2D output folder.

* xx\_PO.csv: time series
* xx\_POMM.csv: max/min values
* xx: the model name

![](images\1_UiMMXKUuRiOLEFPp3ARs3w.png)

To review the time series,

![](images\1_nd82PSyBck-CZqCNivoDGg.png)

### Report for Polygon

If you need to get time series of a polygon, the XPSWMM user interface doesn’t support it yet. And you’ll need to use a Tuflow command to get it done.

* add a line in the control file read the polygon from an GIS file
* Read GIS PO == C:\temp\polygon.shp

![](images\1_BTAOjUEK9EbogZYnB-gzjQ.png)

prepare a shapefile,

* draw the polygon
* create 3 columns
* Type: Qin\_Qout\_Vol means to report flow in/out and the total volume within the polygon
* Label: the name of the time series for this polygon
* Comment: any comment

![](images\1_q7xWAdqJ63tDpagYVK7PNg.png)

The results are reported in the same csv files. But since it is not visible in XPSWMM, you need to plot it in Excel.

![](images\1_94S1VMbKijH_j8VDcG-eBQ.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [March 7, 2022](https://medium.com/p/1feb43d79d18).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-extract-results-from-xpswmm-2d-model-1feb43d79d18)

Exported from [Medium](https://medium.com) on March 18, 2025.