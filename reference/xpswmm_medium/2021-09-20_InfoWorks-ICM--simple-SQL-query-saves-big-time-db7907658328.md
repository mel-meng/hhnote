# InfoWorks ICM: simple SQL query saves big time

When it comes to customizing your modeling environment, sooner or later a modeler will need to write programs using computer languages…

---

### InfoWorks ICM: simple SQL query saves big time

When it comes to customizing your modeling environment, sooner or later a modeler will need to write programs using computer languages. Many modelers have the impression that such tasks are only for the technology inclined types. In this article, I hope I can change your mind, I’ll show you can start to build power tools with just a few lines of SQL, and it reads just like plain English.

### Switch upstream and downstream node IDs

The **reverse all selected links** tool works fine most of the time. However, some times, you only want to switch the IDs and not the inverts, how can you achieve that?

![](images\1_CKFkPISyjAC6Ekc1CGMPBg.png)

In this case, you can use a few lines of simple SQL statements.

1. create a new SQL query

![](images\1_mjMgx8B3oBdpm932-KTwZQ.png)

2. Type the following SQL statements, and you are done.

![](images\1_iEIDm1Z99Z0yUUL6DeMtbg.png)

As shown below, it reads just like English, a few more tipcs,

* words in upper case are keywords.
* SELECTED means the objects selected in the GeoPlan (map)
* $XXX are variables, which can be used to store temporary values
* //xxx is comments

```
//Switch US and DS node IDs
```

```
//store the node id to variables
```

```
UPDATE SELECTED SET $Usnode = us_node_id;
```

```
UPDATE SELECTED SET $Dsnode = ds_node_id;
```

```
//switch the node ids
```

```
UPDATE SELECTED SET us_node_id = $Dsnode;
```

```
UPDATE SELECTED SET ds_node_id = $Usnode;
```

```
//update the flags
```

```
UPDATE SELECTED SET us_node_id_flag = "Q";
```

```
UPDATE SELECTED SET ds_node_id_flag = "Q";
```

A few tips on figuring out the field names,

1. You can use the SQL window to get a list of the field names

![](images\1_axnt_8YTD4EW3aX8VcsvxQ.png)

2. Hover your cursor on the field in properties window

![](images\1_rUjMTMThXEbTEZ-Jr4s71w.png)

3. Hover your cursor on the header in a grid

![](images\1_03XZhvDqddfnY9759ZeDKw.png)

### Ask the user to enter the slope to calculate the invert

SQL can build very powerful calculator that asks the user for input. Some times, we have to update the values one pipe at a time, and a handy calculator can save us big time.

As shown below,

1. select the pipe that will need to update upstream invert using a slope entered, drag the query to the GeoPlan
2. enter the slop and hit OK

![](images\1_OYkG9IM0PNXPnkW-bZONRA.png)

Here is the query,

![](images\1_V85pZlZzl_LMPpPDTsm2mA.png)

A few more notes for this SQL query,

* LET $XXX will assign a value to a variable
* The two PROMPT lines will do the magic of showing a window for input, it is easy to figure out how to write this line.
* You can do simple math to calculate the new invert using the field names and variable

```
//Sets the upstream invert and slope of a link based on the entered slope, the downstream invert, and the length
```

```
//set default value
```

```
LET $gradient = 1;
```

```
//defines the input window
```

```
PROMPT LINE $gradient 'Pipe Slope';
```

```
PROMPT DISPLAY;
```

```
//calculate the upstream invert
```

```
UPDATE SELECTED SET us_invert = ds_invert +conduit_length*$gradient/100;
```

```
UPDATE SELECTED SET gradient = $gradient;
```

```
UPDATE SELECTED SET us_invert_flag = "Q";
```

```
UPDATE SELECTED SET gradient_flag = "Q";
```

I hope you are convinced now everyone can write SQL query in InfoWorks ICM that can save time.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [September 20, 2021](https://medium.com/p/db7907658328).

[Canonical link](https://medium.com/@mel-meng-pe/infoworks-icm-simple-sql-query-saves-big-time-db7907658328)

Exported from [Medium](https://medium.com) on March 18, 2025.