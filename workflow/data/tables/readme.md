---
title: Share a customized workflow in ICM
---

# Introduction

Finding a piece of information quickly in the huge data grid in ICM can be challenging. Especially if you are new to ICM.

The good news is that you can quickly load a customized grid view from a previously saved SQL query to fit your own modeling needs.

In this article, you’ll learn to create custom SQL queries,

-   Setup customized grid view with full editing support for SWMM5 runoff method

-   Setup customized SWMM5 style hydrology results summary

# Customized workflow

Setting up SWMM5 runoff method in ICM can be quite complicated for new users. So we simplified the workflow using SQL queries. You can download the model from Github.

1.  Open the network

2.  Drag step 100 to the GeoPlan

<img src="./media/image1.png" style="width:6.5in;height:3.03403in" alt="Graphical user interface, application, Word Description automatically generated" />

Then you have a fully functional grid for subcatchment to make changes with only the fields that matters for the SWMM5 hydrology,

<img src="./media/image2.png" style="width:6.5in;height:2.08889in" alt="Graphical user interface, application, table, Excel Description automatically generated" />

You can get more instructions from the query description.

<img src="./media/image3.png" style="width:6.5in;height:3.64514in" alt="Graphical user interface, text, application Description automatically generated" />

Similarly, you can edit runoff and landuse

<img src="./media/image4.png" style="width:6.5in;height:2.60833in" alt="Graphical user interface, application Description automatically generated" />

After running the model, you can create a SWMM5 style subcatchments.

1.  Drag the results into GeoPlan

2.  Drag the 400 query into GeoPlan

3.  Review the results, it is the same as the SWMM5 subcatchments report

<img src="./media/image5.png" style="width:6.5in;height:2.65903in" alt="Graphical user interface Description automatically generated" />

# Conclusion

With ICM SQL queries, you can build customize modeling building workflows which can greatly simplify the steps involved setting up SWMM5 hydrology in ICM.
