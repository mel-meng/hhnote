---
title: How to batch import subcatchments into XPSWMM from external data source
---

# Introduction

When building large hydrology models, you might find it easier to prepare the subcatchments input parameters in GIS or CAD software. Two commonly used methods to get external data into XPSWMM are “import from GIS” and “GIS Link”. Most users are familiar with the “import from GIS”, but the “GIS Link” tool is a more suitable tool as it can help us to confirm the required data format and correct matching fields.

In this article we’ll use Clark hydrology as an example to illustrate a complete import workflow.

- Use XPTables to match the fields

- Use “GIS Link” to confirm the correct data format

- Use “GIS Link” to import the subcatchments attributes to existing nodes

- Use “Import from GIS” to import the polygons for the matching subcatchment

# Clark Hydrology

The Clark hydrology method is one of the less used methods XPSWMM supports, finding the right data format and matching field can feel overwhelming even for experienced users. As shown in the figure below, the first step is to identify the field names that matches all the UI elements.

<img src="./media/image1.png" style="width:6.5in;height:3.90556in" alt="A screenshot of a computer Description automatically generated with medium confidence" />

# Map the fields using XPTable

The best way to establish the mapping is using an XPtable.

1.  Go to XPTables

<img src="./media/image2.png" style="width:1.76481in;height:0.4032in" alt="A screenshot of a computer Description automatically generated with medium confidence" />

2.  Create sub catchment table

<img src="./media/image3.png" style="width:3.15331in;height:2.20801in" alt="Graphical user interface, text, application, email Description automatically generated" />

3.  Map the fields found in the UI

<img src="./media/image4.png" style="width:4.36882in;height:3.57347in" alt="Graphical user interface, text, application Description automatically generated" />

4.  There are hundreds of parameters, and it could take some time and effort to locate the correct parameter. One trick is to get the internal field name. You can get the name of a UI element by hovering your mouse over it. And you can check the field name in XPTable using the “Info” button.

<img src="./media/image5.png" style="width:6.5in;height:3.6375in" alt="Graphical user interface, text, application Description automatically generated" />

# Create a GIS Link

The next step is to figure out the right data format for each field. For example, the dropdown list values found in the XPTables uses index instead of the full label, and we need to find what the index is for “Unit Hydrograph” and “Clark Hydrology”. We will need to recreate the same XPTables in “GIS Link”, then we can export a sample table to check the correct values, and then use the same link we can import the data back into XPSWMM.

1.  Create an excel table, and paste the XPTable into a tab

<img src="./media/image6.png" style="width:6.5in;height:2.50694in" alt="Graphical user interface Description automatically generated" />

2.  Create a new GIS link to that table

<img src="./media/image7.png" style="width:1.84252in;height:1.53543in" alt="Graphical user interface, application Description automatically generated" /> <img src="./media/image8.png" style="width:2.92864in;height:3.05869in" alt="Graphical user interface, application Description automatically generated" />

3.  We’ll do both import and export. To keep things simple, we only update on existing objects only.

<img src="./media/image9.png" style="width:2.59674in;height:2.23582in" alt="Graphical user interface, application Description automatically generated" /><img src="./media/image10.png" style="width:2.61167in;height:2.24868in" alt="Graphical user interface, application Description automatically generated" />

4.  For the object, it should be “Node”, and the mapping is very similar to the XPTable dialogs.

<img src="./media/image11.png" style="width:2.76463in;height:2.38038in" alt="Graphical user interface Description automatically generated" /><img src="./media/image12.png" style="width:3.12073in;height:2.48708in" alt="Graphical user interface, application Description automatically generated" />

5.  Once we finished setting it up, we can export the data to the excel table.

<img src="./media/image13.png" style="width:3.4505in;height:1.68978in" alt="Graphical user interface, text, application, email Description automatically generated" />

6.  As shown below, we can see the routing method and unit hydrograph index values are 4 and 7. And that is the value we should use when we import the data back.

<img src="./media/image14.png" style="width:6.5in;height:0.71736in" />

# Prepare the import table

The next step is to populate the excel table for import. When a node has more than one subcatchment, importing subcatchments into XPSWMM might not work correctly. Make sure in your import table, each node has only one subcatchment. Using the exported values from “GIS Link”, prepare the import table accordingly.

# Import the subcatchments into XPSWMM from the excel table

First, make sure all the nodes to be imported are added to the XPSWMM model.

Next, we use the GIS Link tool to import the results into XPSWMM. This should updates all the nodes with the right Clark hydrology information.

<img src="./media/image15.png" style="width:3.01946in;height:2.46996in" alt="Table Description automatically generated" />

# Import from a different spreadsheet

You might want to only import part of your model each time. Instead of recreating a new “GIS Link”, you can use the “Configure..” tool to connect to a different excel table.

<img src="./media/image16.png" style="width:3.52937in;height:3.82623in" alt="Graphical user interface, text, application Description automatically generated" />

# Import the polygon of the subcatchment

The last step is to add the polygons of the subcatchments using the “Import from GIS” tool. You should have the “node”, “subcatchment no” values populated before importing the subcatchment layer.

1.  Import subcatchment from GIS

<img src="./media/image17.png" style="width:4.44736in;height:2.1039in" alt="Graphical user interface, text, application, chat or text message Description automatically generated" />

2.  Select the polygon, and it should have the following fields.

<img src="./media/image18.png" style="width:3.47652in;height:1.69438in" alt="Graphical user interface, text, application, email Description automatically generated" />

3.  The node name is the node it drains to, and the catchment number is the position from 1 to 5.

<img src="./media/image19.png" style="width:6.5in;height:2.94375in" alt="Graphical user interface, application Description automatically generated" />

This will import the matching polygons for the subcatchments.

# Conclusion

By combining the “GIS Link” and “Export to GIS” tools, you can quickly confirm the correct data format the matching field names to prepare and import subcatchments data into XPSWMM from external GIS and table sources.
