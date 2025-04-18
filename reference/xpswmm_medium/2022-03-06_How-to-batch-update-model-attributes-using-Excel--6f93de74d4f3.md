# How to batch update model attributes using Excel?

support: Innovyze support portal

---

### How to batch update model attributes using Excel?

support: [Innovyze support portal](https://innovyze.force.com/support/s/article/How-to-batch-update-model-attributes-using-Excel)

When building a model, Excel is often used to update the model from external data sources. Learning a few Excel tricks can greatly improve your productivity.

The most common workflow looks like this,

* You received some updates to the model as a GIS layer or a table.
* Find these elements in the model to be updated.
* Then update the attributes with the new values.

You can do it one attribute a time in the model by manually copying the value from the external source. Or you can use the built-in import tool from the modeling software to update the results in batch.

#### Measure twice, cut once

What I found works best in most situation is to use Excel as the main tool, to interactively copy and paste the values from the Excel table to the model table. The major benefits of this approach is that it is a more visual and interactive process, I have more opportunities to identify errors and therefore feel more confident about the final results. This is a step you don’t want to go fast.

### The Excel Approach

This approach centers around Excel as the place where most of the actions happen.

* create a list of elements to be updated in the Model
* rebuild the list in Excel with before and after values
* review the updates
* copy and paste the new values back to the model

#### Build a list

In XPSWMM, you can build a full list of model elements using the XPTables.

![](images\1_zlrVky-FZiPpvUfojeYvdQ.png)![](images\1_SVACFyyijR3gPKa_3doqzQ.png)

Once a table is created, we can copy the whole table from XPSWMM to Excel.

![](images\1_SznZRSvaq4z-_ZXo3-mqYw.png)

#### Compare before vs after

Once the model data is in Excel, we can match the model element to the external data using the [**vlookup**](https://www.youtube.com/watch?v=d3BYVQ6xIE4) function. If you are not an expert of this function yet, become one.

For example, we need to update the diameter from an external table. However, I don’t want to replace all the values from the new source, I want to review the data and only update the ones that looks correct.

![](images\1_Db_QVo0RxBaxffyFtcgkOQ.png)

In Excel, we have two tabs. The idea is to put the old and new values side by side so that I can review them first. Then I’ll only pick the ones that I would like to update and update the values in the model.

![](images\1_fp4ynM4dmMjve-5AYJd4RQ.png)

To do this, I created a new tab,

* the first column and the 2nd column were copied from the model table
* the 3rd and 4th columns were values extracted from the external data table

![](images\1_GWbXHMrf2fGCw0F8MzoCnA.png)![](images\1_hQ13hGhaZSDTT-6NmJkZHg.png)

#### Copy and paste

The last step is to paste the updated values back to the model. To avoid introducing errors, we would like to keep the changes to only the records with changes. And this will require filtering the elements in the model before pasting the values.

A commonly used trick is to use a “temporary” field such as “description” or “notes” in XPSWMM to mark the elements that need to be changed first in the table of all elements, and then apply a filter of the “temp” field.

As shown below, we added “description” field to the XPTable.

![](images\1_7yBSaUYJcWsbmJY3WOdgNA.png)

Then we copied the action column from Excel to XPSWMM.

![](images\1_ZucPuqqDopn066XCmJjoAQ.png)

To filter the record,

1. select the description column
2. sort it
3. select the rows with “update”
4. select the objects in the map
5. filter only the rows selected

![](images\1__MMFs_xKCx9nUEr9E2520w.png)

Now, with this new table, we can apply the same technique to create a new tab in Excel to get the new diameters for only the rows that need to be updated.

![](images\1_ePzkbkmw12ok2Ee_XPpM2Q.png)

#### Other common issues

When matching the data, there are a few common issues.

* Excel might automatically format data. 3–14 for mar-14, 1235–1235.0, etc. In such situations, you need to convert the value to a text with the correct format so that vlookup can correctly match the record. See this [link](https://support.microsoft.com/en-us/office/stop-automatically-changing-numbers-to-dates-452bd2db-cc96-47d1-81e4-72cec11c4ed8) for some tips.
* Date can be tricky to handle in Excel. Use custom format for better control.

![](images\1_1YRgX4e-09pFPQwYUSyiYg.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [March 6, 2022](https://medium.com/p/6f93de74d4f3).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-batch-update-model-attributes-using-excel-6f93de74d4f3)

Exported from [Medium](https://medium.com) on March 18, 2025.