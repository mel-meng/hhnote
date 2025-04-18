# PySWMM : Interview with Bryant McDonnell (3 of 3)

This is part 3 of the 3 parts interview with the creator of PySWMM

---

### PySWMM : Interview with Bryant McDonnell (3 of 3)

![](images\1__k2hjOWviqs5dIOn35w0Xw.png)

This is part 3 of the 3 parts interview with the creator of PySWMM

[Part 1: The conception of PySWMM](https://medium.com/p/e9be5cf0a62f)

[Part 2: The Evolution of PySWMM](https://medium.com/p/f5243a59de9b)

[Part 3: Advice and future of PySWMM](https://medium.com/p/4ec86cd5c2ef)

**Mel: Recently there has been a lot of discussion about deep learning, neural networks, how does PySWMM fit into that?**

**Bryant**: awesome question. Philosophically, we would like to think PySWMM separates the concerns out. We are creating a communication conduit between SWMM and the higher-level language python. For PySWMM itself we have no plans to include any machine learning libraries. But I am amazed to see that several universities started to develop plugins for machine learning. The biggest piece we’ve been seeing is that hydrological responses are being represented with a machine learning process. As human being, we used to have to calibrate models manually with simplified approaches. I’ve seen some of the hydrology machine learning models that are compelling. It doesn’t take a million dollars to build, and it runs very fast and it is just as good as the traditional method.

**Mel: what are other fun things about PySWMM?**

**Bryant**: I’ve attended a few conferences where people were presenting PySWMM. I don’t have children, but I think my feeling sitting in the audience watching is like watching children graduating high school or something like that. There has been a lot of relationships built out of PySWMM. We’ve got solid relationship with several people at US EPA in Cincinnati where SWMM5 and EPANET were born.

**Mel: Any lessons learned so far?**

**Bryant**: I have learned a lot from this project. There are some architectural things, including the thread safety and the re-entrance issue. Another one is I wish right out of the gate I would have been able to start with SWIG, simple wrapper interface generator. Eventually, swmm-python will be the low-level interface code within PySWMM instead of the ctypes we use now. I wish I had started with that, and that will make the process a lot easier.

**Mel: Any advice for people who are interested in doing what you do?**

**Bryant**: I think learning Python, a “higher” level and language, when in college would really help. For people who are interested in hydroinfomatics, I would recommend learning Python. Modelers manage so much data, and having automatic means managing, presenting, and interpreting that is such a foundational skill.

**Mel: What advice do you have for people?**

**Bryant**: Think big and think interdisciplinary. The water challenges we are facing now and will face in the future require us to be perpetually dissatisfied with the status quo. I like to think there has always got to be a better way. Please join me and my colleagues achieve this vision by contributing to PySWMM.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 7, 2020](https://medium.com/p/4ec86cd5c2ef).

[Canonical link](https://medium.com/@mel-meng-pe/pyswmm-interview-with-bryant-mcdonnell-3-of-3-4ec86cd5c2ef)

Exported from [Medium](https://medium.com) on March 18, 2025.