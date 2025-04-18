# How to model storage in XPSWMM

It is helpful to define ponding options before getting into the storage difference. When a node is flooding, the following options apply

---

### How to model storage in XPSWMM

It is helpful to define [ponding options](https://help.innovyze.com/display/xps/Hydraulics+Node+Data#HydraulicsNodeData-Ponding) before getting into the storage difference. When a node is flooding, the following options apply

* None: the overflow is lost when it is overflowing
* Allowed: a imaginary inverted cone is added to the top of the manhole and will allow the overflow to keep rising inside. Simulate depression around a manhole.
* Sealed: a imaginary cylinder the same as the top of the node is added to the top of the manhole and will allow the overflow to keep rising inside. Simulate bolted manhole or sealed manhole.

![](images\1_IszsgAaJbtClOFFwxEb00w.png)

When a storage is added to the spill crest, it behaves similar to the “allowed” ponding option, instead with a user provided storage curve. During flooding event, the water will keep rising in the storage, and if it goes above the user defined point, it will assume the area stays constant from the last point.

When storage is added at node Invert: this is the typical setup of a storage node, the node will be filled from the bottom until to the top and then start to overflow, then depending on the ponding setup, the overflow will be routed accordingly.

![](images\1_1XeynVbCGcI05PNMrfAMxQ.png)

A sample is created to illustrate the difference,

* Storage at spill: storage added at spill level with None ponding option
* Storage\_from\_invert\_XXX: storage set from invert with ponding option xxx

The model can be downloaded from [github](https://github.com/mel-meng/xpswmm/raw/master/models/howtos/storage/storage%20at%20spill%20crest%20vs%20from%20invert.zip).

### Storage at spill crest

![](images\1_11grW-k53trYlk0eE24-dw.png)![](images\1_DrsZbau5Tz1itkiqh1LXQg.png)![](images\1_UAWSrQrY5wPH2MNoxgM1xA.png)

### Storage from invert XXX

![](images\1_QR-VC0-3B9XFk_WAvyyC8Q.png)![](images\1_GNzzbqDEV01WZqaGwL2-yQ.png)![](images\1_GD36_fim8jXDuS4vR5tF1Q.png)![](images\1_m1rWdNvE6Fo9mp1k3Xmgbw.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [August 12, 2020](https://medium.com/p/d0c2233cee0).

[Canonical link](https://medium.com/@mel-meng-pe/how-to-model-storage-in-xpswmm-d0c2233cee0)

Exported from [Medium](https://medium.com) on March 18, 2025.