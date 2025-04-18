# Conveyance Curve for bridge openings

You can find the model and calculations on Github.

---

### Conveyance Curve for bridge openings

![](images\1_jlG3FHKI3jG890Qz-xLjAw.png)

You can find the model and calculations on [Github](https://github.com/mel-meng/xpswmm/tree/master/models/conveyance_curve).

For a bridge with two different openings, large and small which one will have higher water elevation?

Intuitively, we know when you have a smaller opening, the water level will be higher, so the water level will be higher in the small opening. But is that right?

The relationship between water depth and the flow through a cross section for open channel is called conveyance curve, and it is defined by the manning’s equation. In this case, the large and small opening are behaving pretty much the same when the flow is less than 3 ft. In other words, the flow depth will be the same when the same flow is going through the bridge. How can that be? Let’s take a closer look.

![](images\1_FZ0FnNqGsbViVg316j1wlQ.png)

Refer to the equations at the end of this article if you need to refresh you memory.

Q = 1/n\*A\*R(2/3)

R = A/WP

Q: conveyance

A: area

R: hydraulic radius

WP: wetted perimeter

In this example, since n and slope (S) are the same, for the same depth,

* The bigger the area, the higher the conveyance Q
* The bigger the hydraulic radius the higher the conveyance Q

For the area, it is very obvious which one is bigger for the same depth. However, it is not so obvious for hydraulic radius because it is calculated as area/wetted perimeter. When the wetted perimeter increases, it increases the friction, which will cause the water to flow slower, therefore to raise the water level to achieve the same Q.

So in summary, it is the interaction between friction and flow area.

Note: refer to this [article](https://medium.com/@mel.meng.pe/example-how-does-xpswmm-model-bridge-openings-d095334b551c) on how to extract conveyance curve from XPSWMM.

Let’s go through each parameters. It is obvious the large opening has more area for the same depth.

![](images\1_ApOCpCW-gMuW2Ql9oEhO_A.png)

For wetted perimeter, the small opening has huge advantage with the vertical walls, because the wetted perimeter barely increases as the depth increases, which means rise water rises, there is almost no added friction, so no slow down for the flow.

![](images\1_JCP65vliZhxOqr6zO4fCNw.png)

For hydraulic radius, it is very clear because of the advantage of the wetted perimeter for the vertical walls, the small opening has higher hydraulic radius once the level is within the vertical walls. It is also interesting to notice how the hydraulic radius dropped when reaching the bridge deck. Since the large opening has a much bigger area, its impact is more significant for small opening.

![](images\1_WEy5tfE5HlOgNpWlIv-2tQ.png)

Reference:

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 13, 2020](https://medium.com/p/8d01d566b344).

[Canonical link](https://medium.com/@mel-meng-pe/conveyance-curve-for-bridge-openings-8d01d566b344)

Exported from [Medium](https://medium.com) on March 18, 2025.