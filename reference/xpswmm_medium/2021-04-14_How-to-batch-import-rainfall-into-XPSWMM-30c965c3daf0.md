# How to batch import rainfall into XPSWMM

source: Innovyze Support Portal

---

### How to batch import rainfall into XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-Batch-Import-Hydrographs-into-XPSWMM)

Manually getting a large number of rainfalls into XPSWMM can take quite some time. In this article we will show the step by step instruction on using the XPX exchange format to import rainfall data.

Major steps are,

1. manually create one template rainfall global database entry
2. export the rainfall to XPX format
3. review the format of the XPX data and develop the steps to convert the source data to the XPX commands
4. automate the conversion

### Create template rainfall in XPSWMM

Start with a new model and add the rainfall into the global data.

![](images\1_NfZmYHDRDP5a9f8ME0MfhQ.png)![](images\1__YSgjlIYtEvebh9ndS5oug.png)

Then enter the data, it is important to review the data and correct any errors identified.

![](images\1_8NCdCCBEx690yvNJYkmScA.png)

It is also a good practice to setup a simple model and make sure the rainfall is generating expected results before moving ahead to automate the import process. As shown below, a single node RNF model is developed to make sure the response is reasonable.

![](images\1_Ly2nUDrAeOqlYyRQH_vTmA.png)

### Export to XPX

Use the export to XPX tool to generate the XPX file for the template rainfall data entry.

![](images\1_Duhojda4Mg_TYae0MnG94A.png)

We only need to export the rainfall, so we can turn off everything else.

![](images\1_1qUG0J8nra3CTYl-62AWRg.png)

### Map data to the XPX Commands

As shown in the comparison of the XPX and the user interface,

1. the XPX commands for each rainfall consist many rows of command, each command set one of the parameters. The syntax is quite easy to understand, refer to the [global database commands](https://help.innovyze.com/display/xps/XPX+Format+File#XPXFormatFile-GLDB) for more details.
2. most of the commands are the same for different rainfalls, the only thing that changes are, the name of the rainfall, the 3 columns of the rainfall data

![](images\1_A9UTxphNMjTJ1XSLqwbPiw.png)

With that understanding, we can develop an automated process below,

1. prepare the input data: a table with 3 columns of the rainfall data, and a name for the profile
2. prepare a template with all the commands and place holders for 3 rows of data and the name of the rainfall profile
3. replace the placeholders in the template with the values of the profile
4. repeat for each profile

I’ll show an example using excel.

### Excel Example

You can find the files on [GitHub](https://github.com/mel-meng/xpswmm/tree/master/models/rainfall_xpx).

![](images\1_AzCNP6_HBqzCJZHuFLnKeQ.png)

In the example excel file, we add the source data in the “test\_rainfall” tab, it has 3 columns and should be ordered as shown below. The order is hard coded, if you need to change the order, modify the formula accordingly.

![](images\1_YTKSXIGzUbehX9OiFkPYmQ.png)

The conversion is done in the template tab.

The only input is cell E1, the tab name of the data source. The following rows 2–6 calculates the number of rows and the ranges of each column.

Next section is the template of the XPX commands, the tricky part is to make sure all the quotes are included.

All the orange cells are placeholders that are updated from the source data.

![](images\1_Qt9CKIrpf5xc2sE5COJrxg.png)

The next step is to select all the green cells, copy and paste it into a text file.

![](images\1_mJev8Durz_wPRKLqVcPU7A.png)

And then import it into XPSWMM.

![](images\1_DvOmwNYSADeBflxU7DqUsQ.png)![](images\1_dbU47SOWFABhv9Odriim7g.png)

This example shows how to create one profile from the source data. To batch convert the data, more advanced programming might be needed, and in a future article, we’ll see how we can use python to automate such tasks.

### Python Example

With python, it is fairly easy to write a script to automate this task.

You can find the source code on GitHub below.

[**mel-meng/xpswmm**  
*Contribute to mel-meng/xpswmm development by creating an account on GitHub.*github.com](https://github.com/mel-meng/xpswmm/blob/master/models/rainfall_xpx/rainfall_xpx.py "https://github.com/mel-meng/xpswmm/blob/master/models/rainfall_xpx/rainfall_xpx.py")

The input table is structured as below,

* station is the name of the station
* columns B, C, D are the rainfall pattern data

![](images\1_NM13rwzsy68TJaZ9W5mnzg.png)

To run the script, install python with pandas library.

If you don’t have python already installed on your computer, you can try [Anaconda](https://docs.anaconda.com/anaconda/install/) which simplifies the installation of all the dependencies.

Download the script,

* update the folder path where the input csv file is located for “ws”
* update the csv and xpx file names
* run the script will generate an xpx file

![](images\1_v8hN9rF6qxMS8KG7lbo9Kg.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 14, 2021](https://medium.com/p/30c965c3daf0).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-batch-import-rainfall-into-xpswmm-30c965c3daf0)

Exported from [Medium](https://medium.com) on March 18, 2025.