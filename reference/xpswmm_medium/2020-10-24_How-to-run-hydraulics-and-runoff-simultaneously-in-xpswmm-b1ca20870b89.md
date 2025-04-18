# How to run hydraulics and runoff simultaneously in xpswmm

Source: Innovyze Support Portal

---

### How to run hydraulics and runoff simultaneously in xpswmm

Source: [Innovyze Support Portal](https://innovyze.force.com/support/s/article/How-to-run-hydraulics-and-runoff-simultaneously-in-xpswmm)

For the majority of XPSWMM models, we should no longer use the interface files when generating runoff from rainfall and then route the flow through pipes. It was a feature that was used in the swmm3, swwm4 era when computer was not powerful enough (see [this article](https://innovyze.force.com/support/s/article/How-to-load-external-flow-from-interface-file-in-XPSWMM) for more details.). The support for interface files is mostly for backward compatibility, and should be avoided when updating an old model or setup new models.

Below are the procedures to remove interface files and run the runoff and hydraulics mode simultaneously.

### Step 1 Remove the references to interface files

![](images\1_ms6yiquUAdzkMixqnr97Mw.png)

### Step 2 Solve Runoff & Hydraulics Mode Simultaneously

![](images\1_iTKst9719MB2bkghKnZYJw.png)

### Step 3 Run both modes

![](images\1_g1n_MaYRd3SvmyfqHAgUGw.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 24, 2020](https://medium.com/p/b1ca20870b89).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-run-hydraulics-and-runoff-simultaneously-in-xpswmm-b1ca20870b89)

Exported from [Medium](https://medium.com) on March 18, 2025.