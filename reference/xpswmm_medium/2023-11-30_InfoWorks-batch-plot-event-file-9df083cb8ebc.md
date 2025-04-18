# InfoWorks batch plot event file

Source: github

---

### InfoWorks batch plot event file

Source: [github](https://github.com/mel-meng/hhnote/tree/main/tools/icm)

### batch\_plot\_event\_file

For models with many nodes receiving inflows, or outfall nodes with boundary level conditions, it can get tedious reviewing the time series.

The “batch\_plot\_event\_file.ipynb” provides a quick way to batch plot each time series as a figure so that you can quickly check them.

To plot the figures,

1. export the event file as an “CSV” file

![](images\0_YMlcX_1HrSjpvk7w.png)

1. open the exported csv file and prepare it as a generic csv file. In the exported csv file, the time series data can be found at the end, row 11 is the header, and the following rows are the values. We need to replace the column header in row 11 with actual profile name listed in row 9 and 10,

(1)copy the profile names

(2)select the column header

(3)use paste special to transpose the profile names as column header

![](images\0_hhO_hg_R7g03rsXO.png)

2. delete the rows above the header, we’ll have a generic csv file.

![](images\0_-MRPiyYXKB8ERMoT.png)

3. run the notebook after updating the csv\_path to the generic csv file, and the folder for the folder,

![](images\0_v1kQOYXnDD5q5nXL.png)

4. each profile will have a figure saved in the figure folder

![](images\0_MbJ4m1FIyiNgT5JF.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [November 30, 2023](https://medium.com/p/9df083cb8ebc).

[Canonical link](https://medium.com/@mel-meng-pe/infoworks-batch-plot-event-file-9df083cb8ebc)

Exported from [Medium](https://medium.com) on March 18, 2025.