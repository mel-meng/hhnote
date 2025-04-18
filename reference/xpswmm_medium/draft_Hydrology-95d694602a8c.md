# Hydrology

outline:

---

### Hydrology

outline:

* big picture what is hydrology
* what are the major component
* initial loss
* infiltration
* ground water
* the interaction with rainfall short term and long term
* use swmm5 subcatchment to show its impact

The figure below from the HEC-HMS technical manual and GSFlow manual show the major processes at a local level that relevant to drainage systems.

![](images\1_XqPunRSkdz927yCAi3Cczw.png)

For the typical drainage design, our main focus is to model a system with a design storm less than 24hrs. In such situations, we can ignore the ground water process as since it will not change during the simulation. However, for continuous simulation where the stream and ground water can play a much important role in the results.

![](images\1_iaLuyqhBziHszoVHpsyZhQ.png)

The main thing we need to work on are the losses from the rainfall,

* intercepted/stored:surface storage of watter by trees grass, local depressions, cracks and crevices in parking lots or roofs
* infiltrated: water moves into the soil
* evaporated or transpired: TODO

We will start from a simple case then evolves into a more complicated case.

Let do a really simple experiment with SWMM5 hydrology to learn more about the routing of subcatchment.

![](images\1_FQWynCrU6ENEZ_6oEF1TPQ.png)![](images\1_1U85MOQeFWcqQSUGfB9HNw.png)

[**How does XPSWMM model evaporation**  
*source: Innovyze Support Portal*mel-meng-pe.medium.com](https://mel-meng-pe.medium.com/how-does-xpswmm-model-evaporation-85c7d12db0fe "https://mel-meng-pe.medium.com/how-does-xpswmm-model-evaporation-85c7d12db0fe")

![](images\1_bjnYjCuACECDzeeG7madTg.png)

If we have constant rain falling on a subcatchment, eventually it will reach steady state.

The width sensitivity analysis.

![](images\1__kwVMI4DBKdvZoWqyNq3iQ.png)

[**Subcatchment width sensitivity analysis**  
*This example demonstrates the sensitivity of the subcatchment width parameter used in the SWMM5 non-linear reservoir…*www.openswmm.org](https://www.openswmm.org/Topic/9861/subcatchment-width-sensitivity-analysis "https://www.openswmm.org/Topic/9861/subcatchment-width-sensitivity-analysis")

[View original.](https://medium.com/p/95d694602a8c)

Exported from [Medium](https://medium.com) on March 18, 2025.