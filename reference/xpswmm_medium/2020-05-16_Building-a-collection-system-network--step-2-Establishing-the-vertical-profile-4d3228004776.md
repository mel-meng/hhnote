# Building a collection system network: step 2 Establishing the vertical profile

This is the third one in the series.

---

### Building a collection system network: step 2 Establishing the vertical profile

This is the third one in the [series](https://medium.com/@mel.meng.pe/building-a-collection-system-network-the-theory-f9422cb61ed5).

Once the connectivity is reviewed, I need to make sure the profile looks right. The profile should be nice and smooth. As shown below, it definitely doesn’t look right.

![](images\1_jm9l6jpYyTMn4oRH5XoKpw.png)

I need to correct manhole rim elevation, pipe inverts and pipe diameters.

In this example, unfortunately the client didn’t send us any rim and invert elevations. So we’ll have to make some assumptions,

* For manhole, we’ll use the elevation grabbed from the contour lines, that is the Z value we imported in the previous step.
* For pipes, we’ll assume a design slope recommended in 10 states standards and back calculate it from the outlet. Not ideal but a pretty good estimates for the first iteration of the model.

### Set manhole rim

I’ll show how to copy the Z value from the geometry table and paste it into the hydraulics table rim elevation. You can also use the GIS gateway to update the rim invert directly from the source GIS layer.

Open the geometry table where the Z values are stored.

![](images\1_5aKXiFsIaGLyaUMK44ETeA.png)

Also open the hydraulic table where the rim elevation column is.

![](images\1_oQZSoWFGY-xUu-_5J4UOqg.png)

Copy values from Z and paste into rim elevation column.

![](images\1_5heS9QqmZzC8CSt5njg8UA.png)

### Set pipe slope

Next we set the slope based on pipe diameter. Recommended pipe slope can be found in the [10 states standards](https://www.broward.org/WaterServices/Engineering/Documents/WWSTenStateStandardsWastewater.pdf).

![](images\1_7ae9BP3tom8jBG2LNBYbLQ.png)

I use Excel a lot when it comes to manipulating tables. After copying the diameter to excel, I used the **vlookup** function to populate the slope column. **Make sure the order of the ID are the same before pasting back to the model.**

![](images\1_nbERwRUUry_fhN6PhvLozQ.png)

We need to copy and paste slope back to the model, first I added slope column to the pipe info table.

![](images\1_cmrdSYVWYsVBdI32jxhnJQ.png)

Make sure it has enough decimal places.

![](images\1_zxQj75bNE4oI4tYKUy3nrw.png)

Then copy and paste it into the column.

![](images\1_WsyVU4vs3503cynt_HPC_w.png)

### Calculate pipe invert from slope

Before back calculate the inverts from the outlet, I need to Change the outlet manhole to outlet.

![](images\1_PAGA7I5HtnkWvnm_QTz8GA.png)

Then I can run the Pipe Invert Calculator,

![](images\1_ARx50egf4AYnILQh0VVq4w.png)

This tool will ask for an starting invert at the outlet, then it will go upstream one pipe at a time, and using the slope and length of the pipe to back calculate the missing inverts. To keep things simple, I used the setting below.

![](images\1_BYDZ0aHa9OZ_H_3Rd2CzQw.png)

I don’t like to add invert drops at manholes, for SWMM it can greatly increase the run time without changing the results too much. So I’ll keep the invert drop at 0.

If you would like to only calculate for selected pipes, use the facility tool to deactivate pipes you don’t want to update.

Now we have much better profile after the calculation.

![](images\1_nM94cPWVM88Mww2hEFF6CQ.png)

### Checking Profiles

The automated tools usually can get 90% of the job done, and I still need to check the results to make sure everything is calculated correctly. I like to check profiles in a more systematic matter. I’ll start from the trunk line, and then the branches. And I like to define major branches using the selection set, that way I can quickly check the profile if it will take many edits to get it corrected.

I use both the tracing tool and domain tools to easily create selection set.

![](images\1_FfTbjnah72rxRl7dasLckw.png)![](images\1_oNYkuHCRQrwk9iG9AApLSQ.png)

To view the profile, first clear the domain, then apply the selection set. After that when using the profile tool, instead of selecting any pipe, right click and choose “Add Domain to Selection”, then right click and click “enter”.

![](images\1_2lwMUi_1-m7Hd64qruqPJw.png)

In the next post, I’ll setup special structures. You can find other articles in this series below,

1. [Connecting the dots](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-1-connecting-the-dots-fa3b33b1bba8)
2. [Establishing the vertical profile](https://medium.com/@mel.meng.pe/building-a-collection-system-network-step-2-establishing-the-vertical-profile-4d3228004776)
3. Special structures such as pumps, etc
4. Interactively building a network

By [Mel Meng](https://medium.com/@mel-meng-pe) on [May 16, 2020](https://medium.com/p/4d3228004776).

[Canonical link](https://medium.com/@mel-meng-pe/building-a-collection-system-network-step-2-establishing-the-vertical-profile-4d3228004776)

Exported from [Medium](https://medium.com) on March 18, 2025.