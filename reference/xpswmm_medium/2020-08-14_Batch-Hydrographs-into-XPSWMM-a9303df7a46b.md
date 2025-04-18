# Batch Hydrographs into XPSWMM

A common scenario is using HEC-HMS to generate the hydrographs, then route the flow in XPSWMM. For models with hundreds of basins, it can…

---

### Batch Import Hydrographs into XPSWMM

A common scenario is using HEC-HMS to generate the hydrographs, then route the flow in XPSWMM. For models with hundreds of basins, it can be a tedious task copying hydrograph for each basin.

![](images\1_0QD9-ciIScaKfX8RTRyIRQ.png)

In this article, I will show an easy way to convert the hydrographs from a csv file into XPSWMM/XPSTORM using the XPX exchange format.

Step 1: Download the tool and install python

The python script can be downloaded from [Github](https://raw.githubusercontent.com/mel-meng/xpswmm/master/xpx/source/src/xpx_tools.py). Here is the link to the [project](https://github.com/mel-meng/xpswmm/tree/master/xpx/source/src).

Anaconda makes installing python really easy. Here is the [download link](https://www.anaconda.com/products/individual#windows). Either 64-bit or 32-bit should work.

1. Start “Spyder”

![](images\1_75eWlgjlwLLc1UFSMdSbWA.png)

2. Prepare the csv file. As shown below, each column is a hydrograph for a node. The header should match XPSWMM node names exactly. The first column is the time stamp, and it should be called datetime and the format should look like the following. If you are familiar with python, read the comment in the script and update the date\_format string to match your format.

![](images\1_XxVZ0pBukWjnffyzJ2K36A.png)

This csv file can be easily created from HEC-HMS using HEC-DSSVue. Open the exported excel file and remove the extra rows and columns.

![](images\1__iSkXMX_3xWaIalLSb4b-w.png)

3. Open the downloaded python script, update the hydograph and xpx output paths, then hit the run button. This should generate the \*.xpx file.

![](images\1_TZ9KMbDr3apHEdYp0bChbg.png)

4. Import the xpx file into the XPSWMM/XPSTORM model

![](images\1__rwxh5JX9VAk8zYXuyXbkA.png)

And that’s it, a very simple and quick way to get hydrographs exported from HEC-HMS into XPSWMM/XPSTORM.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 14, 2020](https://medium.com/p/a9303df7a46b).

[Canonical link](https://medium.com/@mel-meng-pe/batch-hydrographs-into-xpswmm-a9303df7a46b)

Exported from [Medium](https://medium.com) on March 18, 2025.