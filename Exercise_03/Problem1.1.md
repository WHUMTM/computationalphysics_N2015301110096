# 第一章习题

------

[toc]


----------


##摘要



本次作业选取`problem 1.1 a freely falling object`作为习题题目，了解用**Euler method**解决常微分方程的方法，同时尝试用**python**解决简单的物理问题


----------


##背景
>The velocity of a freely near Earth's surface is described by the equation 
$$\frac{dv}{dt}=-g \tag{1}$$ 
where $v$ is the velocity and $g=9.8$ $m/s^2$ is the acceleration due to gravity. Write a program that employs the Euler method to compute the solution to $(1)$.


----------
##主要内容
###1、计算方法与计算工具简介
 - **Euler method**是一种简单有效的数值计算方法，可以用来给定初始值的常微分方程（ODEs）。数学上，这种方法是通过对变量函数进行`First-order Taylor expansion`，实现数值上的近似计算[^1]。
 - 在**python**中，**Euler method**可通过定义`array`和`for-loop`语句实现，同时代码简洁明了。
 - **matplotlib**是用于**python**中一个优秀的作图包，可以用于将计算数据生成直观的图像，并且官网上提供生成美观图像的`source code`，可使作图成本大大降低[^2]。
 - 本文由**cmd markdown**编辑。

###2、计算方法与目的
- 方程$(1)$本身并不复杂，可采用分离变量法求解次常微分方程
-  利用**Euler method**作数值近似时，方程$(1)$化为
$$v(t+dt)=v(t)-gdt \tag{2}$$
在本例中dt取值与最后计算数据的准确度没有任何关系，即此问题，利用**Euler method**做数值计算与解析解完全相等。题目中指出
>For simplicity, assume that the initial velocity is zero—that is, the object starts from rest—and calculate the solution for times $t=0$ to $t=10s$.


   但具体操作上，我尝试将**initial velocity** $v(0)$也设计成变量，同时按照题目要求改变$dt$探究本题目
- 在python上编码流程如下：
    - 定义`array`，定义各参量名称，给常量赋值，本方程中$g$为常量，同时我设置运行时间`end_time = 10`.
    - 利用`for-loop`语句，将运行时间内全部数值加入到定义的array.
    - 利用`matplotlib`包画图，并美化图像.
    - 对比方程解析解，考察数据可靠性和误差.
    - 运行程序，修改bug，优化命名规则，优化结构.

###3、程序源代码与计算
- 可以由数学上解出，方程$(1)$的解析解为
$$v(t)=v(0)-gt\tag{3}$$
是一个斜率为$-g$的一次方程
- 如需查看源代码  [请点击这里](https://github.com/WHUMTM/computationalphysics_N2015301110096/blob/master/Exercise_03/Exercise_03-code.py)

###4、运行结果与分析

##结论

##参考文献与鸣谢
[^1]: **Euler method**的描述来自[en.Wikipedia](https://en.wikipedia.org/wiki/Euler_method).
[^2]: **matplotlib**源代码来自[matplotlib.org](https://matplotlib.org/gallery.html).
