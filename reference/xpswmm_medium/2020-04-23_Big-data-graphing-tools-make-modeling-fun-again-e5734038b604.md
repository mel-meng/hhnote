# Big data graphing tools make modeling fun again

Creating awesome interactive charts no longer just for programmers

---

### Big data graphing tools make modeling fun

As a planning engineer, I spent way too much time following big data and AI news. Fascinated by recent advancements in technology, I spent lots hours coding scripts that can generate clever analysis and cool charts, and I enjoyed every minuet of it. However, I always knew it was just an occupational hobby. To make the code I programmed to become useful even just for a few people for one year will require a huge amount of time. I’ve done that a few times, and it was definitely not that much of fun.

That starts to change a few years ago, when I started using [Jupyter](https://jupyter.org/) notebooks, and digging deep into [pandas](https://pandas.pydata.org/) for time series and general tabular data analysis. Doing data analysis and creating graphs with these tools no longer feel like writing software, once I got used to the tools, I am simply typing my thoughts into the notebook, and with a click of a button, I can watch my idea materialize on the screen in front of me. That feeling is really fun!

The only thing I feel was missing at that time was interactive charts. All the charts I generated were just pictures, if I want to zoom in, I’ll have to type another line of code. That’s when I started to follow [plot.ly](https://plotly.com/), and I wished that I could learn Javascript really well to program these cool interactive charts. Then I got busy with other things and forgot about it until last week.

So throughout last week, I got into not one but several conversations with different people about calibration, and that reminded me not being able to visualize calibration results easily is probably the main reason most projects ended up without proper calibration report. As a result, I started to dig my old memories and code repositories, in hope to find some clues if there is a cure for that. Then to my surprise, I realized my wish was granted, now I can have interactive charts within Jupyter notebook using just python. This is made possible using the awesome [Plotly Python Libary](https://plotly.com/python/).

Now I can make graphs that you might think from a new startup with just a few lines of code. Something I never thought would be possible just a few years ago.

If you are a modeler who also enjoys writing a line or two of code. I think you might reach the same conclusion, this is the best tool for time series analysis ever made available to us modelers. See for yourself and let me know what you think.

![](images\1_dMuYNyEcv50Y_E3zIxwbFA.png)

A fully interactive web flow data graph

All it takes is 5 lines of code. In the first 4 lines, I loaded the time series from two \*.tsf files. And the last line plots the interactive figure.

![](images\1_BSjhk4WRcYpBm_SsOorKlQ.png)

Another commonly used plot is scatter plot, you can zoom in/out to investigate the data. With the histogram turned on, we have much better idea of the data quality.

![](images\1_qiVlst1wmS8KImToKAIAng.png)

Scatter Plot you can zoom in with histogram updates

Just to lightly touch the analysis side, I performed DWF (Dry weather flow) analysis to see if there is a strong diurnal pattern in the flow data. Using the facet wrap scatter plot, I can make very useful plots using just one line.

![](images\1_FrhBHHTvoX6ddwh56TQ1Ng.png)

Compare DWF by Day of the Week, and color by week number

![](images\1_DVbA_aGc2BcFswPhcJG_Qg.png)

Compare DWF by day of week

You can find the data and source notebook on [Github](https://github.com/mel-meng/sewerplot/tree/master/notebooks).

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 23, 2020](https://medium.com/p/e5734038b604).

[Canonical link](https://medium.com/@mel-meng-pe/big-data-brings-advanced-graphing-tools-to-everyone-e5734038b604)

Exported from [Medium](https://medium.com) on March 18, 2025.