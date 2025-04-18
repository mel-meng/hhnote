# Example: How does XPSWMM Model Bridge Openings

Source: Innovyze Support Portal

---

### Example: How does XPSWMM Model Bridge Openings

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Model-bridge-opening-in-XPSWMM-Example)

You can download the model from [GitHub](https://github.com/mel-meng/xpswmm/tree/master/models/bridge_opening).

### Model Setup

XPSWMM models a bridge by converting the opening as closed conduit(s). In this example, we will model a river stretch with a bridge. In this special case, the bridge is above the flow, and shouldn’t impact the flow.

We modeled this situation in 3 scenarios,

1. Top: modeling the bridge as the channel
2. Middle: model the bridge as the channel cross section trimmed to only the opening
3. Bottom: model the bridge with trimmed opening cross section

![](images\1_BFT_vQv7QE5GvFJI-4Q_QQ.png)

### Model setup

* Each scenario has 3 link flowing from the left to the right
* The upstream node has a hydrograph of ramping form 0 to 250 cfs
* The downstream node is a free outfall
* The 3 links are all natural shaped channels with the same cross section

![](images\1_lHyxEbP7wwAwL_VnuZqUEA.png)

The only difference are,

* Top scenario, the middle link uses the full cross section
* Middle scenario, the channel uses a trimmed cross section with everything else the same

![](images\1_IJILC1gqxlMGR_VZShUtOQ.png)

* The bottom scenario, the middle link is modeled as a closed conduit using the table generated for the bridge

![](images\1_vNIkk8ySBCI853KvdF3rmQ.png)

### Results

The max. stage of the upstream node of the bridge in the 3 scenarios are almost the same.

![](images\1_RcTY9RU-KEJp5yr5ZZSi2A.png)

### Analysis

Let’s review the 1D log to understand what is happening.

XPSWMM models bridge openings as closed conduit. And internally closed conduit and natural channel are modeled the same, both are relying on conveyance curves calculated from its geometry to route the flow through them.

To show the conveyance curve for channels, check “Echo Natural Section Data”.

![](images\1_EAEY2uVuHE2BUIWtJ4xPEA.png)

We can then exam the conveyance curve for Bridge trimmed and as channel, a sample is shown below.

![](images\1_u1lm4w7TQSIxMd2lAzl2CQ.png)

For the bridge, its opening is converted into a closed conduit, and its conveyance curve is also reported in 1D log.

![](images\1_gDK8BhZRCv4T5MERWDtKnQ.png)

Based on the information above, the conveyance for the closed conduit can be calculated as C = 1/n\*area\*R^(2/3) using manning’s equation. The data in the 1D log is compiled and compared,

For the simulated depth range less than 3 ft, they are the same, therefore giving similar results.

![](images\1_TLkDB6UOJ7R1kGUG6oowIA.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 8, 2020](https://medium.com/p/d095334b551c).

[Canonical link](https://medium.com/@mel-meng-pe/example-how-does-xpswmm-model-bridge-openings-d095334b551c)

Exported from [Medium](https://medium.com) on March 18, 2025.