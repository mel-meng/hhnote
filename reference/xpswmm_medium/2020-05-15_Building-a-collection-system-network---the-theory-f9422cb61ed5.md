# Building a collection system network: the theory

Earlier in my career I spent a lot of time building models in GIS, and I enjoyed doing that. However, in the past two decades, with…

---

### Building a collection system network: the theory

![](images\1_x7I947YhQCeojuSOE8xcaQ.png)

Earlier in my career I spent a lot of time building models in GIS, and I enjoyed doing that. However, in the past two decades, with continued investments in digital infrastructure data, building models felt like a lost art nowadays. Very few young modelers started their career building models by connecting the dots now.

For nostalgia’s sake, I am going to post a few articles explaining the fun and pain of building a network. I do believe understanding how to build a network and fix the connectivity issues can be a great introduction to graph theories, the math branch that inspired algorithms such as Google search. As AI and big data bring new opportunities solving challenging water problems, a perspective rooted from the GIS network theories should not be ignored.

When building a collection system network, I go through the following steps. You can click on the link to see an example of each step.

1. [Connecting the dots](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-1-connecting-the-dots-fa3b33b1bba8)
2. [Establishing the vertical profile](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-2-establishing-the-vertical-profile-4d3228004776)
3. Special structures such as pumps, etc
4. Interactively building a network

Connecting the dots is pretty easy, just connect manholes using pipes. And that is the basic structure of a graph or network. From this very simple structure we can build very complex systems and that’s what makes network so fascinating.

To appreciate the beautify of networks, I would like to talk about modeling first to explain the not so obvious relationship between modeling and networks. My favorite type of modeling is steady state modeling, I think it has been largely undervalued in the modeling process. Steady state models can be built using manning’s equation and a spreadsheet, virtually anyone with basic math can build it. And it is a powerful mental tool when working with complex systems.

When working with complex system, the hydraulics are so complicated, it felt like a big mess if you look at the modeling results. So what worked for me in the past is that I typically assume I am running a steady state model with constant peak flows through the system, and with that mental model I can intuitively get some ideas how the system should behave, from there I can start to form a more accurate understanding how the system work.

So in other words, I can do steady state routing inside my head fairly easily without the need of running a model. Kind of like how we can do simple math without effort, we just know the answer.

To be able to mentally route steady state flow will take some effort, but not too much. It is the same skill how we how we read a map for directions.

To route the flow, we need to know the source of the flows and the outlet of the flows. And then we simply route the flow from the source to the outlet. In most cases, it is fairly easy just to pass all the flow to the downstream pipe. But for a few situations, we’ll need some rules to decide,

* A flow split. When manhole A has two downstream pipes to manhole B and manhole C. We need a rule to divide the flow so some goes to B: A->B, and some goes to C: B->C. And manning’s equation doesn’t tell me how to calculate that. Here are a few that come to my mind, a 50/50 split if I know nothing about the configuration; or if it is a overflow structure, I’ll assume no overflows during normal condition, and a cut off flow rate during wet weather condition.
* A loop: For gravity sewers, this will never happen. So usually it is a data error. A loop will get us into an endless loop for our simple routing procedures, so it needs to be fixed if we need to do a steady state routing.

Some people might say that with dynamic wave equations, routing procedures like this is no longer needed, so knowing where splits and loops are is not very important. I would argue the modeler should always pay attention to flow splits and loops in a system, because these are hot spots for troubles,

* More likely to have wrong data of the structure configuration
* More likely to cause numerical stability issues
* More likely to have big impact on proposed improvements

So that’s the theory. When we are building the network, think like you are routing steady state flow in the system, pay attention to flow splits and loops that can get your routing stuck. In the next post, I’ll list the steps I usually use to get a network built and cleaned.

In the next post, I’ll import GIS into the model and connect the dots. You can find other articles in this series below,

1. [Connecting the dots](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-1-connecting-the-dots-fa3b33b1bba8)
2. [Establishing the vertical profile](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-2-establishing-the-vertical-profile-4d3228004776)
3. Special structures such as pumps, etc
4. Interactively building a network

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 15, 2020](https://medium.com/p/f9422cb61ed5).

[Canonical link](https://medium.com/@mel-meng-pe/building-a-collection-system-network-the-theory-f9422cb61ed5)

Exported from [Medium](https://medium.com) on March 18, 2025.