# Building a collection system network: step 1 connecting the dots

Connecting the dots is a simple but tedious step. It starts with an understanding of modeling objects, SWMM based models and ICM have very…

---

### Building a collection system network: step 1 connecting the dots

This is the second one of this [series](https://medium.com/@mel.meng.pe/building-a-collection-system-network-the-theory-f9422cb61ed5).

Connecting the dots is a simple but tedious step. It starts with an understanding of modeling objects, SWMM based models and ICM have very similar network objects.

* Gravity pipes and manholes are just node and links.
* Pump stations are more complicated, the wet well is modeled as a node, and the pumps are modeled as links. So a pump station looks like: ->wet well node->pump link->force main inlet node->force main->
* Storage facilities are usually simplified as storage node and overflow structures as orifice and weir, which are modeled as links

I generally import gravity pipes and manholes from the GIS, and manually build pump stations and force mains in the model.

Building a rough model that I can run early in the process is a strategy I often use. Getting all the data reviewed and cleaned so that the model can run usually will take a very long time. If I wait until everything is ready, it might be too late for me to ask for additional data. By building a rough model at the very beginning can help me identify major issues much earlier in the process. The idea is simply to build enough of a model so that I can hit the run button and see results and being able to tell if something is seriously wrong.

Here is my progression of the model built,

* Find the outlet and trace upstream for the trunk lines
* Group the branches into a few groups, so that I can review each group within a day
* First build a model with only trunk lines and make sure it runs.
* After that adding one area a time and make sure everything runs after adding the area.

It is easier said than done, let’s get started. I am going to use InfoSewer to build the network, it really doesn’t matter what modeling package you are using, most of the tools I use are commonly available in these packages.

### Review data in GIS

Before getting everything into the model, need to review the data in GIS.

As shown below, after loading the manhole and pipe layers, we need to remove the parts that are not within the model and adding an outlet.

![](images\1_108bi7kMHX2hGfTewq7T0Q.png)

Next we need to review the flow directions.

![](images\1_OO5PbuQyo3Izq8yFVvg16A.png)

It can be a big pain to fix randomly digitized pipes, some software packages have tools fixing these, and you should take advantage of that. One thing to keep in mind is that, no matter what tools we might have, this can be a tedious process. Just need to be patient.

I don’t have to get all the directions fixed in GIS, modeling software has better tracking and flow direction fixing tools than ArcMap, so I usually fix such errors in the model.

### Assign Unique IDs

I don’t remember ever received a GIS datasets from a client without duplicated IDs in it. So I always check it.

Another tip, if you can afford to use text as IDs, don’t use numbers. It is so frustrating when Excel turns all my IDs to floating numbers. An easy way to build ID is to prefix the OBJECTID in ArcMap, it is always unique.

![](images\1_lSrqLS8HNvLH5Navn8_o0A.png)

If there is a need to exchange data from updated data source in the future, I’ll also keep the IDs from my client in another column and import it into the model.

### Prepare attributes to be imported

For manholes, the following are needed,

* Rim elevation
* Invert elevation

For gravity pipes, the following are needed,

* Diameter: make sure use the model units, in vs ft
* Upstream invert
* Downstream invert
* Manning’s n

I prefer to get the from/to node directly from the geometry of the network so we don’t need to worry about adding these in the GIS.

### Getting the GIS into the Model

In InfoSewer and InfoSWMM, we use GIS gateways, and in ICM we use Open Data Import Center.

![](images\1_6APWkbkFdAo4uSr1_9PReQ.png)

### Connectivity Review

I need to first populate the from/to node for pipes before I can trace the network.

![](images\1_j9p98KFsAw_iDzam2oSteg.png)

If you have great GIS data, using a very small number. Otherwise, you might want to use 1ft maybe even 5ft as search distance.

![](images\1_LCAt48LcWPib0meigq5VnA.png)

I also need to turn on the flow arrow so that I can check the flow direction visually.

![](images\1_KNZObACsmfRGBO4N_PZ9Ig.png)

Let’s find the outlet using the trace tool.

![](images\1_JF0rOIoxKQaO-NuWhsyMHA.png)

Great, it looks like there is only one outlet.

![](images\1_SXaBaJJ2u116ZMi6pX-xSg.png)

Next, we need to find all the upstream pipes and nodes that drain to the outlet.

![](images\1_6WZzD2YgdCF8sg9D9CCm7A.png)

And we found a few objects not connected correctly. I turned on the manhole ID label to make it easier to describe the areas. As shown below, the direction of the pipes were wrong between MH 93–94–96–28. And if you prefer a GIS centric workflow, you can go back to GIS flip these pipes and then update the geometry using GIS gateways. I’ll just fix them in the model.

![](images\1_jhUdb9urxY6acwah6SFsCg.png)

Now let’s make sure all the pipes and nodes are draining to the outlet.

1. Clear the domain
2. Track upstream of the outlet
3. Inverse the selection

![](images\1_kNOrDt9WVfJQ0z9vpmjg_w.png)

Nothing is selected, so I know all the pipes are connected.

In the next post, I’ll establish the vertical profile. You can find other articles in this series below,

1. [Connecting the dots](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-1-connecting-the-dots-fa3b33b1bba8)
2. [Establishing the vertical profile](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-2-establishing-the-vertical-profile-4d3228004776)
3. Special structures such as pumps, etc
4. Interactively building a network

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 15, 2020](https://medium.com/p/fa3b33b1bba8).

[Canonical link](https://medium.com/@mel-meng-pe/building-a-collection-system-network-step-1-connecting-the-dots-fa3b33b1bba8)

Exported from [Medium](https://medium.com) on March 18, 2025.