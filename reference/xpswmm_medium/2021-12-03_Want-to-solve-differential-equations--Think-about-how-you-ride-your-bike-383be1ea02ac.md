# Want to solve differential equations? Think about how you ride your bike

If you’re serious about modeling, you’ll need to understand how the engine solves differential equations sooner or later. So the next time…

---

### **Want to solve differential equations? Think about how you ride your bike**

![](images\1_9uElnvWuImoA-CqyNdK8xA.png)

If you’re serious about modeling, you’ll need to understand how the engine solves differential equations sooner or later. So the next time the engine does something strange, you’ll know what to look for.

Most people, I believe, are like me in that they cannot derive their intuition from equations; it must be something they already know. Riding a bike is it for me.

So, what’s the big deal about riding a bike? To have a smooth ride, unlike driving a car, you must not only maintain a constant speed, but also maintain your balance.

The secret is that I can do it without thinking about how I’m going to do it. This, I believe, is the key.

* I always know if I am going to fall to the left or right
* I also know how to adjust my speed, shift my weight and turning the handle to counter the fall

That gives you a basic understanding of how an engine solves differential equations. Consider how water flows through pipes.

* water will flow through the pipe at a speed (Q, the flow), just like having a smooth bike ride
* as water moves through the pipes, you’ll have less water (H, head) on the upstream end, and more water on the downstream end (H, head), essentially, you are off balance, the speed of the water needs to change so that everything is still in balance.

Now let’s visualize a special machine, while you are pedaling the bike, it moves the water through the pipe (Q), and the level (H) of the upstream and downstream end will tilt your bike, in order to stay in balance, you not only need to adjust the speed (Q), but also the tilt (H).

The engine’s job is to figure out how to keep this unique water bike balanced.

· By plugging the speed and the levels into the equation, the engine will know if I am going to fall

· since we know how to counter the fall, we’ll adjust the speed (Q) and the tilting (H) until it is balanced

Just like riding a bike, the first push doesn’t matter that much, the engine will guess some initial values for flow and head from the existing information just to get started, once things start to move, it can quickly figure out how to stay in balance.

Now we can use our new intuition to answer some questions.

**Why does the time step matter?**

A time step decides how often I check if I am off balance or not. If it is too small, it is like I shift to the right at one moment and immediately shift to the left to avoid the fall. It will take some time for the bike to get to a balanced state, and I don’t need to react to every signal I got.

On the other hand, if the time step is too big, I could already fall to the ground before my next check.

Therefore, ideally, I would have a time step that is not too long that I might get myself into trouble, also not too small, that I am making all these unnecessary adjustments way too soon.

**Why does the length of a pipe matter?**

When we ride a bike, for every second, we adjust how we ride to go through the next few feet and keep repeating this process.

For SWMM, the length of the pipe is explicitly defined as how far we plan for our next move. The biggest potential issue with this approach is that we can only make one move through the pipe, no changes are allowed while we are halfway through. And this can cause two types of problems.

If the pipe is too short, and the-time step is too long, I could be riding my bike outside of the pipe when I check my status next time. It is like blindly riding a bike through a tunnel. And this is what the famous courant number is for, when the wave can travel out of a pipe for the time step, the math can explode.

On the other hand, if the pipe is too long. Just like riding a bike, there is no way you can ride through a long stretch of road exactly the same all the way through, most likely you are going to fall if you do that. So, you need to break the path into smaller segments to be safe and adjust more often.

**Why does the model get unstable?**

Numerical methods can be the source of instabilities as the few examples above showed. The model itself could be unstable, too.

Imagine you ride your bike and hit a big rock in the middle of the road. I bet if I hit the rock 10 times, the results will not be the same. Any small changes in how I approach the rock can result in very big difference in the outcome.

This is just the nature of having abrupt changes while riding a bike. It is the same thing while solving differential equations. When you have abrupt changes such as inverts, pipe sizes, roughness, or the equations change (open channel to pressured flow, pipe flow to weir flow, etc.), a small change in how the flow hit the change can lead to very different outcome, and it can be quite unpredictable.

**Summary**

I hope my little trick can help you feel more comfortable with differential equations. In many ways, it is like how I ride my bike, balancing myself one time step, one path segment a time.

A more accurate analogy would be learn to ride a bike. But I just found that less “intuitive” to me.

The riding a bike analogy is more suited for real-time control. Surprisingly, real-time control and solving differential equations are two sides of the same coin, solving differential equations is given input time series to get the output time series, and real-time control is the reverse, given the desired outcome and figure out the input. It could be another interesting topic to discuss.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [December 3, 2021](https://medium.com/p/383be1ea02ac).

[Canonical link](https://medium.com/@mel-meng-pe/want-to-solve-differential-equations-think-about-how-you-ride-your-bike-383be1ea02ac)

Exported from [Medium](https://medium.com) on March 18, 2025.