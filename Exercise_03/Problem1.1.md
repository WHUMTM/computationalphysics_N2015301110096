# 第一章习题(续)
标签： 计算物理作业

------

[toc]

[^1]: **Euler method**的描述来自[en.Wikipedia](https://en.wikipedia.org/wiki/Euler_method).

[^2]: **matplotlib**源代码来自[matplotlib.org](https://matplotlib.org/gallery.html).
----------

##完成度
 - [x] 阅读`problem1.4`，完成算法设计，编程逻辑（即`Preudocode`）
 - [x] 通过`spyder`或`ipython`，编辑本项目code，运行并查错
 - [x] 通过`matplotlib`编辑画图部分code，运行并差错
 - [ ] 优化代码和画图程序（持续完成中）
 - [x] 编辑代码注释并制作本项目报告


----------


##摘要



本次作业选取`problem 1.4 a radioactive decay problem`作为习题题目，了解用**Euler method**解决常微分方程的方法，同时尝试用**python**解决简单的物理问题,本项目与上一个解决`problem1.1`的题目相类似。


----------


##背景
>Consider a radioactive decay problem involving two types of nuclei, *A* and *B*, with populations *N<sub>A</sub>(t)* and *N<sub>B</sub>(t)*. Suppose that type *A* nuclei decay to form type *B* nuclei, which then also decay, according to the differential equations
$$\begin{align}
    \frac {dN_A}{dt}& = - \frac{N_A}{\tau_A}  && \tag 1\\
   \frac{dN_B}{dt} & = \frac{N_A}{\tau_A}-\frac{N_B}{\tau_B} &&  \tag 2\\
\end{align}$$ 
where $\tau_A$ and $\tau_B$ are the decay time constants for each type of nucleus.

----------
##主要内容
###1、计算方法与计算工具简介
 - **Euler method**是一种简单有效的数值计算方法，可以用来给定初始值的常微分方程（ODEs）。数学上，这种方法是通过对变量函数进行`First-order Taylor expansion`，实现数值上的近似计算[^1]。
 - 在**python**中，**Euler method**可通过定义`array`和`for-loop`语句实现，同时代码简洁明了。
 - **matplotlib**是用于**python**中一个优秀的作图包，可以用于将计算数据生成直观的图像，并且官网上提供生成美观图像的`source code`，可使作图成本大大降低[^2]。
 - 本文由**cmd markdown**编辑。

###2、计算方法与目的
- 方程$(1)$ $(2)$可采用分离变量法求解次常微分方程
-  利用**Euler method**作数值近似时，方程$(1)$化为
$$\begin{align}
    N_A(t+dt)& = N_A(t) - \frac{N_A}{\tau_A}dt && \tag 3\\
   N_B(t+dt) & = N_B(t) + (\frac{N_A}{\tau_A}-\frac{N_B}{\tau_B})dt &&  \tag 4\\
\end{align}$$ 
与`problem1.1`不同的是本题中解析结果中`High-order Taylor expansion`不可忽略，即`Euler method`的截断误差不可忽略，从下面分析可以看到本计算方法只有在**time_interval (`dt`)**极其小，可近似于0的时候，`Euler method`可以得到很好的近似，与解析结果基本相同；但当`dt`偏大时，本方法与真实结果有较大的偏差。
为了方便计算和说明，我们采取`Problem 1.5`的初始条件，即：
>Consider different intial conditions, such as $N_A = 100$, $N_B = 0$, etc, and take $\tau=1s$.


   但具体操作上，我将取固定值$\tau_A=1$， **initial number of nuclei B** : $N_B(0)$也设计成变量，同时按照题目要求改变`final_time`， `time_interval`: $dt$， `decay time constant for  nuclei B` : $\tau_B$探究本题目
- 在python上编码流程如下：
    - 定义`array`，定义各参量名称，给常量赋值，本方程中$g$为常量，同时我设置运行时间`end_time = 10`.
    - 利用`for-loop`语句，将运行时间内全部数值加入到定义的array.
    - 利用`matplotlib`包画图，并美化图像.
    - 对比方程解析解，考察数据可靠性和误差.
    - 运行程序，修改bug，优化命名规则，优化结构.

###3、程序源代码与计算
- 可以由数学上解出，方程$(1)(2)$的解析解为
$$\begin{align}
  N_A(t) & =N_A(0)*e^{-t} && \tag 5\\
  N_B(t) & =\frac{\tau_B*N_A(0)*e^{-t}}{\tau_A-\tau_B}+\frac{N_B(0)-\tau_B*N_A(0)}{\tau_A-\tau_B}*e^{\frac{-t}{\tau_B}} &&  \tag 6\\
\end{align}$$ 
- 如需查看源代码  [请点击这里](https://github.com/WHUMTM/computationalphysics_N2015301110096/blob/master/Exercise_03/Problem1.4-code.py)

###4、运行结果与分析
####探究 **$dt$** 对结果可靠性的影响
- 此时不妨按`Problem 1.5`示例的初始数值，取$\tau_B=0.5$， $N_B(0)=0$，   $final$ $time=10$
  当**$dt=0.01s$**时，结果如下
![图1](https://raw.githubusercontent.com/WHUMTM/computationalphysics_N2015301110096/master/Exercise_03/0%2C0.5%2C0.01%2C10.png)
  当**$dt=0.1s$**时，结果如下
![图2](https://raw.githubusercontent.com/WHUMTM/computationalphysics_N2015301110096/master/Exercise_03/0%2C0.5%2C0.1%2C10.png)
  当**$dt=0.5s$**时，结果如下
![图3](https://raw.githubusercontent.com/WHUMTM/computationalphysics_N2015301110096/master/Exercise_03/0%2C0.5%2C0.5%2C10.png)
####对曲线本身的探究
- 此时不妨取误差最小的$dt=0.01s$，$final$ $time=10$
  当$N_B(0)=0$， $\tau_B=0.5$ 时，结果如下（与之前相同）
![图4](https://raw.githubusercontent.com/WHUMTM/computationalphysics_N2015301110096/master/Exercise_03/0%2C0.5%2C0.01%2C10.png)
  当$N_B(0)=50$， $\tau_B=0.5$ 时，结果如下
![图5](https://raw.githubusercontent.com/WHUMTM/computationalphysics_N2015301110096/master/Exercise_03/50%2C0.5%2C0.01%2C10.png)
  当$N_B(0)=100$， $\tau_B=0.7$ 时，结果如下
![图6](https://raw.githubusercontent.com/WHUMTM/computationalphysics_N2015301110096/master/Exercise_03/100%2C0.7%2C0.01%2C10.png)





----------


##结论
- `python`是一个语法简洁明了且非常适合做物理计算的一种计算机语言.
- 由第一个探究可以发现，与`Problrm1.1`不同，本题中必须取$dt$ 是一个极小值，否则随着$dt$ 的增大，其越来越不可近似为0，使用`Euler method`做近似的解曲线与解析解曲线差距越大，即误差越大，原因是其解析解并不是一次函数.
- 由第二个探究可以发现，衰变过程中的粒子数目曲线是一个指数曲线，
  当初始时刻$\frac{N_A}{\tau_A}-\frac{N_B}{\tau_B}<0$ 时，初始时刻$N_B$的曲线斜率为正，之后曲线先增后减.
  当初始时刻$\frac{N_A}{\tau_A}-\frac{N_B}{\tau_B}=0$ （即$N_B(0)=50$， $\tau_B=0.5$）时，初始时刻$N_B$的曲线斜率为0,之后曲线单调下降.
  当初始时刻$\frac{N_A}{\tau_A}-\frac{N_B}{\tau_B}<0$ 时，初始时刻$N_B$的曲线斜率为负，之后曲线单调下降.


----------


##参考文献与鸣谢
[1]: 画图部分程序，参考[matplotlib source code](https://matplotlib.org/examples/lines_bars_and_markers/line_demo_dash_control.html). 
[2]: 算法部分参考 "Computational Physics" by Nicholas J. Giordano & Hisao Nakanishi.

