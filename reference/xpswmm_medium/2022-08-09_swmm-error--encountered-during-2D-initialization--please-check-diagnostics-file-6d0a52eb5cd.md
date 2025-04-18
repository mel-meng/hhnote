# swmm error: encountered during 2D initialization, please check diagnostics file

source: Innovyze support portal

---

### swmm error: encountered during 2D initialization, please check diagnostics file

source: [Innovyze support portal](https://innovyze.force.com/support/s/article/swmm-error-encountered-during-2D-initialization-please-check-diagnostics-file)

This article shows the troubleshooting steps when getting the following error.

![](images\1_293d0-8qynStBaDLBs5Kvw.png)

### Show the Diagnostics on the map

The diagnostics file is located under the modeling folder, the default location is,  
..\2D\log\[model\_name].mif  
   
If it is not loaded, right click on the “Diagnostics” item in the layer list to load the file.

![](images\1_1NxnpPPXbsS4CtUiCrZO-w.png)

By default, XPSWMM only shows the first 5 messages. To overwrite that, right click on the file, the choose properties.

![](images\1_w2X6naCQpfF0nsEGAXtqNA.png)

In the dialogue, switch to the data tab and make sure there are more items displayed than the number of items. You can turn off different type of messages to make it easier to locate them on the map.

![](images\1_w3M4PHrMnty2C6qQ-W85ow.png)

### Search for the error code

The error code can be found on the Tuflow website. Usually if you google “tuflow error xxxx”, it will take you to the official page of the error  
<https://wiki.tuflow.com/>

![](images\1_ZoweNjOmQnKmFjzZsT5LIg.png)

### Example

### Error 2061

An interface line needs to be connected to a node on both ends, as shown below, the left side of the interface line was digitized as two line segments instead of a continuous one. To fix this error, delete the left interface lines, and digitize a continuous one.

![](images\1_9hPUf16cUpcaPi4J4QbHeg.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 9, 2022](https://medium.com/p/6d0a52eb5cd).

[Canonical link](https://medium.com/@mel-meng-pe/swmm-error-encountered-during-2d-initialization-please-check-diagnostics-file-6d0a52eb5cd)

Exported from [Medium](https://medium.com) on March 18, 2025.