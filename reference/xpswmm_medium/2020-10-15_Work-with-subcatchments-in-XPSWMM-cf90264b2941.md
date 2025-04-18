# Work with subcatchments in XPSWMM

Source: Innovyze User Portal

---

### Work with subcatchments in XPSWMM

![](images\1_-Tt3RNJRk2aIXghmnlRWPw.png)

Source: [Innovyze User Portal](https://innovyze.force.com/support/s/article/Work-with-subcatchments-in-XPSWMM)

Sample models can be downloaded from [GitHub](https://github.com/mel-meng/xpswmm/tree/master/models/import%20subcatchment).

Subcatchment is a widely used concept for modeling the runoff. Most storm sewer modeling software uses subcatchment to generate runoff from rainfall. However, the way to create and edit subcatchment can be quite different in different software packages.  
   
In most modeling packages, subcatchments are used to generate runoff from rainfall, and the user can enter all the hydrology parameters.  
   
In SWMM5 and InfoWorks ICM, subcatchment has its own layer, it works very similar to nodes and pipes, which can have its own names, attribute tables, and can be accessed directly from the map view by clicking on the subcatchment polygon. There is no limit on how many subcatchments can be connected to a single node.  
   
In InfoWorks ICM, subcatchment is also used for generating dry weather flows from land use information.

Catchment and subcatchment are usually used interchangeably. XPSWMM, however, does use them with slight difference.  
Catchment: The polygon layer or the polygons that can be associated to a node that may represent the model subcatchment. The catchment polygon can be connected to a node in a subcatchment position and then be used to assign area or other hydrologic properties using embedded tools.

Subcatchment: The drainage area and associated data that will convert rainfall to runoff using a routing method such as SWMM non-linear reservoir, SCS etc. A node in XP can have up to 5 subcatchments. The outflow of a subcatchment can be directed to another node or another catchment rendering the 5 subcatchment limit moot.

In summary, in XPSWMM, catchment is a graphical only child layer of the nodes layer and the individual subcatchment data can be directly accessed through the node or by double-clicking on the attached catchment polygon in the map view. In XPSWMM, each node can have up to 5 fixed subcatchments with fixed subcatchment number.  
   
Due to these differences, working with subcatchments can feel different for users who are familiar with SWMM5 or InfoWorks ICM. In this article, we will go over a few best practices when working with subcatchments in XPSWMM.

### Subcatchment Polygons (catchment)

The subcatchment polygon layer is treated as a polygon layer rather than a modeled element layer the same way as node and point. Therefore, when creating subcatchments, it works in similar ways as all the 2D layers. We need to select the catchment layer in the layer tree first, then the polygon tool will be activated.  
   
Also, having a polygon for a subcatchment is optional, the engine doesn’t use any of the information of the subcatchment polygon for its calculation.

### Creating Subcatchment

The XPSWMM user interface is optimized for manually entering subcatchment attributes. For models with a large number of subcatchments to delineate and parameters to populate, a different workflow is needed.  
   
For teams with advanced GIS capabilities, subcatchment attributes are commonly generated using automated GIS tools, and then imported into modeling software.  
   
We’ll review 3 typical subcatchment creation workflows.

* [Manually create subcatchment](https://innovyze.force.com/support/s/article/How-to-manually-create-a-subcatchment-in-xpswmm) for small models
* [Import subcatchment from GIS data](https://innovyze.force.com/support/s/article/How-to-import-subcatchment-from-GIS-in-XPSWMM) for large models
* [Import subcatchment from table](https://innovyze.force.com/support/s/article/Import-subcatchments-from-external-table-in-XPSWMM) will take more time to setup, but if keeping a dynamic link is important this is the right method

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 15, 2020](https://medium.com/p/cf90264b2941).

[Canonical link](https://medium.com/@mel-meng-pe/work-with-subcatchments-in-xpswmm-cf90264b2941)

Exported from [Medium](https://medium.com) on March 18, 2025.