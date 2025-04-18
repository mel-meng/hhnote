# Update a model from external source - the responsible way

After spending 3hrs updating the model from external drawings and tables, the thought that I need to spend another hour or two to check the…

---

### Update a model from external source - the responsible way

After spending 3hrs updating the model from external drawings and tables, the thought that I need to spend another hour or two to check the results doesn’t sound too pleasant. What should I do?

We can easily come up with a thousand reasons why we shouldn’t do it at the moment. However, we all know the errors introduced to the model can cost us hours in the future, the longer we wait to fix it, the more it will cost us.

So how can we turn this around? Here is a few things that worked for me, sometimes I even find it fun doing some of the tasks,

* we should always check our work, developing a consistent workflow to ensure all the proper checks are done, and making it a habit
* using the model’s results as a check
* automate the tedious tasks
* think of creative ways to check the results without re-do the work

### Workflow

Updating a model can be really simple, adding a few pipes of a new subdivision, no complications.

The really complicated situation is to update an existing part of the model with as-built drawings which looks very different from how it was modeled.

I found visualizing the process as the actual construction process can be very helpful.

### An Example

As shown below,

* in our model, we have the proposed relief parallel sewer modeled as AEFD
* as the as-built drawing is turned in, we noticed that the parallel was built differently from the existing model, instead of connecting to D, a new manhole M6 was created to tie the parallel back in

![](images\1_FLE-wnq2EnCHK1OUm1tSnA.png)

 Let’s think through the construction steps,

1. remove pipe CD
2. create a new manhole M6
3. create new pipes M3-M6, M6-M4
4. adjust node E(M7)
5. adjust node F(M8)

![](images\1_zZI2KpVgOrqUceZLwTg-Cw.png)

How are we going to get through each step?

* build a record of the existing condition
* build a record of the as-built condition
* map the action for each element in the existing condition
* map the action for each element in the as-built condition
* break the updates into a few steps
* carry out the updates
* check the results

First, let’s identify all the modeled objects that need to be reviewed and create a table to track these changes.

![](images\1_s3w5o9rLWyYhNucW6jgjeg.png)

I found Excel can be very efficient and flexible tool for matching things up. It is a two way process.

* match everything in the model to the as-built
* match everything in the as-built to the model

Let’s check the nodes first, as shown below,

* the “model node” column shows all the node from the model
* the “as-built node” column shows all the node from the the as-built model
* the action column shows how we are going to match them

![](images\1_zTrh3pgm7hdCj3l9yhH5Hw.png)

The key for this exercise is to keep everything from both the model and external source matched.

Similarly we can map the links,

![](images\1_6819rtV0wVehJYsYkfaNhA.png)

With everything mapped both ways, we can break up the updates,

1. remove the pipe
2. add a new node
3. update the nodes and pipes information from the as-built drawings

ICM has some nice tools to facilitate this process.

* create a development scenario where we can easily compare the before and after condition

![](images\1_g3X-y9zmY_IhOVAurLKFrw.png)

* create selection list for each of the step

![](images\1_ca3-sVryr7c_m8r8W_AXig.png)

* carry out the steps.

![](images\1_pOGQOSbF6feku-k-mSCeUw.png)

The key to this process is to have the discipline to slow down and develop the mapping tables to make sure every element is accounted for, and create the list from the tables.

The nice thing about this process is that you can easily check your work by dragging the selection list into the model and quickly confirm the elements are the right ones to be updated.

When it comes to updating the model, I found using the vlookup function is a quick and reliable way to match things up.

1. select all the nodes from as-built
2. ensure they are the correctly shown in the map
3. opening the records of the selected manhole grid, copy the NODE ID column to Excel

![](images\1_0hJ0XjX41RcbRUeXBqjLzg.png)

In Excel, we can get the as-built node name using VLOOKUP function.

![](images\1_2xbv1gA4KsUtv6-b6Nrpcw.png)

Similarly, we can get the updated X, Y coordinates from the as-built table using the VLOOKUP function.

![](images\1_l3TRatxhLVlIAnzeMkW3xQ.png)

After that we can paste the updated X, Y back to ICM. Make sure the flag is turned on, so that any data that is changed will be flagged.

![](images\1_5YAt5a92XguY-birdAZQPA.png)

The updated network is shown below,

![](images\1_O4xX3FFI6Je-EIbMGf7hpg.png)

As you can see, this process can get complicated quickly. One thing that can greatly improve modeling productivity is using [small batches](https://queue.acm.org/detail.cfm?id=2945077).

Small batch size is a proven technique used in manufacturing and software development. When applied to model building, what it means is this. Instead of building the model in a series of steps such as build the network, calibrate the model and then perform the capacity analysis as major milestones, we go through all the process many times. Below is an example.

Say we have a model with 5 basins, instead of getting all the 5 basins into the model before we do the calibration, we’ll build a much smaller model for one of the basin all the way from importing the GIS to the capacity analysis. Then we start to work on the second basin, etc.

It might seem counter-intuitive at first, because with this process we are building 5 models instead of a single one, therefore, we will spend 5 times the effort.

I usually will divide the as-built drawing into a few smaller areas. This is another good practice, to break up the work into smaller pieces, so that we can check the update earlier and more often to identify issues.

Then, we create a similar table for the object in the as-built drawings.

Imagine how you can demolish the existing pipes in the model then build the new ones as shown in the as-built drawing can help us easily go through the steps below,

* identify all the changes in the as-built drawings
* identify all the objects need to be changed in the model
* map the change for each object from the as-built to the model
* develop a sequence to make the change
* build automated process to make the changes
* verify the changes are made correctly

[View original.](https://medium.com/p/efeb33ad497)

Exported from [Medium](https://medium.com) on March 18, 2025.