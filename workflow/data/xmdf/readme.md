---
title: Work with XPSWMM 2D Results (xmdf) in QGIS
---

# Introduction

[QGIS](https://docs.qgis.org/3.28/en/docs/user_manual/working_with_mesh/mesh_properties.html) offers native support for XPSWMM 2D results files, allowing you to access simulation results in their raw format without the need for conversions. This capability provides several benefits, including:

- The ability to use advanced visualization styles and animations for mesh in QGIS.

- An expanded range of options for converting results to other GIS formats.

<img src="./media/image1.png" style="width:4.24362in;height:2.61036in" alt="A blue stream with many small black dots Description automatically generated with medium confidence" />

In this article, you will learn,

- Load XPSWMM 2D results into QGIS

- Rendering maximum values in the map

- Play animation of the simulation

- Export the results to raster format

- Export the results to vector format

# Load XPSWMM 2D results into QGIS

XPSWMM saves the 2d results in two files,

- \*. [2dm](https://www.xmswiki.com/wiki/SMS:2D_Mesh_Files_*.2dm): saves the mesh, and the terrain data

- \*.[xmdf](https://en.wikipedia.org/wiki/XMDF): saves the time series

To load the results into QGIS,

1.  Load the \*.2dm file into QGIS. Drag the file into QGIS.

<img src="./media/image2.png" style="width:4.57512in;height:2.54809in" alt="A screenshot of a computer Description automatically generated" />

2.  Load the \*.xmdf into the \*.2dm mesh

<img src="./media/image3.png" style="width:4.84016in;height:3.23711in" alt="A screenshot of a computer Description automatically generated" />

# Rendering maximum values in the map

## Max. Depth

1.  Select max. depth as the value to show

<img src="./media/image4.png" style="width:4.28085in;height:2.45783in" alt="A screenshot of a computer Description automatically generated" />

2.  Select the color ramp and make it transparent

<img src="./media/image5.png" style="width:5.48777in;height:2.93385in" alt="A screenshot of a computer Description automatically generated" />

<img src="./media/image6.png" style="width:4.65458in;height:4.02701in" alt="A screenshot of a computer Description automatically generated" />

# Play animation of the simulation

1.  Set depth as the contours (fill), and velocity as the vector

<img src="./media/image7.png" style="width:6.5in;height:2.57361in" alt="A screenshot of a computer Description automatically generated" />

2.  Set the depth style

<img src="./media/image8.png" style="width:5.11901in;height:2.33145in" alt="A screenshot of a computer Description automatically generated" />

3.  Set the velocity style

<img src="./media/image9.png" style="width:6.5in;height:2.80139in" alt="A screenshot of a computer Description automatically generated" />

4.  Turn on the time control

<img src="./media/image10.png" style="width:3.26128in;height:5.52789in" alt="A screenshot of a computer Description automatically generated" />

5.  Play the animation

<img src="./media/image11.png" style="width:6.5in;height:4.61042in" alt="A screenshot of a computer Description automatically generated" />

6.  You can explore more vector styles

<img src="./media/image12.png" style="width:4.76883in;height:3.53994in" alt="A collage of images of a person&#39;s body Description automatically generated" />

# Export the results to raster format

1.  Turn on the processing toolbox

<img src="./media/image13.png" style="width:3.11396in;height:4.95177in" alt="A screenshot of a computer Description automatically generated" />

2.  Locate the Mesh tools

<img src="./media/image14.png" style="width:2.72883in;height:1.94767in" alt="A screenshot of a computer Description automatically generated" />

## Export max. water depth as raster

1.  Open “Rasterize mesh dataset”

2.  Set up the parameters for the tool

<img src="./media/image15.png" style="width:5.07549in;height:3.45198in" alt="A screenshot of a computer Description automatically generated" />

<img src="./media/image16.png" style="width:2.83427in;height:3.80703in" alt="A black and white image of a shoe Description automatically generated" />

## Export max. water contour lines

1.  Open the “Export contours” tool

2.  Set up the parameters

<img src="./media/image17.png" style="width:6.5in;height:4.64028in" alt="A screenshot of a computer Description automatically generated" />

3.  Turn on the contour line layer

<img src="./media/image18.png" style="width:4.95086in;height:3.56494in" alt="A screenshot of a computer screen Description automatically generated" />

# Export the results to vector format

1.  Open the “Export mesh vertices” tool

2.  Setup the parameters

<img src="./media/image19.png" style="width:4.48145in;height:3.6091in" alt="A screenshot of a computer Description automatically generated" />

<img src="./media/image20.png" style="width:4.2053in;height:3.47701in" alt="A screenshot of a computer Description automatically generated" />

# Conclusion

In conclusion, working with XPSWMM 2D results in QGIS provides benefits such as advanced visualization styles, animation capabilities, and options for converting results to other GIS formats. By following the steps outlined in this article, you can easily load XPSWMM 2D results into QGIS, render maximum values on the map, play animations of the simulation, and export the results to raster or vector formats. This integration enhances the analysis and visualization capabilities for water management and flood modeling projects.
