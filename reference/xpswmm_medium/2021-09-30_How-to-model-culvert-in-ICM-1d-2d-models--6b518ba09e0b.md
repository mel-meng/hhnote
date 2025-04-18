# How to model culvert in ICM 1d/2d models?

source: Innovyze Support Portal

---

### How to model culvert in ICM 1d/2d models?

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-model-culvert-in-ICM)

### Introduction

For a more in-depth discussion of culvert design, refer to [FHWA HDS 5](https://mel-meng-pe.medium.com/culvert-design-theory-99965aa4efac). In this article we’ll give recommendations on how to model culvert in a 1d/2d ICM model.  
2D conduits are recommended if stability is a concern. However, with 2D conduits, the inlet control condition cannot be modeled using the FWHA HDS5 method. There are however advantages such as the continuity of mass and momentum. This could be especially important where rapid surface flow is present.

![](images\1_fMxdRNVd74YvkZj8NbQimQ.png)

When modeling a 1d/2d culvert it is very different from a normal 1D pipe configuration; culvert doesn’t have manhole shafts, it opens directly to the channel.

When considering the “ground level” it is very important to match the culvert inlet and outlet levels with the bed of the channel. That is where the linkage is going to be taking place and where the calculation points will be taken from.

### Recommendation

From our limited experiences, 2D conduit usually is more stable and easier to setup. Therefore, if getting very high accuracy at the culvert is not a top priority of the modeling project, this should be a good enough solution.

### 2D conduit

Culvert using 2D conduits: Connect 2D -> 2D conduit -> Connect 2D

![](images\1__CjylRvcD2oi-Sre-5t1uQ.png)

### 1D Culvert

If you need to model the culvert using the FHWA method, things can get tricky because the method is only developed for 1D method. In theory, we should model both the channel and the culvert as 1D system, therefore, we’ll need to model the channels as 1D river, and connect the 1D river to the 2D surface. The system could look like this,  
Inline bank>river reach>inlet>conduit>outlet>outfall 2d  
We might need to add both inlet and outlet if reverse flow is expected. As you can see this approach can be quite tedious, and it is prone to stability issues with the complication of 1d river, and culvert losses. And without calibration data, it can be hard to judge which method is more accurate.  
In practice, you might want to try different variations this setup. For example, you can try this setup without adding the river reaches and the outlet link: Outfall 2D->Culvert Inlet->Break node->Culvert->Outfall 2.

![](images\1__CjylRvcD2oi-Sre-5t1uQ.png)

### 1D-2D link basis

When linking a culvert to 2D using Connect2D or Outfall2D, in most cases we should use the depth basis because ideally a culvert should be flush with the channel bed. Elevation linkage should only be used where the culvert entrance / exit is at a high level above the ground level (i.e. bed level).  
If the entrance to the culvert is below the ground level of the terrain model, then the mesh elements at the entrance will have to be lowered to that level. This can be achieved using a mesh zone or mesh level zone.

![](images\1_z3DFnGYQyVStBbij5U8c_g.png)

When connecting 1D and 2D, it is important to cross reference the 2D element and 1D object inverts make sure the data entered are correctly presenting the flow path.

![](images\1_xF0mXhJRC10pNGWXyznAcQ.png)

### FAQ

### Can I use node types other than Connect 2D for 2D conduit? If so, which type should I use?

When using conduit 2D, you can choose to use types other than connect 2D, but it will turn the node into a manhole and transfer the flow into the 1D engine. This would negate the reason for using the 2d conduit.

### When modeling a 1d culvert, what type of node to choose from? Outfall 2D, manhole, connect 2D which one to choose from?

If you are modeling using a 1D conduit, use outfall 2D to connect the culvert to the 2D. You should not use a manhole type node to connect a culvert to 2D.

### What is the difference between 1d-2d linkage basis elevation vs depth?

Users should really follow the rule that “elevation” applies when the conduit invert is above the element level i.e. the pipe is significantly raised above the bed. Minor differences due to scour can typically be ignored.

### For outfall2D/Connect 2D when using elevation basis, what elevation is used?

ICM will look at the elevation of water in the element and the elevation of water in the conduit to calculate a head difference and flow rate.

### How to model blockage and flap gate for culvert?

Blockages can be modelled by either adding “sediment” to the conduit and adding a “blockage” link to the appropriate location. Note that a blockage link is intended for calibration against recorded data. A flap valve can be modelled to ensure unidirectional flow. However, all of these would currently dictate employing the 1D-2D connection mentioned above.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 30, 2021](https://medium.com/p/6b518ba09e0b).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-model-culvert-in-icm-1d-2d-models-6b518ba09e0b)

Exported from [Medium](https://medium.com) on March 18, 2025.