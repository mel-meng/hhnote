# An Introduction to Drainage Design for Everyone

Mel: I just realized that we worked together in two different firms for almost 10 years. I think all the storm water projects I worked were…

---

### An Introduction to Drainage Design for Everyone

Mel: I just realized that we worked together in two different firms for almost 10 years. I think all the storm water projects I worked were your projects, you are truly my mentor on storm water. Could you please tell us a little bit about yourself?

Lee: TODO

Mel: At Innovyze, I help our customers become modeling experts. The modeling part of drainage design usually is just one of the many steps of a big project, so a good understanding of why do we need to do drainage design, and how drainage design fits into the general engineering process is very important for modelers and people who need to make decisions using the modeling results. And that’s what I would like to get out of today’s interview.

Lee: That sounds great. Let’s get started.

Mel: **Storm water design is everywhere, could you please share with us how you design storm water?**

Lee: It is pretty much in every project we do. For most projects, storm water is not the main focus, it is just part of the design. It is not too different from building code requirements, there is an electrical portion, an HAVC portion. And storm water is just one of the permits to apply. For example, for one of my projects we have a 50ft diameter shaft, instead of putting a slab, we buried it under grade with grass on top to comply with the storm water rules.

Mel: That is interesting. **So who set all these storm water rules?**

Lee: My career started in the late 90s, and that’s how far I can go back. At that time, there was very few federal regulations. All we had was phase I NPDES, that was mainly erosion sediment control for large construction sites. For most municipalities, they have mostly flood control type of ordinances. And from my experiences, most of the country was like that. In the early 2000s when phase II NPDES kicked in, and came in with construction permits. that’s the first time we started to see federal requirements for water quantity and quality controls in a post construction setting. Each state was required to adopt their own rules at least as strict as the federal rules. Most states have their own rules very close to the federal requirements, with a few states went above and beyond, like Michigan, California. That led to a lot of the communities looking at their regulations. For example , Columbus had its storm water manual updated in 2006, almost 30 years after the previous version. And that is the evolution of the regulations.

Mel: **So what has changed how we design storm water?**

Lee: The tools have changed substantially. Back in the 90s we were using spreadsheet with the rational method. Then we saw [pondpack](https://www.bentley.com/en/products/product-line/hydraulics-and-hydrology-software/pondpack), [hydrocad](https://www.hydrocad.net/info.htm), [hydroflow](https://knowledge.autodesk.com/support/civil-3d/troubleshooting/caas/CloudHelp/cloudhelp/2020/ENU/Installation-Civil3D/files/GUID-CB9C2634-538A-465A-8C51-9BAC0A6DC1A4-htm.html), there are various packages out there started to automate that process. The regulation also evolved to use more type of storms you can use SCS hydrograph and other unit hydrograph, different duration of storms. Even with these tools it is still a very simplistic method. In the past, it has all been focused on one site at a time, it has been pieced together for past many years. And you are left with this storm water conveyance system that was built one piece a time, and there was no master plan for it. And that’s where I see the type of modeling such as SWMM comes into play. More and more municipalities are starting to look at storm water at the watershed basis. With this approach, you are going to be able to come up with some reality based requirements for the development in that watershed, rather than the one-size-fits-all requirements. For example, if you are building a restaurant, the developer is not going to build a watershed model. But if the City already has a watershed storm water model, we’ll have much better idea the release rate the existing system can take. I think if we can move from a developer driven to a planning driven process, it will be better for everyone, especially for the owner of the storm water utility.

Mel: I am just curious, **who is in charge of reviewing all the plans and projects?**

Lee: It is generally handled during a zoning or building permit review. It varies a little from City to city and county to county, etc. More common in the zoning review, it is part of the site plan review. For example in Columbus, Ohio. They have a chapter in their zoning code says that any development has to follow storm water design manual. So as part of the approval process you have to prepare a set of plans, storm water management plans and along with a report documenting your designs, your calculations and all your assumptions, all your background such as soils. And that is just one of the permits you apply simultaneously with other permits.

Mel: **For the reviews, are they done in house or by a consultant?**

Lee: most larger community is doing it in-house. Some of the small townships without any engineers will fall back on the county, smaller cities might hire consultant to do it.

Mel: **My guess for all development, sub divisions and commercial development, the processes are all the same?**

Lee: Yes and No. Depending if there are public roads, sewers and other utilities the municipality will take over after the site is developed. If that is the case, there are additional construction requirements. Because the municipality will take over and maintain all these infrastructure. In this case, I can see having a planning tool can help the owner to know what impact it will have for the whole system. And the site specific process wouldn’t tell too much for that.

Mel: What is the typical goal of storm water drainage design?

Lee: Current rules are very empirical. For a site development, the water quality volume is calculated using an empirical equation. You need to provide treatment for the first flush, which is the first 0.75–1" of the storm, using BMPs such as a pond need to hold the water quality volume for 48hrs. For peak flow control, we size storage to shave the peak lower than pre-construction condition. ODNR rainfall water and land development manual is a great source for reference in Ohio. <https://epa.ohio.gov/dsw/storm/rainwater>

Mel: What kind of people are working on drainage designs in engineering firms?

Lee: For large firms, they have specialists who works on drainage designs every day. For smaller firms, they have generalists, they work on a wide range of projects, and they work on drainage design projects from time to time. For specialists, they are the experts. For generalists, they are usually not experts, and they don’t always know everything needed to get the design done, so the project team might need get additional trainings if the project requires.

Mel: I want to circle back on the regulation side, storm water regulations are enforced using the NPDES permit. For example for City of Columbus, it will obtain a city wide permit, and then it becomes the agency to review all site developments to make sure the drainage regulations are met. Similarly for ODOT, they have a state wide permit, and they enforce all storm water rules for road constructions in its road. What about flooding type of regulations?

Lee: A good example is the project we are working on. A low dam water intake project, we are dealing with all the layers.

* The City’s drainage manual for all the drainage on the site.
* The flood plain regulations for the modifications we made to the intake.
* The dam regulation for dam safety through ODNR to ensure the structural integrity of the dam.
* For water quality concerns in the stream such as wet lands, endangered species, we need to follow the Army Corps of Engineers rules.

Mel: I am familiar with FEMA and its flood insurance programs, what is the role of the Army Corps of Engineers?

Lee: The involvement of the US Army Corps of Engineers is confusing. The clean water act granted the Corps some of the authority on water quality. You would think the Navy would be involved in the navigable waters, but it is the army. So when it comes to rivers, usually it is the corps, sometime EPA also gets involved on water quality. And when it comes to dams, it is usually ODNR unless the corps built the dams. Then if you get into flood plains, FEMA is getting involved. So for dams that does flooding controls, it will involve the community, FEMA and dam regulations.

Mel: I’ve seen green infrastructures a lot in recent years, can you talk a little bit about that?

Lee: yes, for City of Columbus, GIs are added to the manuals in recent years. However, since it is new, we are still learning how they work. The City has shared some of the lessons they learned through their projects. For example they are requiring under drains for all GI now because of the clay soil doesn’t drain too well in this area. So it will take some time before we get all the issues figured out. And that is making it hard to model and estimate the effectiveness of green infrastructures.

[View original.](https://medium.com/p/67034fe178fd)

Exported from [Medium](https://medium.com) on March 18, 2025.