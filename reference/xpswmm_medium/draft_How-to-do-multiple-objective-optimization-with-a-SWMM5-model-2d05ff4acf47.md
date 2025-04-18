# How to do multiple-objective optimization with a SWMM5 model

This blog is part of the Generative design series. In the previous blog, we showed how you can write python code to modify the model…

---

### How to do multiple-objective optimization with a SWMM5 model

This blog is part of the [Generative design](https://mel-meng-pe.medium.com/generative-design-66c90e1b6120) series. In the previous [blog](https://mel-meng-pe.medium.com/how-to-create-run-modify-a-swmm5-model-using-python-2ebaf7fd497), we showed how you can write python code to modify the model parameters and then extract the results.

Next, we’ll run an optimization program to tweak the model parameters to find the best values for us automatically.

We will use the [pymoo](https://pymoo.org/index.html) to do optimization for us. With only 11 lines of code below, we solved our problem using genetic algorithm!

![](images\1_6eDEEG4wGmjrtdUqslifZA.png)

[View original.](https://medium.com/p/2d05ff4acf47)

Exported from [Medium](https://medium.com) on March 18, 2025.