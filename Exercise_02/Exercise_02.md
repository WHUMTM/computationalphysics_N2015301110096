# 计算物理第二次作业

------

#作业要求
写一段代码使自己的名字能在屏幕上移动

------
#设计思考
一开始我想到能否将字符串转换成图片，然后生成个位置函数实现，但目前这个想法仍在探索中。之后在同学的帮助下，了解到了**os.system('cls')**可以实现清屏，于是完成了当前的比较简单的实现方式
> * 首先import **os**和 **time**两个包，以实现清屏和后面程序的延时
> * 下一步定义我要显示的内容即我的名字的list
> * 程序中假定向下移动10行，即刷新屏幕10次后结束
> * 当每一次显示过后，清屏，下一次再显示，A中的每一个字符都在最开始地方增加两个空格，同时在A整体的上方添加空行，即B，同时为了显示清楚在每一次清屏前设置1s延时

[点击查看源代码](https://github.com/WHUMTM/computationalphysics_N2015301110096/blob/master/Exercise_02/Exercise_02%20code.py)
##源代码

```python
import time
import os
A=["#     #   #######   #     #",
   "##   ##      #      ##   ##",
   "# # # #      #      # # # #",
   "#  #  #      #      #  #  #"]
B=("                           ")
for l in range(10):
      for n in range(4+l):
         print (A[n])
      time.sleep(1)
      i = os.system('cls')
      for k in range(4+l):
        A[k]='  '+A[k]
      A.insert(0,B)
```
