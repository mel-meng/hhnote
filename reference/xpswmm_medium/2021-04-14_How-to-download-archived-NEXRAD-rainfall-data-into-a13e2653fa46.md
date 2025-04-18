# How to download archived NEXRAD rainfall data into

source: Innovyze Support Portal

---

### How to download archived NEXRAD rainfall data into ICM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-download-archived-NEXRAD-rainfall-data)

Many Cities around the United States have access to freely available high resolution radar rainfall data. In this article, we’ll have a step by step example on downloading a few months worth of radar rainfall data and see them playing in ICM.

### Locate the station

ICM supports the DPR product (Instantaneous Precipitation Rate), the first thing is to find the nearest station with that data. Use the map below, we can see all the NEXRAD stations.

[**Radar Data Map | GIS Maps | National Centers for Environmental Information (NCEI)**  
*Level-II and Level-III NEXRAD data include three meteorological base data quantities: reflectivity, mean radial…*gis.ncdc.noaa.gov](https://gis.ncdc.noaa.gov/maps/ncei/radar "https://gis.ncdc.noaa.gov/maps/ncei/radar")

1. search the location of interest
2. check only Level III
3. click on the wrench icon
4. enable the identify tool

![](images\1_nnYINB_0KFeQqkQivHo2tw.png)

Click on the red square to get the station information,

![](images\1_EDOS_YdV5DWAFwBJMRz24Q.png)

Make sure the station has DPR.

![](images\1_VNAOJTKVZITDtViwQllqAg.png)

### Order the data

To download the data for station KOKX, go to the NEXRAD data inventory page below.

[**Order Data | Archive Information Request System | National Climatic Data Center (NCDC)**  
*NCEI's Archive Information Request System (AIRS) provides online access to numerous data holdings in their native…*www.ncei.noaa.gov](https://www.ncei.noaa.gov/has/HAS.FileAppRouter?datasetname=7000&subqueryby=STATION&applname=&outdest=FILE "https://www.ncei.noaa.gov/has/HAS.FileAppRouter?datasetname=7000&subqueryby=STATION&applname=&outdest=FILE")

Select the station, time range, and leave your email before submit the order.

![](images\1_aZymGx1pUqFDW4_eTPdeTw.png)

### Download the data

It is recommended to use a FTP client for downloading the data due to its large size and number of files. You can install [WinSCP](https://winscp.net/eng/download.php), an open source free FTP client for this task.

Copy the ftp url from the email notification of order complete

![](images\1_uAbihT6StkcxM4Ocm-BCRQ.png)

Start WinSCP, in a new session,

1. paste the url into the host name box
2. check the “Anonymous login”
3. click Login

![](images\1_63ktleE-KNYMQ9oMIGxE4g.png)

Open the local folder where the files will be downloaded,

![](images\1_P42eBdSUwCjxGFqOkLGbzw.png)

in the FTP window, hit ctrl+A to select all files, then right click and download.

![](images\1_JG0x5Ah4CaiUH_nA2VVtiQ.png)

It will take a while to download.

### Extracting DPR files

We only need the DPR files for the NEXRAD rainfall data, we will use the 7zip in command line to extract files by matching a pattern. [7zip](https://www.7-zip.org/) is an open source and free file archiver tool.

Open a command window.

Win+R, then type cmd

![](images\1_zvB0iqea6FzNvdIEg37kGQ.png)

Go to the folder where all the files are downloaded,

![](images\1_V3I_q8ufl6uK7GK8tbPHog.png)

Then extract all the \*.gz files: “C:\Program Files\7-Zip\7z.exe” x \*.gz

![](images\1_UKZOWDB6eGIRN3qmjrmqaw.png)

Next we need to figure out what the DPR files look like, use 7zip to open the extracted \*.gz file, then study the file name patterns, you can see, the 3rd part of the name indicates the product “DPR”.

![](images\1_llZADQy9fTOpyLs5RBd1KA.png)

Now we can use 7zip to extract only the files with the prefix KOKX\_SDUS81\_DPR\* to the DPR folder, the command below extract all the files in the current folder to a folder on D drive with a prefix with DPR in it.

“C:\Program Files\7-Zip\7z.exe” x “NWS\_NEXRAD\_NXL3\_KOKX\_\*.tar” -o”C:\temp\kokx\dpr” “KOKX\_SDUS81\_DPR\*”

![](images\1_5joGckNSVjAA-CIqm-q1sA.png)

You should have all the files in the dpr folder now.

![](images\1_DLZGYxASX7dFrGWCkFNkZA.png)

### Setup the TSDB

Next we will load all the DPR files into a TSDB.

First, create a spatial TSDB in ICM.

As shown below, give it a name and choose a template file. You need to change the file type to (\*.\*) for the files to show up.

![](images\1_xHCOtEoUk4dWQ4KnOcYl1w.png)

Set it up as shown below, you need to check your model’s projection and extent to setup the projection and crop coordinate bounds.

![](images\1_5jYv5esdKvbr8feARzAUOQ.png)

Now we can update the TSDB from the processed files.

![](images\1_vmP5KR484nNnUOpgcnY6VA.png)

### Review the Radar Data

Click on the graph button will show a sample time series of the rainfall.

![](images\1_IHAyWY6XKG7F3ojDx5RSfg.png)

Take a note of the time of a few storms, we can then look into in the GeoPlan.

To review the radar rainfall on a map, we need to open a network. If you already have a model, just open the network. Make sure your model and your radar data are in the same projection. If they are different, make sure you set the projection conversion correctly in the TSDB settings.

To set the project of the map,

1. open the network in GeoPlan
2. set the coordinate system

![](images\1_qp5gp6l12pc_ez2ekVDLtw.png)

Then we can drag the nexrad TSDB to the GeoPlan, the database window should popup and the title bar will change with the TSDB name added.

![](images\1_bm2X7eBqbWT7B5INc42uXQ.png)

In order to view the radar data, it is helpful to turn on the radar cell boundary.

![](images\1_Gc1FG4xLrLXaymbm7cgD_g.png)![](images\1_I2HJ97hYhsZvYrZoV3Ja8A.png)

Now we should see the cell boundaries. To see the storm moving in the map,

1. graph the data
2. zoom in one event
3. go to that date
4. use cursor to move up from the row of the start of the storm, you’ll see an animation in the GeoPlan

![](images\1_pQZ3Hf47QybFlytujdrSeg.png)![](images\1_P47yc7Pj9_Xf4B_afLnEPQ.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 14, 2021](https://medium.com/p/a13e2653fa46).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-download-archived-nexrad-rainfall-data-into-a13e2653fa46)

Exported from [Medium](https://medium.com) on March 18, 2025.