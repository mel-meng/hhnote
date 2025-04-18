# How to share XPSWMM models

source: Innovyze Support Portal

---

### How to share XPSWMM models

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-share-XPSWMM-models)

XPSWMM models work best in a single user environment, therefore, any time we need to sharer the model with someone else, we need to archive the model and send a copy.

In this article, we’ll go over a quick summary of the common external files a model will use and a few recommendations on best practice of sharing the models.

### Using the Transmit Model tool

The best way to share a model in most cases is using the transmit model tool. Check the files you would like to be included and uncheck the ones you don’t need. Then a zip file will be created with all the file paths correctly linked.

![](images\1_rEumpCU41BfkIQen8kX9uQ.png)![](images\1_HDbAXkbrfm-sWOgkS5obLw.png)

When another user receives the zip file, just unzip it, and open up the \*.xp model, the included external files should be correctly referenced.

### Review referenced files

When using the transmit tool, it is a good practice to review the files listed in the window.

* make sure all the external files are used, outdated files should be removed
* make sure all the external files are saved in an appropriate location that will not be deleted

Most of the files included can be located in the layer tree panel.

![](images\1_Kqp2gxIb09k9_x_1Q9Ir2Q.png)

Hot Restart file can be access through the HDR settings,

![](images\1_ehuw9GYRnM0S6jz3gT9EzQ.png)

Interface file can be accessed through the configuration menu.

![](images\1_cUi0CZjBlHMyG8zasBbFyQ.png)

Rainfall file is defined in Global data

![](images\1_xf0TIkxdcdh-tzvqnywa4A.png)

Gauged data file is defined for the node

![](images\1_mwDWzabWsnthxD7YvggUwg.png)

### Tips for transmitting a model

When exporting results, it is highly recommended to make sure there are no other models in the same folder, otherwise, XPSWMM will also export the results from other models. To get around this situation,

* create a new folder for the model
* save the model as a new model in the new folder
* run the model to get the results
* now you can transmit the model with only its own results in the zip file

Most of the externally referenced files in the 2D settings are not automatically included in the transmit zip file. If they are used, the user need to send additional instructions on how to link to these files.

![](images\1_YjVtROgEIPTv_K8CSjBylA.png)![](images\1_qejlftSrJcnmQux4vr6kzQ.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 6, 2021](https://medium.com/p/875ba2221a2f).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-share-xpswmm-models-875ba2221a2f)

Exported from [Medium](https://medium.com) on March 18, 2025.