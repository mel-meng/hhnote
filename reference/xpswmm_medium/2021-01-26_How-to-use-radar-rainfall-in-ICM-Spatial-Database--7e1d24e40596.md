# How to use radar rainfall in ICM Spatial Database?

Source: Innovyze Support Portal

---

### How to use radar rainfall in ICM Spatial TSDB(Time Series Database)?

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-get-historical-radar-rainfall-into-ICM-Spatial-TSDB)

![](images\1_ojz1TFmRQ0HFZ6AUZ1l4wA.png)

**Introduction**

The Nexrad radar rainfall brings high resolution rainfall to most urban areas, and the data are freely available to the public. In many places historical data as far back as 1995 are available for download.

InfoWorks ICM support Nexrad radar rainfall using spatial time series database. In this article we’ll go through the steps of downloading the radar data, and then get it into ICM.

**Archived Nexrad Website**

NEXRAD radar rainfall can be downloaded from NOAA website: <https://www.ncdc.noaa.gov/nexradinv/>  
   
 Let’s take level III data, DPR for rainfall as an example.  
   
 We need to select the station on the website. We recommend using the Select by County, City, Zip Code tool on the page. Let’s choose a station here in Portland, OR as an example shown below.

![](images\1_zEA4kR08vulbTLZaQMztjw.png)

Select the state

![](images\1_o3sNhyzcPs_JqfsevNIIPw.png)

Then select the station,

![](images\1_tkoOdMtE1Aq_Abg3CcNUNw.png)

Click on the Portland station link to view details of the station,

![](images\1_2IfTyjiNz7mUU0UnvdlAzg.png)

Add the station to cart, then view the cart for details, set up the form as shown below,

![](images\1_vMzqtiAZYaw0MWJr4Kp1ug.png)![](images\1_UtMtknCX9B2gaDKjzF6DFw.png)

In the next page, select DPR

![](images\1_1FbUtuu_BBEat7JQwWLX-g.png)

And then enter the email and place the order, it will take 30 min for the order to be ready.

![](images\1_yk3BDP_hKRe2NdS9F-jkEA.png)

A download link will be provided in the email,

![](images\1_6qulWlvP5f160b7lcLyVPA.png)

WinSCP is a good FTP client downloading the files,

![](images\1_93CmI89TSafWNB9WW8xhCw.png)

After downloading the data from the FTP site, the files are organized in different folders. For ICM to load the data, all the files need to be moved to a single folder, each file is an “image” of the rainfall for that 10 min.

**Bulk Order**

For large dataset, the above approach tends to create a very large number of files, therefore taking much longer to download the data from the FTP site. An alternative is to download all the products as zipped file, then unzip on the local computer once completed.  
 The only difference when creating the order is to select the “Compressed Archive Files”.

![](images\1_J7mYSPRGgwyVqwJqXG_foQ.png)

This will result one file for each day instead of the individual 10-min interval data.

**Scripts**

The tasks of downloading the data from NOAA website can be tedious and time consuming, Two scripts were created to automate the process.  
 Get\_NEXRAD.bat uses WinSCP to download the files directly from the FTP site to a local folder.

