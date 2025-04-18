# How to import multi-link from a table into XPSWMM

source: Innovyze Support Portal

---

### How to import multi-link from a table into XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-import-multi-link-from-a-table-into-XPSWMM)

XPSWMM has many ways to bring external data into the model. Most of them can be accessed through the **Import/Export Data**

![](images\1_RmZB5vCU-POKxNJ3-ss-Qg.png)

For GIS files, most of the import/export tools can be accessed by right click the item in the layer tree panel.

![](images\1_a9Jcghy1A-Vg6LLtsmcClA.png)

### What is Multi-link

[Multi-link](https://help.innovyze.com/display/xps/Multiple+Conduits+or+Diversion+Links) is XPSWMM specific feature no other software offers. Multi-link is used for two situations,

* parallel pipes between two nodes, a common one is dual drainage, a pipe and the street section that both convey storm water
* pumps, weir, orifice and other diversion structures

Multi-link presents a challenge when importing data from external sources, because in XPSWMM muli-link is treated as a group entity with multiple children, however, usually the data in the external source are not grouped. Therefore, importing multi-link from external sources will require a slightly different process.

Before getting into the steps of importing multi-link, modelers who are building dual drainage system might also want to check the [dual drainage automation tool](https://innovyze.force.com/support/s/article/How-to-setup-dual-drainage-in-XPSWMM), which might be a more intuitive way of building drainage system.

### Import/Export External Databases

To import/export multi-link data with external data, use the tool below.

![](images\1_bVq-UdLv_-RJ6s1UBQY7Og.png)

Create a new connection to an excel table.

![](images\1_LskFLx4xKnFZDEMkobGZSA.png)

For a two way import/export, you can set it up like this,

![](images\1_2tWJU0Dkqv56L5PQWpkBkA.png)

The last step is to map the key columns in the table so that XPSWMM knows how to import each row. Make sure,

* Link Name is the multi-link name
* Channel/Conduit is the name of the individual pipe/channel

![](images\1_x0PdwY5wPnMMa7rskyxHsA.png)

Next, set up the mapping for the values to be imported.

![](images\1_sz0vYVDsigJ9_s7ncOKqHg.png)

When the mapping is done, use the Import/Export button to get the data into or out of XPSWMM.

![](images\1_s-Qa62vmxiq_tWOD69Z70A.png)

You can find the sample model on [GitHub](https://github.com/mel-meng/xpswmm/tree/master/models/multi_link).

### TIPS

Figuring out the field mapping can be tricky, it will take some trial and error. Therefore, it is highly recommended started with a very simple model and a sample table with just a handful rows to test the mapping before working with the full dataset.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 27, 2021](https://medium.com/p/a1592a25c74f).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-import-multi-link-from-a-table-into-xpswmm-a1592a25c74f)

Exported from [Medium](https://medium.com) on March 18, 2025.