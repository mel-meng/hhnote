# How to update a model without breaking it?

Updating a calibrated model is one of the most annoying modeling tasks I can think of, not only that it is tedious, it can break the model…

---

### How to update a model without breaking it?

Updating a calibrated model is one of the most annoying modeling tasks I can think of, not only that it is tedious, it can break the model and lead to hours of frustration trying to fix it.

Here are a few examples,

* we are calibrating and preparing a master plan while a survey crew is updating the pipe inverts. So we need to update the model every 3 to 4 weeks with the new data
* As the modeler for the latest master plan, the utility sends us as-built drawings every 6 months to update the model.

These tasks are very challenging because most modeling teams have their workflow optimized for creating new models, not maintaining existing models.

When building a new model, we can move very fast without worrying about breaking the calibration. I am going to calibrate the model two months later, want to change this pipe, not a problem.

However, when updating an existing model, the beautifully calibrated model can suddenly look ugly after some changes.

So what should we do?

* First, I would like to share the comforting news, we are not alone. No matter what you do, sooner or later you’ll suffer from something like this. If you do a little research on software development, maintaining a piece of software is just as challenging, and that’s why programmers are very interested in management frameworks such as Agile development and DevOps to make their life easier.
* Second, as we are moving closer and closer to the vision of digital twins, modeling will see the same shift the software industry did, we’ll switch from a release cycle of every 5 years to a continuous release cycle. The focus will shift from how to create a new model to how to continuously update the model without breaking things.

Before our industry starts to widely promote and educate the workforce to embrace the changes as the software industry did in the past 10 to 20 years, as individual modelers, we’ll need to learn a few new skills to make our life a little easier. I am going to share a few very simple strategies using tools like Excel, ICM versioning and scenario manager.

### Manage Changes

As I am updating the model, managing the changes is the last thing on my mind. All I want is having a working model after the updates, the model still runs fine, and all the calibration still holds up reasonably well. What I don’t want is spending hours and days figuring out why it is not doing it supposed to do.

And it just happens that managing the changes is the best way to minimize the extra work of fixing the model after we made the changes. The proven workflow is,

* make small changes and save your model often
* automate the checking process so that you can run it often and catch the error early
* rollback the changes that caused the problem if needed
* review the changes incrementally to identify the issues

I will cover these topics in several articles.

* Update a model from external source, the responsible way
* Managing changes using versioning and scenarios
* Automate the testing
* Cherry pick the changes in your revision history

By [Mel Meng](https://medium.com/@mel-meng-pe) on [December 17, 2021](https://medium.com/p/841a1d022e57).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-update-a-model-without-breaking-it-841a1d022e57)

Exported from [Medium](https://medium.com) on March 18, 2025.