# Batch Import hydrograph from csv files into XPSWMM

I have blogged about batch import rainfall and hydrograph into XPSWMM using python script with the help of XPX files.

---

### Batch Import hydrograph from csv files into XPSWMM

I have blogged about batch import rainfall and hydrograph into XPSWMM using python script with the help of XPX files.

[**How to batch import rainfall into XPSWMM**  
*source: Innovyze Support Portal*mel-meng-pe.medium.com](https://mel-meng-pe.medium.com/how-to-batch-import-rainfall-into-xpswmm-30c965c3daf0 "https://mel-meng-pe.medium.com/how-to-batch-import-rainfall-into-xpswmm-30c965c3daf0")

[**Batch Hydrographs into XPSWMM**  
*A common scenario is using HEC-HMS to generate the hydrographs, then route the flow in XPSWMM. For models with hundreds…*mel-meng-pe.medium.com](https://mel-meng-pe.medium.com/batch-hydrographs-into-xpswmm-a9303df7a46b "https://mel-meng-pe.medium.com/batch-hydrographs-into-xpswmm-a9303df7a46b")

In this article, I will update the batch hydrographs script to import hydrographs from a series of CSV files. The python script can be found at [github](https://github.com/mel-meng/xpswmm/blob/master/xpx/source/src/hydro_cals_xpx_tools.py).

### The problem

We have hundreds of CSV files saved in different folders, each csv file has the results of the hydrograph for a basin generated from another tool. Our job is to extract the time series from each csv file and assign it as the user inflow for a node in an XPSWMM model.

### The solution

The solution is we first walk through all the folders to identify all the csv files, and then merge all the hydrograph into a single csv file.

Then we import the merged csv file into XPSWMM using the same script we developed in the batch hydrograph blog.

Below is a sample of the hydrograph format. The only thing we are interested is the highlighted columns, we can ignore everything else.

![](images\1_rNIiEV_FIh28G1B1jg8XVw.png)

The merged csv file looks like this, the first column is the time in hours, and each column is a node name.

![](images\1_WemsZ5ykZA9zu5lE3ZkmmQ.png)

### The script

To run the script,

1. update line 76 with the root folder of all the csv files
2. update the path for the xpx file which will hold the time series information to be imported

![](images\1_ZHUZxUNHYt-Kvo3h1Bsayw.png)

Then run the script it will create the xpx file.

More details about the script below.

Reading the time series from the csv file is very easy to do with Pandas.

line 8: we read the csv file and skip the first 9 lines. “dropna” is needed to remove the last empty row.

line 9: since XPSWMM uses hours for time series, we need to turn minutes into hour.

line 10: we use a simpler name for the peak flow

line 11: we need to merge all the time series into a single table, setting the hour column as the index is needed when we join all the time series.

![](images\1_xOY_Sh3mLtM9RKK9_7nWVA.png)

The next step is to find all the CSV files, extract the time series, and then merge them into a single csv file.

line 26: the variable to hold the merged table.

line 27: using the pyhton os.walk to loop through all the files and subfolders in the root folder

line 28,29,30: locate a csv file

line 32: the node name is embedded into the file name “Rubio Wash — DA — **0**–50YR.csv”, it is the 3rd part of the name if separated by “-”

line 34: we extract the time series from the csv file

line 34: we rename the column name to the node name

line 36–39: we join the new csv file to the df\_join, the merged table

line 42: after looping through all the files, we save the merged files to the csv file.

![](images\1_GeH4Lgzh6IEySBJJLy9bZA.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [December 28, 2021](https://medium.com/p/6e6ba3f01f2b).

[Canonical link](https://medium.com/@mel-meng-pe/batch-import-hydrograph-from-csv-files-into-xpswmm-6e6ba3f01f2b)

Exported from [Medium](https://medium.com) on March 18, 2025.