# InfoWorks Timestep\_log\_file\_reader

source: github

---

### InfoWorks Timestep\_log\_file\_reader

source: [github](https://github.com/mel-meng/hhnote/tree/main/tools/icm)

The timestep log is very useful When debugging an InfoWorks ICM model, however, the log file usually will have thousands of lines and extracting the useful information can be a challenge.

The “timestep\_log\_file\_reader.ipynb” can extract the count tables showing the nodes and links with trouble in calculation into an Excel spreadsheet.

Here are a few example tabs,

* 93-Unconverged link depth
* 98-Unconverged nodes coun
* 1084-Link depth fail coun

The tab name starts with the line no, then the name of that table.

![](images\0_9yu3VFjLkiISNbor.png)

The first few tables are for initializations, and the following tables are for the simulation.

To use this tool,

* step 1 turn on timestep log in the RUN

![](images\0_o_Yw8m7CsxVTRMrI.png)

* step 2 run the simulation
* step 3 export the log to a file

![](images\0_N2l34sRpZ5t2Mq8c.png)![](images\0_R2SYe6IHH05HbFVP.png)![](images\0_EgILDgas5QjyvSrA.png)

* step 4 set up the log path, and the excel\_path in the notebook and run the cell

![](images\0_mjrA5rfnlqLEaC-B.png)

You will have a spreadsheet with all the count tables, and ordered by the count.

![](images\0_gyD2Cps5TTVkoSVt.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [November 29, 2023](https://medium.com/p/f633c5147257).

[Canonical link](https://medium.com/@mel-meng-pe/infoworks-timestep-log-file-reader-f633c5147257)

Exported from [Medium](https://medium.com) on March 18, 2025.