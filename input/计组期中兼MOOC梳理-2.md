---
title: 计组期中兼MOOC梳理-2
date: 2024-04-01 14:44:45
tags: 计组
---
![还原机器代码-1](../img/计组/还原机器代码-1.png)
![还原机器代码-2](../img/计组/还原机器代码-2.jpg)
前面都没问题，注意一下beq那行（一般beq都是while循环），而且后面一般跟label
>虽然偏移量是1，不过实际上读的是下下一条指令（毕竟没有偏移的话就直接读下一条了（很重要！！

D触发器：主要有一个数据输入、一个数据输出和一个时钟输入。在时钟clock的上升沿（0→1）， 采样输入D的值，传送到输出Q， 其余时间输出Q的值不变

![2016期中-一位全加器](../img/计组/一位全加器.png)
为什么与S连的都是或非门？（A,B两个输入先或非一下，然后再和进位的输入或非），因为S只是某一位的取值（类比个位 只需关注奇偶）又加上二进制只有10两个数字，所以看一下一不一样就行

为什么Cout先连与门再连或门？AB两个输入先与一下，如果全是1那就构成进位条件。如果AB不全是一呢？没关系AB只要有一个是1就可以了（异或为1），并且如果输入的进位也是1的话也可以构成进位条件，两者满足其一就可以
![进位输出信号分析](../img/计组/输出信号i+1.png)
可以推一下i=1的时候的公式
![2016期中-进位信号公式i+1推导](../img/计组/进位信号公式i+1推导.jpg)
以上都是行波进位加法器。

如果是超前进位加法器：
![超前计算进位信号（三级门延迟）](../img/计组/超前计算进位信号（三级门延迟）.png)
他主要优化的点在于C2的值不需要依赖C1，节省了等待时间（全都是并行计算的），一个竖列的全都是同时算出来，总共三个数列，所以计算Ci的延迟时间固定位三级门延迟

但是总的一整个超前进位加法器是四级门延迟的。那是因为S3的计算依赖于C3，而计算C3需要三级门延迟。所以计算出S3需要四级门延迟（关键路径
![超前进位加法器](../img/计组/超前进位加法器.png)

![2016期中-与门](../img/计组/2016期中-与门.png)
非门记忆：让positive的人在上面，本negative人只想当一个阴暗爬行的接地鼠鼠
![2017期中-或门（画的是或非门）](../img/计组/2017期中-或门.png)
![2016期中-计算n位行波进位加法器门延迟数](../img/计组/算门延迟数.png)
