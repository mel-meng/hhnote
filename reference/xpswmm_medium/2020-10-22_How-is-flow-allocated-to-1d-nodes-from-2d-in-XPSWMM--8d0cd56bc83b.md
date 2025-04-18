# How is flow allocated to 1d nodes from 2d in XPSWMM?

There are quite a few major assumptions are made to link 1D/2D models. In this article we will setup a very simple model to get better…

---

### How is flow allocated to 1d nodes from 2d in XPSWMM?

![](images\1_GbzoCc9j_zxKls5rQTPrjg.png)

There are quite a few major assumptions are made to link 1D/2D models. In this article we will setup a very simple model to get better feel how it works. You can find the models on [github](https://github.com/mel-meng/xpswmm/tree/master/models/1d2d_interface).

As shown in the figure above, we have a surface that has a ridge at the middle of 12ft high, then it slopes down north and south to 10ft. In the middle of this surface, we have added a fairly flat channel that runs from south to north with inverts from 8.1ft to 8ft.

With a typical setup of interface lines, inactive areas and connection lines, the channel is linked to the 2D surface. Refer to the “Link 1D and 2D Models” section below for more information about how it works.

What we would like to focus on in this article, is after the flow is calculated at each cell along the interface line, how does the 2D engine pass it back to the 1D nodes?

As explained below, the engine simply divides the interface line between the two nodes in half, and total flow from each half goes to its node.

To test this, we set up our model accordingly,

* we load water to the channel at two locations
* To force the flow into the channel, we build two dams by adding break lines (green lines)

### Test 1 — load on the downstream end

Load water only to the downstream end. As expected,

* Table E19 shows flow into the d/s node
* the profile shows negative flows into the system from the downstream end

![](images\1_MdFVFTctQUPIjOF1N7bVNA.png)![](images\1_M43imNa4JLngRVdKJOZPaQ.png)

### Test 2

From the the upstream end.

![](images\1_IoaqVUtWP9H8k2NX8jjTdw.png)

As expected,

* In table E19, there is only flow into u/s node from the 2D layer.
* And this time we have positive flows from the upstream end

![](images\1__MkzPF57xYFq9t0GDcUmdA.png)![](images\1_uaahI9069sEUdwTiKWyAqw.png)

### Conclusion

Without getting into the source code (if we have access) or taking an experts’ words for it. We confirmed how flows from 2D are loaded into 1D nodes with two simple models. Due to the limitation of 1D model, flow can only be loaded at the upstream/downstream nodes, therefore, the 2D engine routes the flow along the interface lines to the 1D nodes by dividing the interface line in half. For all the flow exchanges happening on the upstream end, the 2D engine loads all the flow at the upstream node. For all the flow exchange happening on the downstream end, the 2D engine loads all the flow to the downstream node.

### Link 1D and 2D Models

As shown in the figure below (from Tuflow manual), there are a few ways flow can be exchanged between a river and the surface around it. The 2d engine compares the water level in the 1D channel with the water level in the left and right banks, and then calculates the flow exchange at each cell.

![](images\0_LPFNVMrrbw1WnBR-.png)

The calculation for the flow to go through the banks is achieved using the interface lines. As shown in the figure below (from TuFlow), for a river reach, we create two interface lines for each bank (blue, HX type, head boundary), and then we connect the nodes to the interface line (green, CN type). By connecting the nodes to the interface bank lines, the 2D engine can interpolate the water depth inside the river by interpolating between the two nodes, then the engine compares the depth of the 1D river with the 2D cells along the interface line to calculate the flow exchange between them. Then the engine will divide the interface line in half, and load all the flows (in or out of 1D) on the upstream end to the upstream node, and the other half to the downstream node.

![](images\0_6hnKMuIErL7dXn_8.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 22, 2020](https://medium.com/p/8d0cd56bc83b).

[Canonical link](https://medium.com/@mel-meng-pe/how-is-flow-allocated-to-1d-nodes-from-2d-in-xpswmm-8d0cd56bc83b)

Exported from [Medium](https://medium.com) on March 18, 2025.