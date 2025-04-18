# Importing river models from HECRAS to XPSWMM

source: Innovyze Support Portal

---

### Importing river models from HECRAS to XPSWMM

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Importing-river-models-from-HECRAS-to-XPSWMM)

Bridges in XPSWMM are usually imported from HECRAS.  
   
According to the HECRAS reference manual, bridges are modeled as 4 cross sections and the bridge structure as shown in Fig 5–1 and Fig 5–2. For more details refer to the manual.

![](images\1_EWBwpc6j73sbbNHO5ybTKg.png)![](images\1_tR7WiphclcTnPWI5G_sJog.png)

When XPSWMM imports a HECRAS model, it will import all the cross sections, and for the bridge, additional information need to be populated due to the difference between how XPSWMM represent bridges.

### Difference between XPSWMM/HECRAS

### HECRAS Reach

HECRAS represents a river reach as a cross section with lengths for the center channel, left and right overbanks. The cross section represents the actual shape and invert on the upstream end, the slope of the reach is determined by connecting the invert of the two upstream/downstream reach cross sections.  
   
XPSWMM represents a river reach as two nodes and a link, the cross section only represents the shape of the link, the inverts of the upstream and downstream of the link need to be entered as the inverts for the reach link, and the nodes of the reach should match the cross section invert and top.  
   
As a result, ineffective areas and blockage cannot be defined directly in XPSWMM, because they are not part of the channel shape definition.

* Blockage needs to be built into the shape directly in XPSWMM
* Ineffective area needs to be handled carefully, if it is not contributing to the conveyance, it should be modeled as a storage or 2D surface. If it is within the conveyance, a very high manning’s n can be used for the ineffective area.

When it comes to bridge, XPSWMM represent a bridge as,

* Closed conduits for openings (3 piers will result in 4 openings)
* Weir for flow over the top of the bridge
* Standard shape pipes for culverts

![](images\1_oeL0jcCCryMK8zvneyiSJQ.png)

HECRAS provides more parameters to define a bridge on both the upstream and downstream sides of the bridge.

* The deck have two profiles
* The pier is defined on both sides

### Cleaning Imported HECRAS Model

Since the most common type of HECRAS model is steady state model, in most cases they need to be cleaned up before running in XPSWMM, which is unsteady state.  
   
For steady state HECRAS model, the whole flood plain is modeled using cross section, which extends to areas where ponding will happen. When converting to unsteady state models, ponding areas that doesn’t contribute to the conveyance should be removed from the model, and modeled as 1D storage or 2D surface.  
   
Therefore, the first step should be overlaying the HECRAS bank lines and the water surface extent showing the main channel, and then trim the cross section to keep only the main channel.

![](images\1_WOViJyQx37aM8nglupOfqw.png)

This step is especially important for 1D/2D models, the interface line between the river and the 2D surface should match the boundary of the cross section in XPSWMM.

### Review XPSWMM River Models

XPSMM 1D log has detailed information for river links and bridge links.

### Bridge

Bridge openings are shown in Table E1

![](images\1_pbcQTth3y77bCChWcy2S5A.png)

The inverts for closed conduits can be found in Table E4

![](images\1_pHU0hVK8hApYhCUPapnCoQ.png)

And the conveyance curve for the closed conduit is also reported.

![](images\1_FgljA-1G2aUmi4gR-DIoag.png)

### River Reach

Detailed river reach cross section and conveyance curve can also be reported  
To show the conveyance curve for channels, check “Echo Natural Section Data”.

![](images\1_6F0LCcWSE6H7OpzFOCuVWQ.png)![](images\1_ZvlV16n-QCTdcdUT2ips3A.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 9, 2020](https://medium.com/p/595b3ade1323).

[Canonical link](https://medium.com/@mel-meng-pe/importing-river-models-from-hecras-to-xpswmm-595b3ade1323)

Exported from [Medium](https://medium.com) on March 18, 2025.