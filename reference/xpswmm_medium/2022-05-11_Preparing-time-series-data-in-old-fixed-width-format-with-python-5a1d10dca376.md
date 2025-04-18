# Preparing time series data in old fixed width format with python

source: Innovyze Support Portal

---

### Preparing time series data in old fixed width format with python

source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/Preparing-time-series-data-in-old-fixed-width-format-with-python)

When working with models sooner or later you’ll run into a project that you need to prepare data in a really old format from the 60s. And it asks you to prepare everything using a fixed width format.

Figuring our how many spaces you’ll need to pad your text, and how many decimal places you’ll need to fit your value in the column can be a great elementary math problem, but a poor one for Excel to solve easily.

The good news is that python is built for the task, it takes only one line to do the formatting for each column.

In this post, I’ll share a script that converts a table in excel into the “\*.his” format.

### Hydsys Format

The definition of the hydrograph text file is defined here:

[**Hydsys Hydrographs**  
*This window allows users to import HydSys Rainfall and Streamflow data. HYDSYS type Rainfall and Streamflow Data…*help.innovyze.com](https://help.innovyze.com/display/xprafts/Hydsys+Hydrographs "https://help.innovyze.com/display/xprafts/Hydsys+Hydrographs")

![](images\1_ShQaJe9wjoz3we2bQPwBmg.png)

As the example shown below,

![](images\1_TVRSFgvt7rmBrLLes8PQxA.png)

* first column is station “A8” means it is a text of 8 characters width, and we need to pad on the right side with spaces if the name is less than 8 letters long. Therefore we need to format it as “8CAM01\_\_ “ (\_ means it is a space).
* second column defines the type of the variable and it is a float number of 7 characters long, “\_140.00”, with 1 space to pad on the left, and the 140.00 means it is a hydrograph instead of rainfall
* the next few date columns are straightforward, just using this format, “YYYYMMDDHHMM”, “201309071140” is “2013 Sep 07 11:40”
* the last column is the value, it is a float number of 12 characters long

### Python script

As shown below, the heart of the python script is to implement the definition.

![](images\1_Uenka4jDLHvbQtFht_DNEg.png)

line 2: .ljust(8, ‘ ‘) will pad the station to 8 character with space on the right side

line 3: ‘140.00’.rjust(7, ‘ ‘) will pad to 7 character with space on the left side

line 4: x[datetime\_col].strftime(‘%Y%m%d%H%M’) will format the date to the required format

line 5: ‘{:12.5f}’.format(x[value\_col]) will format the float number with 12 characters long, and 5 decimal places

You can find the example on [Github](https://github.com/mel-meng/xpswmm/tree/master/hydsys).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 11, 2022](https://medium.com/p/5a1d10dca376).

[Canonical link](https://medium.com/@mel-meng-pe/preparing-time-series-data-in-old-fixed-width-format-with-python-5a1d10dca376)

Exported from [Medium](https://medium.com) on March 18, 2025.