@echo off  
 echo — — — — — — — — — — — — — — — — — — — — — — — — — — — — —   
 echo Script for pulling the latest radar data from an FTP site  
 echo Requires local install of WinSCP  
 echo <https://winscp.net/eng/index.php>  
 echo NEXRAD site codes:  
 echo <https://www.roc.noaa.gov/wsr88d/Images/WSR-88DCONUSCoverage1000.jpg>  
 echo — — — — — — — — — — — — — — — — — — — — — — — — — — — — —   
 echo.  
   
 rem — Define local paths and desired window for pulling files.  
 set “datapath=D:\Data\Passaic\_Valley\NEXRAD\”  
 set “logpath=D:\Data\Passaic\_Valley\NEXRAD\\_logs\”  
   
   
 rem — Call WinSCP to pull requested window of files from FTP to local folder  
 “C:\Program Files (x86)\WinSCP\[WinSCP.com](http://WinSCP.com)” /ini=nul /log=”%logpath%\WinSCP.log” /loglevel=-1 ^  
 /command ^  
 “open ftp://ftp.ncei.noaa.gov/pub/has/HAS011624076/"" ^  
 “get NWS\*.\*>%window% %datapath%” ^  
 “close” ^  
 “exit”  
   
 rem ftp://anonymous:pw@tgftp.nws.noaa.gov

Unzip\_nexrad.bat will using 7zip to unzip the downloaded \*.gz files in the same folder, and then only unzip the DPR files.

“C:\Program Files\7-Zip\7z.exe” x \*.gz  
   
 To unpack the DPR files from all tar files:  
   
 “C:\Program Files\7-Zip\7z.exe” x “NWS\_NEXRAD\_NXL3\_KOKX\_\*.tar” -o”D:\Data\Passaic\_Valley\NEXRAD\DPRfiles” “KOKX\_SDUS81\_DPR\*”

#### Preparing the data in one folder

Once all the data are downloaded, they need to be placed in a single folder for ICM to load. Depending on your method of acquiring the data, you may need to filter and move the data.

Since NEXRAD has so many products, it is quite possible to have other data downloaded, make sure all your files in the data folder has the right prefix indicating they are DPR rainfall data, for example, **KOKX\_SDUS81\_DPR\*.** The prefix varies depending on the station. If all the data are organized in subfolders, then they need to be moved to a single folder. You can use windows command to filter and move the files. Or using file explorer to filter your data,

* **\*.\*** will query all the files in all the folders
* **\_DPR** will filter all the files with DPR in its name

![](images\1_fE4vhf0Kkf7C5uOi_fkkOg.png)

**Import archived Nexrad Data**

Create a new spatial TSDB, and set the path to the folder where all the DPR files are downloaded. Change the file to \*.\*, the sn.\* is for live data.

![](images\1_yzpPkCB5n-4unDJjiH3pdg.png)

If your model is a small area, we need to clip the data to our area only to reduce the size of the file.

![](images\1_kIjjKqStc6xLiviPHlHkSg.png)

Then update the data to load the data into TSDB.

**Verify Rainfall Sources**

It is good practice to compare the radar data with other sources. If we don’t have local rain gauges, historical rainfall data can be found at weather underground: <https://www.wunderground.com/history>  
   
 We can use the daily total rainfall as a quick check of the general timing and totals of the radar data.

**Weather Underground**

Search for a station

![](images\1_uWsNV7EGswXffwA1VcMuVQ.png)

Then switch to monthly history,

![](images\1_GXbuUtMeJe_oTYGHTv7qZg.png)

At the end of the page is has daily total rainfall.

![](images\1_lmwBJ6P-3uPSOxR58DwX1w.png)

As shown above, we should have around 2.02 in of rain for 2/6/2017 at Portland station.

**Convert CSV file to TSDB**

TSDB can load csv files into the TSDB, we’ll use the batch csv file format, which is a csv file with fixed columns, it has no header.

**Batch CSV file format**

The columns are: site name, datetime, value

![](images\1_SCF_mrIN6Q3oNKWnwVszEw.png)

CSV files can be easily created, converted in Excel. For the date field use the “yyyy-mm-dd hh:mm” format.

![](images\1_12LpKZSR3mHWOQt2H7BfOg.png)

Setting batch csv data source,

* It is very important to set the time zone in the data source tab.
* Give it a name, and path to the csv file

![](images\1_VOsygDGcHfqbVNxwp0IYNA.png)

**Verify the rainfall**

Setup a simple hydrology model with a few basins in the study area, so that we can get rainfall data aggregated from the NEXRAD data. Make sure the time zone is setup correctly.

![](images\1_4q76lLAwxfsjda9JpYPKvQ.png)

For nexrad rainfall, simply drag the TSDB into the run.

![](images\1_GZu0dDOpZ63SzbfZwtheFg.png)

For rain gauges, TVD polygons need to be added to the model.

![](images\1_3nXFpMqRjtvo0wvCln_DAw.png)

Run both models, and then compare the results.  
 Check the timing and total.

![](images\1_06TfQCgP0LnDgzudY8xqzQ.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [January 26, 2021](https://medium.com/p/7e1d24e40596).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-use-radar-rainfall-in-icm-spatial-database-7e1d24e40596)

Exported from [Medium](https://medium.com) on March 18, 2025.