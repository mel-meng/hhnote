# Graphical Encoding and Spatial Report

source: Innovyze Support Portal

---

### Graphical Encoding and Spatial Report

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Graphical-Encoding-and-Spatial-Report-in-XPSWMM)

Present modeling results in maps with symbols and labels is an important task for any modeling projects.

For large models and professional quality figures with unique branding and looks, exporting the modeling results into a GIS package will be needed for the finer touches.

However, for small projects and a quick check of the modeling results, the overhead of exporting results to GIS is simply too high and XPSWMM has all the tools you’ll need to style the map and label the maps with just a few clicks.

To change the symbols of nodes and links, we’ll use the graphical encoding tool, and for advanced labeling, we’ll use the spatial report tool.

You can download the sample models for [graphical encoding](https://github.com/mel-meng/xpswmm/tree/master/models/graphical_encoding) and [spatial report](https://github.com/mel-meng/xpswmm/tree/master/models/spatial_report_example) on GitHub.

These tools can be accessed on the toolbar and in the layer tree.

![](images\1_6wK6qNcy4ViwbAhlSSvFqA.png)

**Graphical Encoding**

![](images\1_y-t-omQ4DAcQ12gCVW0Xmg.png)

Graphical encoding styles the nodes and links based on the object’s attribute values. To start the Graphical encoding window, we can either right click on the “Graphical Encoding” tree item or click on the icon in the toolbar.

Each row in the window controls one aspect of the symbol. For example, the first row is for node color.

![](images\1_QGQ5YFIWOqWisnVBufwCvg.png)

To set the node color symbols,

1. Select a variable to show, the freeboard

2. Click on the node color to set the color ramp

3. Use the suggest button to automatically get a range

4. Modify if needed the color and range

5. Click OK to finish

![](images\1_nwzqnwmEpMjkpuvnoaNKrQ.png)

To add a legend,

1. click on the legend button.

2. Change the title

3. Select a background

4. Pick the location on the screen

5. Click OK

![](images\1_z7yAjeUk-IbxcIHfvaky3g.png)

**Spatial Report**

![](images\1_c6wzPLlLmhrA9UbQHKomyQ.png)

For advanced labeling, we use the spatial report tool, which is an addition to the link and node labeling. Spatial report tags have leader lines to the object.

To start the spatial report window, we can either right click on the “Spatial Report” tree item or click on the icon in the toolbar.

![](images\1_X_1WPpEX1aVzxtqCrbqC-A.png)

As shown in the report attributes window, we define the attributes/variables, and the look of the “tag”/frame for links and nodes.

**Setup the spatial report**

![](images\1_TB5cUGQXZTQWkDPaY_yLSg.png)

And for the variables, we also define its label/Mnemonic and unit in the variable list window.

Once the tags (spatial report) are created, we can adjust the location by moving the tags.

![](images\1_z072_XWrE-Rn9RB7t3ERhA.png)

We can also define the behavior how the tags are turned on or off by right click on the Spatial reports tree items.

![](images\1_KKEH1Vtp5fgmiD_9XfpTRw.png)

For example, if “Show Spatial Reports as Tooltip” is selected, only when we hover the mouse on the object the tag will show. This can be great when interactively checking the modeling results.

**Quick Data View**

![](images\1_weAYd2d9A9gKznr3kdhARg.png)

In addition to the spatial report, we can also use “Quick data view” to show attributes of the selected model element in its own window. To show the attribute table, click on the icon on the toolbar.

![](images\1_X9Vt4BG-G54yQ8lELXZHfQ.png)

We can change the default table for node, link, and how multi-link should be displayed in the attributes window.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [November 3, 2020](https://medium.com/p/9b370f99cd27).

[Canonical link](https://medium.com/@mel-meng-pe/graphical-encoding-and-spatial-report-9b370f99cd27)

Exported from [Medium](https://medium.com) on March 18, 2025.