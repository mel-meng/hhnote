# How to model hydrology in a 2D model?

For stormwater models, selecting the right hydrology method is probably the most important modeling decision to consider, especially for…

---

### How to model hydrology in a 2D model?

For stormwater models, selecting the right hydrology method is probably the most important modeling decision to consider, especially for models with very limited calibration data, the results will be largely determined by the hydrology method.

1D hydrology methods have been widely used, and if the model is for a permit application, the drainage design manual usually will have detailed instructions on the calculating the hydrology. However, 2D hydrology is rarely discussed in the published design manuals in the United States. Due to the lack of “regulation” on 2D hydrology, when 2D hydrology is used calibration is usually required for the model reviewer to judge the mode’s accuracy.

Without calibration, it is very hard to judge if one method is better than another. The 1D hydrology methods established from statistical models have a huge advantage over the more physics based methods in such situation,

* because the statistical model based methods are backed up by studies with lots of observed data, the input data can be easily and more accurately measured, and its accuracy and uncertainty is well understood.
* the physics based methods on the other hand, in general will have more input parameters, and usually a few key parameters cannot be accurately measured and thus can lead to bigger uncertainty than the statistical models.

### Rain on grid

Rain on grid is a distributed hydrology model. It has two components, one is the routing of the rain falling on the 2D cells, and another part is the infiltration happening when water flowing through the 2D cells. A few parameters that can lead to high uncertainties are,

* the resolution of the grid, the results can be highly dependent on the size of the grid, for example using 1ft grid might give very different results than using a 10ft grid.
* TODO:

### Rain on grid vs 1D hydrology method

In theory, rain on grid is a much better approach than the traditional 1D hydrology. However, in practice it can be a lot more complicated. We have to admit that the hydrology process is very complicated, the science and technologies are not there yet for us to cheaply and accurately predict the hydrology process.

One of the major challenge is the lack of observed data to calibrate a model. Without calibration data, a physics-based model with a large number of parameters can be at disadvantage. Because usually the results can be quite sensitive to some parameters that cannot be accurately measured, thus without a calibration, the uncertain of the modeling results can be quite high.

Therefore, many widely used hydrology methods were developed using statistical models, instead of trying to understand the physics at the detailed level, medium to large basins (lumped models) of similar characteristics were compared to derive a model that can be easily parameterized with easy to measure characters such as area, time of concentration, slope, etc.

If you do have good calibration data, in general you’ll find it is much easier to calibrate the model using a physics based model because the meaning of calibration parameters are well understood. The SWMM runoff method is one of such methods, watershed is divided into distributed smaller subcatchments with uniform land cover, and a physics based routing equation can be applied to each subcatchments to generate complicated flow patterns. In many ways, rain on grid just extended the SWMM runoff concept a step further by dividing the watershed into even smaller “subcatchment”.

 Unfortunately, most of the widely used hydrology methods were developed before rain on grid was invented and there is limited guidelines on using rain on grid for projects without calibration.

Comparing with a distributed 1D hydrology method such as the SWMM runoff method, the basic idea is quite similar, the main difference is that for 2D you can rely on the 2D routing method to ensure the flow path is correct, while in the SWMM runoff method, it is up to the modeler to delineate the drainage area into logical subcatchments to ensure the flow path is correct.

So far so good, things are getting more complicated once we add the underground pipes into the picture. For a simple design project, the underground drainage system should be able to convey all the runoff without any overflowing. And thus, once the runoff hit a storm inlet, it will never come back to the surface.

However, if the area has flooding issues. Things can get more complicated, the water can overflow from the underground pipes and flow over the surface, therefore, additional infiltration can happen. And how should we model this process?

For the infiltration, again it is your decision to make, the way the model works is “wrong” one way or another when you use both 1D hydrology and 2D infiltration, it doesn’t reflect reality.

* When you are modeling infiltration in both subcatchments and in the 2D, you are double counting the infiltration if your subcatchments overlaps your 2D areas. You need to decide if that is a problem or not.
* You can turn off infiltration in 1D, but that is wrong because only when using subcatchment water flows directly into a manhole, infiltration only happens when water is overflowing to the 2D area.
* You can turn off the infiltration on 2D, but that is also wrong, because when water is overflowing to the 2D, no infiltration will happen.

[View original.](https://medium.com/p/f41ca2114236)

Exported from [Medium](https://medium.com) on March 18, 2025.