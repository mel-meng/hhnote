# How to check diagnostics file in XPSWMM

source: Innovyze support portal

---

### How to check diagnostics file in XPSWMM

source: [Innovyze support portal](https://innovyze.force.com/support/s/article/swmm-error-encountered-during-2D-initialization-please-check-diagnostics-file)

How to check the diagnostics file when you see this error **swmm error: encountered during 2D initialization, please check diagnostics file.**

![](images\1_QCDFdYsVkWx-y2-cNXzUug.png)

When running a 2D model, the XP2D engine will write error messages into a a MapInfo GIS file reporting diagnostic information. By default, the information is saved in the folder: ..\2D\log\[model\_name].mif

Usually the diagnostic file will be automatically loaded into the UI, however, if it is not showing, you can manually add the file.

![](images\1_iZMdr15ko6cFAlIKLRXScQ.png)

By default, XPSWMM only shows the first 5 messages. To overwrite that, right click on the file,

![](images\1_BD40vUQnVS07XN4CCqfHLA.png)

In the dialogue, switch to the data tab and make sure there are more items displayed than the number of items. You can turn off different type of messages to make it easier to locate them on the map.

2. the total number of entries in the diagnostic file

3. increase the number of entries to match the number in (2) so that all entries are display in the map. You might want to turn off Warning messages, etc to only focus on the errors and unstable messages.

![](images\1_NigTZL17QMZ3ZA2oARa05A.png)

The error code can be found on the Tuflow website. If you google “tuflow error xxxx”, it will take you to the official page of the error  
<https://wiki.tuflow.com/>

![](images\1_DdSjDWqGVSzlKLRMkeLuDw.png)

For example, error 2061 is a common error. When drawing interface lines around a 1D river, an interface line needs to be connected to a node on both ends, as shown below, the left side of the interface line was digitized as two line segments instead of a continuous one. To fix this error, delete the left interface lines, and digitize a continuous one.

![](images\1_aVhYAH31oBmjms7mIi-LMw.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [December 15, 2021](https://medium.com/p/7c3d74b1897b).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-check-diagnostics-file-in-xpswmm-7c3d74b1897b)

Exported from [Medium](https://medium.com) on March 18, 2025.