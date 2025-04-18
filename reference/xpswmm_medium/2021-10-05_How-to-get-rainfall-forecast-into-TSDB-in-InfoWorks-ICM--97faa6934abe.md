# How to get rainfall forecast into TSDB in InfoWorks ICM?

Source: Innovyze Support Portal

---

### How to get rainfall forecast into TSDB in InfoWorks ICM?

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-get-rainfall-forecast-into-TSDB-in-InfoWorks-ICM)

NOAA provides free rainfall forecast for most of the place in the United States, anyone who has a TSDB can load that data into ICM and take a peek into the next 18hrs into the future.

### Introduction

The High resolution Rapid Refresh ([HRRR](https://rapidrefresh.noaa.gov/hrrr/)) is a NOAA real-time 3-km resolution, hourly updated, cloud-resolving, convection-allowing atmospheric model, initialized by 3km grids with 3km radar assimilation.

The web page can be quick intimidating for a Civil Engineer with lots of jargons. But don’t worry, all you need to know is that there is a very simple Web API that you can call to download the forecast files.

Every hour, NOAA releases the HRRR files gradually into the next 18 hours to the web one file a time (each file is for one hour). All we need to do is to download these files just in time then run the simulation with the weather forecast.

### Spatial TSDB

ICM manages HRRR data in a spatial TSDB as shown below,

1. Each hour, a set of forecast files are imported into the TSDB
2. It has 18 files, each file represents the hours into the future from the origin time (1 first hour into the future, 18 is the 18th hour)
3. Each file consists 520 cells (squares) in this example, and each square has the value of the rainfall for that hour

![](images\1__Ag-3hX06npzlVPdeSmMgw.png)

To get HRRR into ICM, here are the steps,

1. setup an HRRR TSDB
2. download the HRRR files to the data folder
3. load the downloaded files into the TSDB

### Setting up the HRRR TSDB

The first thing is to create a HRRR TSDB to store the rainfall forecast data.

An HRRR TSDB has the following settings,

1. ICM support the HRRR grib file format
2. We would like to use all of the 18 hours forecast. You can choose a different number if you don’t need to forecast all the way to 18hr into the future
3. The folder where the forecast files to be downloaded
4. Convert the rainfall cells to the same projection as the model and limit to the model extent

![](images\1_VjkKuIT6VHBCyO6ZmrNv4g.png)

### Download the HRRR files

NOAA web API for HRRR is quite easy to use,

* each day the grib files are released to a folder using the date
* the file name is created using the origin and leading hours
* for example, for the 18 hours of forecast at UTC time 20:00, the files look like: hrrr.t20z.wrfsubhf##.grib2, where ## is from 01–18.

![](images\1_lzeOEhCSr0sDOMF-SpiEcw.png)

Apparently, manually creating all the URLs, and download them individually is not practical if you plan to do this on a hourly basis. Below is a sample powerscript code, you can run it anytime, and it will try to download the 18 files forecast for that hour.

---

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

# Run this script ~25 min after each hour of the day.

# Run the script at an interval of 15 min

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

# Set the execution policy for the current PowerShell session

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

# Specify Local Inputs -

# — Lat-Lon window, and Local file path

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

$Lon\_min = -74.546

$Lon\_max = -73.710

$Lat\_min = 40.437

$Lat\_max = 41.164

$Local\_Path = “F:\DATA\HRRR2\”

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

# Get current UTC hour in string format

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

$now = [DateTime]::Now.AddHours(-1) # minus 1 since files are 50–80 minutes late

$Hour = Get-Date $now.ToUniversalTime() -format HH

$today = Get-Date $now.ToUniversalTime() -format yyyMMdd

[string]$Hr\_Char = “{0:D2}” -f ($Hour) # This bit converts hour to 2 character string with zero in front if needed

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

# Prepare other inputs

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

$str1 = “https://nomads.ncep.noaa.gov/cgi-bin/filter\_hrrr\_sub.pl?file=hrrr.t"

$str2 = “z.wrfsubhf”

$str3 = “.grib2&var\_PRATE=on&subregion=&leftlon=”+$Lon\_min+”&rightlon=”+$Lon\_max+`

“&toplat=”+$Lat\_max+”&bottomlat=”+$Lat\_min+”&dir=%2Fhrrr.”+$today+”%2Fconus”

$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession

# last step, check if all the files are downloaded

# if so, create a file with the origin time and next time when the script runs it will terminate the script

$check\_file = $Local\_Path + “HRRR\_”+$today+”\_”+$HR\_char+”.txt”

$flag = “complete”

if (Test-Path -Path $check\_file)

{

write-output “completed, exit”

exit

}

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

# Loop for each forecast hour

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

For ($i=1; $i -le 18; $i++) {

if($i-lt10){$fhr=”0"+$i}else{[string]$fhr=$i}

$url = $str1+$HR\_char+$str2+$fhr+$str3

$output = $Local\_Path + “HRRR\_”+$today+”\_”+$HR\_char+”\_”+$fhr+”\_.grib”

if (-not (Test-Path -Path $output))

{

write-output $url

write-output $output

Invoke-WebRequest $url -WebSession $session -TimeoutSec 900 -OutFile $output

}

}

---

### Automate the data download

For LIVE modeling, download the data needs to be automated. This is usually done using the dataloader services.

It involves the following steps,

1. setup the scripts
2. add auto-update information in TSDB settings
3. turn on dataloader services to run the scripts at specified intervals

To run the powerscript from ICM, we’ll need to create a bat file first.

![](images\1_o6-mY4U4hqK0h8MGVmteCw.png)

In the TSDB, we then reference to the bat file, then set the interval of running the simulation at every 15 min.

We can also use the triggering file instead of running the simulation at fixed intervals. In this case, we provided a triggering file just as a way to trigger an update by manually save the trigger file.

Once we turn on the dataloader services, it will run the script every 15 min, and try to load the HRRR files into the TSDB.

![](images\1_gRCpYzT-k14uoizCAMCLsg.png)

### Manual Update

If you don’t have ICMLive, or you don’t need to have a fully automated setup. You can do this manually,

1. run the powerscript file to download all the data into the HRRR TSDB file folder
2. Manually update the file

![](images\1_Db6ucLXAd5-IeYFUec5Ayw.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 5, 2021](https://medium.com/p/97faa6934abe).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-get-rainfall-forecast-into-tsdb-in-infoworks-icm-97faa6934abe)

Exported from [Medium](https://medium.com) on March 18, 2025.