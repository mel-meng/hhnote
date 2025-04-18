# How to import/export model nodes/pipes using shapefiles in XPSWMM

source: Support portal

---

### How to import/export model nodes/pipes using shapefiles in XPSWMM

source: [Support portal](https://innovyze.force.com/support/s/article/How-to-import-export-model-nodes-pipes-using-shapefiles-in-XPSWMM)

Nodes and pipes in XPSWMM/XPSTORM can be easily imported or exported using shapefiles using the built in tools.  
The import tool can import shapefiles from the GIS database to build model network, and the export tools can be used to export results to GIS for more advanced mapping.

### How does it work?

An easy way to visualize the process is to treat the shapefile and the XPSWMM model as two tables.  
For example, the shapefile is a table with a few columns,

![](images\1_EfxmJ0J2QAgTKrF1Sw-BXA.png)

And we need to import this shapefile into XPSWMM

![](images\1_xcVoAJ5znmV8MPHeZcNHqQ.png)

And the export is the reverse process to get the table in XPSWMM to be saved in a shapefile table.  
   
To make the import work, we’ll need the following defined,

* First we need to match the rows in the two tables using a primary key, the value uniquely identifies the row. In this case it is the “name” field in the shapefile and the “Node Name” field in the XPSWMM table, which uniquely identifies a node in the two tables. Node1 row in the shapefile table is the same as the Node1 row in the XPSWMM table.
* Once the row is matched, a mapping is needed to convert the field value from the shapefile table to the XPSWMM table, for example “x” in the shapefile table for Node1 row is imported as the “Node X” cell in the XPSWMM table.

For export, it is the reverse writing data from the XPSWMM table to the shapefile.

### XPTables

Before getting into the import/export procedures, we need to get familiar with XPTables, which exposes the internal data structure of XPSWMM models for the user to create customizable tables. The mechanism of mapping the fields between XPSWMM and Shapefiles and other external sources relying on this functionality of XPTables.  
   
Click the XPTables icon to start the XPTable list

![](images\1_60jeGbZO1RUn62h8ReYRCA.png)

To create a new node table,

* Select the “Node Tables” folder
* Click Add button
* Using the “Variable Selection” window to add the field into the list of table headers. Most of the common model attributes can be found under the Hydraulics Node > HDR Node Data
* Use the tools to create a list of table columns
* Click OK to create the table.

![](images\1_NKrldtpshA1lfwTaS6Bm8A.png)

Once a table is created, you can use the “Setup Table Variables” tool to go back to the window above to change the table.

![](images\1_sCxNwS-UBes48DxGgQ_8RA.png)

### Export node layer to shapefile

Both importing/exporting tools can be accessed by right click on the **Nodes** or **Links** layer.

![](images\1_AobAuKRlFt9p71QHWRB56Q.png)

To export the node layer as shapfiles,

* Right click the Nodes layer > Export to GIS File …
* Go to the export folder and name the shapefile
* Using the “>” button to add the field from the list
* a. Node Name, x, y
* b. Hydraulics > HDR Node Data > Invert Elevation/Ground Elevation
* Change the custom name following shapefile naming convention
* a. name, x, y invert, rim

![](images\1_cvOn_TtNFOaxKKasc0TiNw.png)![](images\1_uICx6dR-hZBurzOOTaWu9w.png)

### Import Node from shapefile

Before importing shapefiles into XPSWMM, it is recommended to create a corresponding XPTables,

* So that you can check the imported data quickly
* To make sure the values in the shapefile are properly prepared, for example, using the XPSWMM code for shape of pipe, and using the same units for pipe size, inverts, etc.

Right click on **Nodes** layer

![](images\1_TGCPttTxRX_CVGolesmqSQ.png)

* elect the shapefile
* Click import
* Set node name field (primary key to match the rows)
* Set field mapping, “Field” column is the field in the shapefile, “XP Variables” is the field the values will be imported into.

![](images\1_mKtFU2K5T4ZvOXIBe68KIg.png)

### Export Links layer to shapefile

Right click on the Links layer,

![](images\1___nqXORK-KrA7ssw37YTHw.png)

Export window,

* Go to the folder and name the new shapefile
* Select the field, common link attributes can be found under Link > Link Data > Conduit Data
* Rename the custom Name column to comply with shapefile naming convention (short simple names)

![](images\1_zGIQB29nChpMDjQXvQ0nJw.png)

### Import Links from Shapefile

To understand the data format, open an existing model, or create a few sample links.  
Then create an XPTables for links to check the format of the data. For Shape, it is coded as “Circular”, and the units are shown in the table header.

![](images\1_rfTQ0IXg8AnzWt-9Z2cKqg.png)

Right click the Links layer,

![](images\1_zqBQma6BJy2w9xu2xCch0w.png)

Import links from shapefile

* Locate the links shapefile file
* Click import
* Set link names as the “name” field in the GIS (primary key, matching the rows)
* Link End Points, XPSWMM will automatically assign the node for links on the end of the link
* Map the field from shapefile to the XPSWMM table

![](images\1_vxIzAr0BPofuSyBRqv4OcQ.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 29, 2020](https://medium.com/p/90650b8a4a24).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-import-export-model-nodes-pipes-using-shapefiles-in-xpswmm-90650b8a4a24)

Exported from [Medium](https://medium.com) on March 18, 2025.