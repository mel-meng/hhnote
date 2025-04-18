# PySWMM : Interview with Bryant McDonnell (2 of 3)

This is part 2 of the 3 parts interview with the creator of PySWMM

---

### PySWMM : Interview with Bryant McDonnell (2 of 3)

![](images\1__k2hjOWviqs5dIOn35w0Xw.png)

This is part 2 of the 3 parts interview with the creator of PySWMM

[Part 1: The conception of PySWMM](https://medium.com/p/e9be5cf0a62f)

[Part 2: The Evolution of PySWMM](https://medium.com/p/f5243a59de9b)

[Part 3: Advice and future of PySWMM](https://medium.com/p/4ec86cd5c2ef)

**Mel: What do you think needs to happen to make this open source project a long-term success?**

**Bryant**: Building a community is incredibly challenging to do, and I would argue that it has been the hardest part of this project. Things that really helped are good documentation and testing. Everything is documented, and unit tested. We don’t accept code that is not tested and documented. Those are foundational pieces. Passing on leadership responsibilities is also important for the long-term success of the project. At the beginning, I was doing everything. Now as we have new contributors, it becomes easier. Say if it is LID stuff, I know who to send that to.

At Xylem, our vision is that that models should be democratized. (Democratizing the model means that the model is not confined as a tool for planning but is available to all utility stakeholders. In a democratized model, field staff, operators, and engineers utilize and continuously build the model. To enable this vision, we need a modern approach to developing SWMM and EPANET.) The idea behind PySWMM is that individuals, groups, and communities can share proposals and, based on demand, features can be contributed in. This approach works really well when there is a core team of maintainers to help the community strategize in a thoughtful way the features that are “best.”) So, by getting a bigger community involved and having thoughtful leaders, we can all keep pointing to the same direction.

**Mel: What are the common challenges PySWMM solves?**

**Bryant**: PySWMM solves many things. Some of the bigger things are around workflow. You can automate a process, the general functionalities are connecting, manipulating and interacting with the model. (a few examples).

· At the basic level, open the model, then run it, and you can stream the results out of the model, showing say a hydraulic grade line.

· There are a lot of people doing work with LIDs these days. So, there is a pretty substantial programming interface for LID.

· There are people doing surface water quality modeling.

· Developing tools for automated interaction with the model such as automated calibration and real time control design.

There are a lot of things people are doing with PySWMM.

**Mel: how many people are working on this project?**

Bryant: Both the SWMM and PySWMM have an up to date author list. Many of my colleagues at Xylem are active contributors for which I am very thankful. Many the contributors also come from different universities and different research organizations. We have 4 or 5 consistent maintainers; maintainers are responsible for their sectors of code. I encourage everyone to become a contributor!

**Mel**: This is great. I can see there is a disconnect between the academic side and the engineering side. When I talked to people from the academic side about my problems, they usually will say it is already a solved problem, and it is up to the engineers to figure out how to perfect it. This project is a bridge that helps connect the academic side and the engineering side. The research on the more exciting things can be made accessible to the engineering side more quickly.

**Bryant**: This is interesting. Someone would start using PySWMM for their PhD, and after they are hired, and they will continue (contributing to PySWMM). It is taking their graduate research and R&D and opening it up directly to helping our clients meeting their needs.

**Mel: Could you please talk more about the current scope of PySWMM?**

**Bryant**: The current scope of this project is building out the APIs (Application Programming Interface). APIs are added to SWMM by the open source community (<https://github.com/OpenWaterAnalytics>

). It started with 7 entry points, it was mainly open, start, step, close and report a model. Roughly 30 to 40 entry points have been added to SWMM. PySWMM wrapped all these APIs. It has two steps, first exposing the APIs in the SWMM C source code, then abstract the APIs in Python. For example, you have a node in the model. With PySWMM you can access the node as an object and using the property “getter” to access the invert value. We want to make it to feel like a normal Python package.

Every time we expose a new API it unlocks more opportunities. We have the ability to stream the results out of a running simulation and have the ability to change settings and inject flows all through Python. With the ability to change input parameters during the simulation, you don’t have to have an input file processor because we can leverage the SWMM data model during the simulation.

**Mel: What kind of features are you working on now?**

**Bryant**: There is a very big feature request list. Near term plans are making some fundamental updates to SWMM, re-entrance and thread safety are really big.

**Mel: that is interesting. So, it sounds like most of the people working on the project are more on the civil side than on the computer side?**

**Bryant**: If you look at the earlier code of PySWMM. You can definitely see it was a civil engineer who didn’t know Python approaching this problem. So, we had a developer come one board who worked with Anaconda and put us on a really good direction. All of a sudden, we had automatic documentation, continuous integration and lots of great workflows guidelines. PySWMM is being built and tested on Mac, Linux and Windows, 32 and 64-bit. So, it has been a process.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 5, 2020](https://medium.com/p/f5243a59de9b).

[Canonical link](https://medium.com/@mel-meng-pe/pyswmm-interview-with-bryant-mcdonnell-2-of-3-f5243a59de9b)

Exported from [Medium](https://medium.com) on March 18, 2025.