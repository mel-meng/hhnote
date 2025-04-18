# What is live modeling?

LIVE modeling is based on the idea that we can look into the future based on what we know now, and the tricky part of that is “now” is not…

---

### What is live modeling?

LIVE modeling is based on the idea that we can look into the future based on what we know now, and the tricky part of that is “now” is not a fixed point, it is changing every second, therefore, what we know now is a concept that is highly sensitive to its context.

Here is an analogy. Say you are on a camping trip with poor internet connection, while there was also an important football game you would rather watching at the time. So intermittently, you’ll get messages from your Facebook feeds and messages from your friends about the game. And the order they come in because of the poor internet connection, are not in order. So it is your job to sort through all these information about an ongoing game to figure out what actually happened.

Similar to observe a live event by only following Twitter in real-time, ICMLive has a systematic way to sort through the live stream and identify the best data sources for the next forecast.

The goal of the ICMLive simulation is to forecast the future based on best available information at the moment. So the most important thing is to figure out what is the best information at any moment.

As shown below, the forecast is done as a series chained simulation, say every hour a forecast is made. We have two types of input data for a live simulation, forecast TSDB (time series database), e.g. rainfall forecast. And observed TSDB, such as radar rainfall.

![](images\1_qmFMUWrWbGyTUwtzlKyE8w.png)

So at time 0,we know the initial state (e.g. boundary condition level, soil moisture, etc.).

At hour 1, say it is origin 1, at that moment, we have the observed data such as rainfall until origin 1, with the initial state and the observed rainfall we can run the model to the current time. By the end of the run, we have much better idea on the state of the system at origin 1, and what happened in the past hour. This is called hindcast, using observed data to run the simulation to learn what happened in the past.

At the same time of hour 1, we also have the forecast into the future 3 or 4 hours. So we can look into the future using the latest available forecast and the new state we just got. This is called a forecast, looking into the future.

Then we simply repeat this process, at each hour, we figure out the best model state, best observed data, and forecast data available to us, run the hindcast to move the model state forward, then run the forecast from the latest state to look into the future.

The key to this operation is the time series database, which monitors the live stream data into the database by applying time stamps when they come in, with the time stamps, ICMLive can figure out what is the latest information. The same way how you tell which message or twitter is the latest.

A huge part of the ICMLive system resolves around this operation, and an understanding of these concepts can be very helpful when setting up and operating a LIVE system.

By [Mel Meng](https://medium.com/@mel-meng-pe) on [April 26, 2021](https://medium.com/p/e385c7e0b1ac).

[Canonical link](https://medium.com/@mel-meng-pe/what-is-live-modeling-e385c7e0b1ac)

Exported from [Medium](https://medium.com) on March 18, 2025.