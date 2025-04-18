# The power of small batch sizes

Coding is one of my hobbies, I’ll consider it a great day if I can find a way to get my job done by writing a piece of program. The more I…

---

### The power of small batch sizes

![https://cdn-images-1.medium.com/max/1000/1*X6Thw1aGQMkWrzkw5ZLg0A.png](images\1_X6Thw1aGQMkWrzkw5ZLg0A.png)

Coding is one of my hobbies, I’ll consider it a great day if I can find a way to get my job done by writing a piece of program. The more I write programs, the more I realize building models is very similar to building software.

Since software is a much bigger and mature industry, I am very interested in what developers might say about solving my modeling challenges. And that gets me into reading books and articles about [DevOps](https://en.wikipedia.org/wiki/DevOps), the latest iteration of the software development management framework that is widely adopted by the industry.

I learned a lot from the DevOps framework. Today, I would like to share the power of [Small batch size](https://queue.acm.org/detail.cfm?id=2945077).

So what is small batch size? Say we have a model with 5 basins, the traditional way will be to build a single model once with all the basins. In contrast, when applying the small batch sizes, we’ll start with one of the upstream basins, and then go through calibration and capacity analysis for the basin in our first try. Once that is done, we’ll add another basin to the model, and then go through the whole process again. We’ll repeat the same process until we have all the basins added to the model.

Most of you might immediately say, that’s a crazy idea. Let’s think about a much simpler situation, and that might change your mind. Say you need to bake 1000 cookies. It makes a lot of sense to bake all of them in one batch. However, if it is your first time baking cookies, the chance that you’ll do something wrong is quite high, say it will take you a few tries to learn your lessons, you are going to waste a lot of cookies.

So if you are honest about your baking skills, a better way is to bake the cookies in smaller batch sizes. Let’s cook 200 cookies a time, and in the first few batches, you’ll learn a lot about what can go wrong without worrying about throwing thousands of cookies away. You see, it is just common sense, when you are not sure about yourself, take baby steps to reduce waste and stress.

Now back to our modeling world. I think the reason most modelers might be against the idea of small batches is that many of us are terrible at estimating the true effort required building a model, we are way too optimistic about our ability to devise a perfect plan without making any mistakes.

Fortunately for me, at one time I had a boss who is fully aware of this bias, he will double my estimate for my tasks when preparing for the project schedules, and that usually worked out pretty well.

What we need is to face the reality, building a model is not building a Lego set, there is no well established instructions that can guarantee success in one try. No two modeling projects are the same, when doing something new, it is natural for us to fail a few times to learn the right way.

For example,

* as you are writing the report by the end of the project, the client realized that we need to evaluate the inlets performance, however, you never calibrated your model for the inlets. A small batch approach will identify this lack of understanding in the first basin model at the very beginning of the project. Everyone makes mistakes, we need to create more opportunities to catch these mistakes at the beginning of the project.
* you need to submit the modeling results in a week, and it is the first time you run the model because it took twice as long as you estimated! And you couldn’t get the model to run. A small batch approach will expose the problem much earlier, and since the model is much smaller, it will be much easier to fix the problem.

I hope now you are convinced that small batch size might not be that crazy an idea. So how should we break the model into small batches? Our modeling industry is far behind on a management framework similar to DevOps, which requires a lot of tooling to automate the whole process. However, I do believe there are a lot of things we can already do without waiting for the tools to be available.

* First, I like the philosophy of continuously delivering values to the customer throughout the project. The owner of the model doesn’t care what software we are using, and how we calibrated the model, etc., what they need is a master plan. Instead of giving them that master plan at the very end of the project, is there anything we can do to give them something that has true value for the owner during the project? Can we just model this basin and give recommendations for this pump station next month instead of next year? This might not work for every customer, but I think many will perceive this as benefits.
* Second, think about reducing waste. Identify the most uncertain part of the modeling project, how can you break up the model so that if you make a mistake, you are not going to throw weeks of work out of the window. Not sure about the hydrology method? Then do a pilot basin and spend some time to get confident about your approach.

The software industry has proved building software in small batch sizes and releasing more often can reduce waste, stress and increase the quality of the software. I think it is time for the modeling community to take a page from this game plan to improve our model building process.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [December 27, 2021](https://medium.com/p/895017c9be6d).

[Canonical link](https://medium.com/@mel-meng-pe/the-power-of-small-batch-sizes-895017c9be6d)

Exported from [Medium](https://medium.com) on March 18, 2025.