# How to use RTC in XPSWMM

Source: Innovyze Support Portal

---

### How to use RTC in XPSWMM

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-use-RTC-in-XPSWMM)

In XPSWMM, RTC is implemented as simple logical rules based on the state variables of the modeled objects. The challenge is that most of these variable can only be accessed for the current simulation time.

If we imagine we have an operator working inside the model who enforces the RTC rules. This person will be like Dory in Finding Nemo who suffers from short term memory loss. This person doesn’t remember anything just happened, all this person does is looking at the current values of all the pipes and nodes, then apply a set of rules.

Therefore when designing RTC rules, we have to imagine a world without a past and a future, we only live in the NOW. Anything that relies on past information has to be inferred from a variable that is available to us now.

In this example below, we have a storm event flow coming into the model from Node 1, then it goes into the storage node. When the water level in the storage is below 3.2ft, we would like the flow to go to WWTP. However, once the water level is above 3.2ft we would like to protect the WWTP and close the pipe “ToWWTP” and open “ToOverflow” to Overflow.

![](images\1_DbE-EXuk6vopgBnQ31wNVg.png)

Here is our first try, the results is shown below,

* at the start, “ToOverflow” closes, and “ToWWTP” opens
* when the water level is above 3.2ft, “ToOverflow” opens and “ToWWTP” closes, and the water level keeps rising
* as the water level drops below 3.2ft, “ToOverflow” closes, and “ToWWTP” opens

![](images\1_QGHfyrnz_-eJe4fm-O800w.png)![](images\1_lJ7V4dsrA5MgNaAMH6AblA.png)

This is not exactly what we need, but pretty close. What we need is once the overflow is activated, we would like to keep it open for the rest of the event.

However, as we have discussed when using RTC, you cannot have prior knowledge, there is no direct way to tell RTC to keep the gate stay the way it is once overflow is triggered.

Let’s see how we can resolve this issue. First let’s list all the variables,

* time: the time from the start of the simulation
* flow in pipes
* water level in nodes

To understand how XPSWMM does RTC, we can turn on the RTC logging.

![](images\1_nXkyg9mkGj9csoNUQ_DHVg.png)![](images\1_iKFHIksAG08ZP4lx51LkPg.png)

With RTC logging enabled, we can see how the RTC rules are applied at every time step.

![](images\1__ItSljengrnb4iKjyg9KEQ.png)

Table E4b shows the rules,

![](images\1_n_RjwKL1XRilmSKFilMDTQ.png)

For the close\_toWWTP rule, we close the gate to WWTP if simulation time is > 0 and the storage water elevation > 3.2ft. It is common practice to include simulation time in the rules, when everything failed us, we can still manually direct the operation using the time. Say if we know at time 5hr, we need to bypass the flow, using the time variable we can easily achieve that.

It is (time >0) AND (storage elev>3.2)

What is not implicitly said is that when the rule is false, the pipe will be open as it is modeled.

For the close\_toOverflow rule, if the gate toWWTP is open, then we close the toOverflow gate:

(time >0) and (toWWTP flow >0)

Here instead of defining the exact condition that the overflow should be closed, we are simply saying, if the toWWTP is open, then toOverflow should be closed.

Next, we can take a look of the RTC log,

![](images\1_yR3AO3_kpj0X3LT4ZWHuyw.png)

As shown in the log, it is just simply logical calculations of the rules we defined.

As you have seen, translating our desired operation into the rules is not a straight forward process, we need to turn our ideas into logical rules applied to state variables.

To get familiar with the rules, refer to the examples in the [XPSWMM online help](https://help.innovyze.com/display/xps/Real+Time+Control+Examples).

In this example,

* the easiest part is when water level is above 3.2 ft in the storage node, which can be directly translated into a rule
* In our operation, there are dependencies between WWTP gate and the OVERFLOW gate. Only one gate should be open at any time, when one is open, the other must be closed.
* expressing such dependencies between different objects can be hard using logic test of state variables
* another difficulty is the lack of the “if..then” structure, therefore, it is up to the modeler to ensure the logic test are not overlapping

Here are a few things we did to overcome some of the challenges,

* Since each gate only has two operation conditions, open and close. We only need to define when the gate should be closed, when the rules of closing the pipe is False, the pipe will be open.
* Since at any time only one gate should be open, we can define the operation of another gate as the opposite state, to ensure we don’t have convoluted logics define.

As shown below,

* the close\_toWWTP rule says close the WWTP gate when Storage is above 3.2
* and the close\_toOver rule says close the OVERFLOW gate when there is flow in the toWWTP gate

![](images\1_63G0X64ERKdq0mMNVSWiBQ.png)

Our next challenge is to keep the gate opened, even when the water level drops below 3.2.

This is achieved by adding one more condition to the close\_toWWTP rule,

By adding an “OR” condition to check if the “toOverflow” gate has flow in it. So once the OVERFLOW gate is open, with the “OR” operator, the rule will stay true regardless of the water level in the storage, and that will keep the gate closed.

![](images\1_qm2Rxt9x0D2fHVZU9IlHIg.png)![](images\1_w_WVkRSQDIqF3qZQ1cWg8Q.png)

You can find the sample models on [github](https://github.com/mel-meng/xpswmm/tree/master/models/rtc).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [June 11, 2021](https://medium.com/p/d1c35078d67d).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-use-rtc-in-xpswmm-d1c35078d67d)

Exported from [Medium](https://medium.com) on March 18, 2025.