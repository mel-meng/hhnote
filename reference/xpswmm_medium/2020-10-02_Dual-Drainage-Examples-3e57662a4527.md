# Dual Drainage Examples

In this article we will use a few examples to understand how dual drainage work.

---

## Dual Drainage Examples

In this article we will use a few examples to understand how dual drainage work.

You can find the model on [GitHub](https://github.com/mel-meng/xpswmm/tree/master/models/dual_drainage).

A simple dual drainage model,

* A constant 3% slope stretch of street with sewer pipe underneath, the street is 20ft wide and 1ft tall, the sewer pipe is 1.5ft in diameter

![](images\1_TDkz1H8DchR0rDXs13zk_A.png)

## Base Scenario: No inlets with 15cfs constant flow at upstream node (N1)

Without inlets, ,

* Flow will fill in N1 and start to flow in the sewer pipe down stream
* Since there is no surcharge, the flow never reached the street level

Apparently, this is not the desired behavior of a dual drainage system.

![](images\1_atsKwUwJCxZ8Dl2kBjXEsg.png)

## Scenario 15cfs with inlet 3cfs max flow

In this scenario,

* 15cfs is loaded at N1
* All the inlets have an max. capture of 3cfs
* For N1, 3cfs goes into the sewer pipe, and 12 cfs goes down the street
* At N2, another 3cfs goes into the sewer pipe, and 9 cfs goes down the street, etc.

![](images\1_qrMnFgM6gyoXeOMsgZEeQw.png)

The final results are shown below. Each time an inlet is passed, 3cfs is transferred from the street to the sewer pipe.  
   
Note: ##.1 is the sewer pipe, ##.2 is the street, link 31->32..->36  
   
Flow in the dual drainage system (cfs)

![](images\1_KVeQ35ExF4bBDOzVp1K6Hw.png)![](images\1_t2zDwdcwjGvfqaEmxfnhsQ.png)

By [Mel Meng](https://medium.com/@mel-meng-pe) on [October 2, 2020](https://medium.com/p/3e57662a4527).

[Canonical link](https://medium.com/@mel-meng-pe/dual-drainage-examples-3e57662a4527)

Exported from [Medium](https://medium.com) on March 18, 2025.