# Building a collection system network: step 4 Interactively Building a Model

This is the fourth one in the series.

---

### Building a collection system network: step 4 Interactively Building a Model

This is the fourth one in the [series](https://medium.com/@mel.meng.pe/building-a-collection-system-network-the-theory-f9422cb61ed5).

When building large models, the best advice I have is divide and conquer. With thousands of pipes in a network, it probably will take days to get all the errors fixed before the model will run. So a systematic approach is needed to divide the network into smaller sub models and get one sub model to run at a time. This approach helps me to catch data gaps much earlier on, so that I don’t turn them into a bigger problem by realizing the issues much later and running out of time getting the data.

I usually divide the model into the following sub models,

* Start with the gravity part of the model, if I have major pump stations, I’ll stop at the pump station and treat the areas upstream and downstream of the pump station as two sub areas
* Then I’ll identify the trunk lines of each sub areas, and build a trunk model by adding loadings at the upstream end of the system and run the steady state model. It usually will ask me to fix a few errors before it will run, and that’s how I fix the data errors. Once it runs, I will check the results to make sure the results make sense.
* Then I’ll add branches to the trunk line, using the same steps, adding a loading at the upstream of the branch to get the steady state model to run and make sure everything make sense.
* Once I have all the branches added and the model runs, I can move to the next step, adding special structures

For users who are not familiar with InfoSewer or InfoSWMM, the “facility” tool is used to sub divide a model. With the “facility” tool, I can enable and disable model objects so that I can run the model for only part of the network. If you are using other modeling packages, you can create sub models by copy and paste part of the model as a new network. As long as you can run a model of only part of the network, you can use this method.

Before I sub divide the model, let’s populate missing default values. To know what is missing, just run the model and see the error message.

As shown below, I need to populate the 4ft default manhole diameter.

![](images\1_EY8fnBsgat_yAtgQ-mU5HQ.png)![](images\1_oxoD6SiFyLKB-k4XTiKR6Q.png)

I run the model again, and this time it asks me to fix the manning’s n values.

![](images\1_OHkA-jHwOkbz30M-ov0IHQ.png)![](images\1_W8fjVYiHJ8ldWwNN0zv8gw.png)

Then it complains a default pattern.

![](images\1_x4jg6ker4Zay6U2mCnYoLw.png)

For a steady state run, I added a constant pattern of 24 ones for diurnal pattern.

![](images\1_RU-wZCyyXF31G3SDx9hOag.png)

Then I got other errors that are more specific to a single object, and that’s where I know I should start to divide my network.

### Trunk Line

To find the trunk line, I used the tracking network downstream tool and then use the facility tool to enable the trunk line.

![](images\1_ITZLX9DZ2oyp6eHGOpSyUg.png)![](images\1_PYlJv5v6gtyX1_QVj192dw.png)

Save the trunk line as a selection set.

![](images\1_o8tb1SgjyY6eehrZfe4aug.png)

Disable all objects in the model.

![](images\1_XgGdw0kZtyfOALx-pmWWTQ.png)

Enable the trunk line,

![](images\1_aI0KGqqfuXihLz76ZNJLTw.png)

Load the flow at the upstream node. The absolute value is not important, the idea is that we can see the flow routed downstream. It should be something like 0.5, or 0.1. Numbers you can remember and as they are routed downstream you can easily verify if the total flow is correct.

![](images\1_Xi-8DUpg--sf8ONhuOp5tQ.png)

You can check the profile and the results in the pipe to make sure the flows are routed correctly.

![](images\1_JrAdKxpCG0WsR5zyjT6fQw.png)

Next, I am going to add a tricky area. Since it is a loop, there must be a node with split flows on both directions. Let’s turn on flow direction.

![](images\1_WA1854rnO37VxQpOnjyoog.png)

Once we enabled this area, we can see the flow split below. Let’s load 0.4 cfs at MH166 and see what happens.

![](images\1_Ja4acsK49sDYwHzfvcBiiw.png)

Let’s run the model and display flows on the pipe,

![](images\1_C3QBo1GlUf7IAT2X99jYJg.png)

Since we are using the automatic allocation for both downstream pipes, InfoSewer decides how to split the flow based on the inverts.

![](images\1_04KjSNgrgF_rbxgVQx7bbg.png)![](images\1_aSGlnZ80AInNgmAAHJL-_A.png)

Personally, I don’t like flow splits because they tend to make things more complicated, and usually they are the sources of stability issues and data entry errors. If I can afford it, I usually will verify the flow splits with record plans and other sources. In this case, since the tributary area of the upstream area is so small, I am OK with using the automatic split. If it is on a trunk line, I might run some tests to decide what is the best flow split settings.

And that is the case for the next area,

![](images\1_wB8rEzaZf9qxd8PK6fMLxQ.png)

In this case, the flow split happens on the trunk line. Recall we estimated the inverts based on pipe slopes from the outlet. So without checking the record drawings, I would not say this flow split is a reasonable estimate. So my action item for this split is to request record plans or field verification.

![](images\1_Rk6JPbNsWPylM_L_jvjMJA.png)

I hope you got the idea on how to interactively build a model. Through my own experiences, small batches actually is more efficient than large batches. When I start building smaller areas at the beginning of the project, I quickly learn most of the places things can go wrong, and then I start to address them very earlier instead of in the last minute. As shown in this example, I quickly realized that I need to survey the flow splits along the trunk lines in the 2nd area I worked on. If I tried to run the model with everything in it, I might spend another week just to get the model running, and then as I started to review the results which might take another few weeks, by that point I might realize that I need to verify this flow split, and it might be too late for me to get the results in time.

In the next post, I’ll setup special structures. You can find other articles in this series below,

1. [Connecting the dots](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-1-connecting-the-dots-fa3b33b1bba8)
2. [Establishing the vertical profile](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-2-establishing-the-vertical-profile-4d3228004776)
3. Special structures such as pumps, etc
4. Interactively building a network

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 20, 2020](https://medium.com/p/9e39f41de27d).

[Canonical link](https://medium.com/@mel-meng-pe/building-a-collection-system-network-step-4-interactively-building-a-model-9e39f41de27d)

Exported from [Medium](https://medium.com) on March 18, 2025.