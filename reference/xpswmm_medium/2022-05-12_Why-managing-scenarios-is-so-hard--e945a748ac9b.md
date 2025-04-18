# Why managing scenarios is so hard?

Managing scenarios in a model over a long time is challenging, no matter who does it, what software you use, you might feel hopeless at one…

---

### Why managing scenarios is so hard?

![](images\1_Xu8pR8JzO90fW-XCin6k3g.png)

Managing scenarios in a model over a long time is challenging, no matter who does it, what software you use, you might feel hopeless at one point or another.

Before the use of a scenario manager, things are much simpler, what you have is all it is, there is no history in it. However, the downside is that if you make changes to something that is in all the scenarios, you’ll have to change all the models manually.

When people are using a scenario manager, they can save a lot of time by making changes once in the base. However, there is a cost to pay down the road when using a scenario manager.

Here is an example, say you need to make some changes to your model 3 years after it was first created. The problem is at that time it is no longer very clear which object is in the base, and which object is in an scenario. To make things worse, we actually track changes at the attribute level, so for example, we might want to keep the diameter for a pipe defined differently in a scenario but we want to use the manning’s n from the base. It can get complicated very quickly, so when the modeling results start to look funny, you know it will take some time to sort things out.

So is there an easy solution to this problem? I think there are things you can do to make things easier, but I doubt it will ever be easy. If we use the software industry as a benchmark, we can see the maintenance cost of a piece of software is much higher than creating the software in most cases, to be more specific, adding something to the software and making sure it doesn’t break is not cheap. Since software is updated a lot more often than models, the incentives to bring the cost down is much stronger in that industry. Since the software industry couldn’t figure out a way to dramatically reduce the cost of making changes to a software, I am not very hopeful we can make it dramatically cheaper managing changes to models.

With a much modest expectation of what a scenario manager can do helping managing changes, here are a few thoughts I have about possible improvements.

There are two type of scenario managers, I would call them implicit vs explicit.

* InfoWorks ICM/XPSWMM uses an implicit manager, the software will compare the values in the child scenario with the base scenario, if they are different, the software will infer the inheritance is broken. So the difference is implied. And in general, the user cannot alter the values automatically logged by the software.
* InfoSWMM uses an explicit manager. Tracking the changes are still managed by the software automatically, however, the change log is a open book. The user decides where to save the changes and can overwrite the values later if needed.

Like most things in life, they are both useful solutions to the same problem. Neither one is perfect.

I personally prefer ICM’s scenario management because it doesn’t allow anything “fancy”. You can only have a base and a child, no grandchild. And the only inheritance rule is that it compares the values between base and child, if they are the same, then it is inherited from base, if not, it is a scenario specific value. From my experiences if you want to maintain something for a long time, it has to be as simple as possible. All the smart tricks you planted in the model can become bombs at a later time.

And I would recommend most projects to follow the same advice, only limit your use of your scenario manager to do something very simple. It will make it much easier for the next person to figure out how to update the scenarios.

Another suggestion I have is to keep all your objects in the base, instead of creating new objects in child scenario, enabling and disabling the objects from the base. Again, the idea is to keep things simple, everything should come from the base first, then we make changes to it.

However, for planning projects with lots of scenarios, the more advanced features of a scenario manager can be a huge productivity booster. In such situations, I would recommend a detailed memo explaining the dependencies between all these scenarios, and write instructions on how to make future updates to the model. More than likely the person who will make the changes will know nothing about the model.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 12, 2022](https://medium.com/p/e945a748ac9b).

[Canonical link](https://medium.com/@mel-meng-pe/why-managing-scenarios-is-so-hard-e945a748ac9b)

Exported from [Medium](https://medium.com) on March 18, 2025.