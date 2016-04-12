#pi的计算
from random import random
from math import sqrt
from time import clock
darts = 1000 #总点数
hits = 0 #在1/4圆内的点数
clock()
for i in range(1,darts+1):
    x,y = random(),random() #随机得到从0到1间的一个值
    dist = sqrt(x**2 + y**2) #得到点到原点的距离，判断是否在圆内
    if dist <=1.0:
        hits = hits + 1
#四分之一的圆面积为1/4*pi*r^2,r=1,对应的正方形面积为1，它们面积之比为1/4*pi*r^2:1 = hits:darts
pi = 4 * (hits/darts)
print("Pi值是 %s" %pi)
print("程序运行时间是 %-5.5ss" %clock()) #clock()是运行的时间
