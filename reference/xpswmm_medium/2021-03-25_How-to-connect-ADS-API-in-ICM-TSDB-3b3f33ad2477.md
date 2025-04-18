# How to connect ADS API in ICM TSDB

Source: Innovyze Support Portal

---

### How to connect ADS API in ICM TSDB

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-connect-ADS-API-in-ICM-TSDB)

ICM TSDB provides a streamlined process for getting external monitoring, forecasting time series data into the ICM model. Once the external connection is setup, the retrieval of the data is automated. When ICM runs a model, it automatically pulls the needed input data from the sources. When the run completes, it automatically pulls the data for comparison/calibration. For utilities with permanent flow meters in ground, a TSDB enabled workflow can eliminate tedious data preparation work which can easily take hours to days for each model run. These efficiency gains will enable and empower the utility to gain more insights into the system by running the model more often with real data.  
   
Many utilities are using ADS’s flow monitoring platform managing flow monitoring data. ICM TSDB (Time series database) supports direct connection using ADS API for flow monitoring data. Once the TSDB is setup, the modeler can easily build TVD connectors to bring the ADS data into the model as input and calibration data.  
   
**Connect to ADS API**  
   
ICM uses the ADS API for pulling the data into TSDB, for more information about ADS API, refer to the official API page:  
<https://api.adsprism.com/swagger/index.html>  
   
Before setting up the connection, you need to contact ADS to get the developer or API key. It is a long string of text, something looks like this:  
**MQQzMTQxRTItMUN0Ni00QUZFLTaCMDktNzAyRTlFQsMxQTY5**  
   
**Database sources tab**  
A sample of the **database sources** tab is shown below,

![](images\1_hXiQSXtGR7-h83t5yaK4Ow.png)

Server: <https://api.adsprism.com>  
Database: api/Telemetry  
Password: the developer key, it is a very long string of text.  
Time zone: it is also important to set the time zone. If left blank, the system will assume it is the same as the computer’s time zone, which can change (for example using VMs hosted in a different time zone).  
**NOTE: ICM always uses standard time for the simulation, therefore all the data coming into the model needs to be in standard time (daylight saving time needs to be adjusted.)**  
   
**The observed tab**  
A sample is shown below, most of the fields can be set using the information from the ADS website.

![](images\1_W7PRR54Z_C1fqI0sEFZgyA.png)

For the connection, fill the following fields,

* External data source: the database connection entry data source name
* Table: pick the location, the list should populate automatically

![](images\1_hyrB_jIXrAlNkzSsNQeXOQ.png)

* Data Column: the field to be used, for example QFINAL, DFINAL, VFINAL for final flow, depth and velocity. The list should populate automatically.

![](images\1_lcXqGSN_NYr_gUxDmFHmgQ.png)

**Troubleshooting connection**  
   
A common issue when setting up the connection is errors introduced when copy and pasting the url and passwords. Make sure no extra space and line break is copied. If copying from an excel table, try not to copy the cell which might include a tailing line break. Instead, get into the cell and copy the text.  
   
Another issue is the information provided might not be correct, and verify the connection information, follow the instruction below to test the ADS API.  
   
**Test ADS API**  
   
ADS has an official API page, where the user can test the API: <https://api.adsprism.com/swagger>

* Authorize

![](images\1_WOHzUdkjzNUI8NdCFE2s9A.png)

* Get a list of the values reported. For example QFINAL is the flow for a meter, and its ID is 2303. We will need this ID when querying for the time series data.

![](images\1_T96UOcuJEahRp0LIEUWjIQ.png)

* Get a list of locations

![](images\1_4_za5-Au187fYTNTwKmS3A.png)

* We will need the ID for each flow metering location for the telemetry query, as shown below in the response, we have two sites with the IDs of 70 and 171.

![](images\1_N-HdGzF762j8uR9aocIAjA.png)

* Query the time series for location 171 of QFINAL (2303) from 3/20–3/25/2021

![](images\1_CIF8FnUpjPCe25NtrCzG3A.png)

And here we got the response below.

![](images\1_D--TyKi0ruVbCcF9rw-BUg.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [March 25, 2021](https://medium.com/p/3b3f33ad2477).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-connect-ads-api-in-icm-tsdb-3b3f33ad2477)

Exported from [Medium](https://medium.com) on March 18, 2025.