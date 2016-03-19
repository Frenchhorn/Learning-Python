#grahics库

from graphics import *

#GraphWin类
win = GraphWin('标题', 450, 450)
直接创建一个图形窗口，默认为200*200
默认标题为Graphics Window,有最小化和关闭按钮。
点(0,0)表示屏幕左上角
X轴正方向为从左往右
Y轴正方向为从上到下
#方法：
win.getMouse()    等待鼠标点击，返回一个Point对象，其坐标值为点击时的坐标值
win.close()       关闭窗口win
win.setCoords(x1,y1,x2,y2)   重新设置坐标轴，左下为(x1,y1),右上为(x2,y2)
#用setCoords后，所有坐标就会以其为标准，如move()等。

#Ponit类
a = Point(x, y)
x为横坐标，y为纵坐标
#方法：
a.getX()       返回点a的x轴坐标值
a.getY()       返回点a的y轴坐标值
a.clone()      复制对象a
继承自GraphicsObject()类的方法
a.draw(graphwin)   在graphwin上显示点a，在已有的点上重复显示，则会报错。
a.move(dx, dy)     移动点a的x,y轴坐标
a.setFill(color)   改变内部的颜色(改变点的颜色)
a.setOutline(color)  改变线的颜色(改变点的颜色)
b.undraw()         使点a在graphwin上消失,重复操作不会报错。


#Circle类
a = Circle(center, radius)
center为圆心，需要时Point对象
radius为半径
#方法：
a.clone()
a.getRadius()  返回圆的半径（整型或浮点型）
a.getCenter()  返回圆心坐标的一个Point对象
a.getP1()      返回Ponit对象,坐标为(x-r,y-r)
a.getP2()      返回Ponit对象,坐标为(x+r,y+r)
继承自GraphicsObject()类的方法
a.draw(graphwin)   在graphwin上显示圆a
a.move(dx, dy)     移动圆a的x,y轴坐标
a.setFill(color)   改变内部的颜色
a.setOutline(color)  改变线的颜色
b.undraw()         使圆a在graphwin上消失

#Line类
a = Line(p1, p2)
点p1到点p2的线
#方法：
a.clone()
a.setArrow(option)
a.getCenter()  返回中点坐标的一个Point对象
a.getP1()      返回Ponit对象,p1
a.getP2()      返回Ponit对象,p2
继承自GraphicsObject()类的方法
a.draw(graphwin)   在graphwin上显示线a
a.move(dx, dy)     移动线a的整体的x,y轴坐标值
a.setFill(color)   改变内部的颜色
a.setOutline(color)  改变线的颜色
b.undraw()         使线a在graphwin上消失


#Image类

#Entry类
内容可以被用户修改的文本框
Entry(p, width)
#方法：
clone() 
getAnchor()         返回p对象
getText()           返回text字符串
setFace(face)       设置字体，有['helvetica','arial','courier','times roman']
setFill(color)      设置内部颜色
setSize(size)       设置字体大小
setStyle(style)     设置字体格式，有['bold','normal','italic', 'bold italic']
setText(text)       设置text
setTextColor(color) 设置text颜色
#继承自GraphicsObject
draw(win)
move(dx, dy)
setFill(color)
setOutline(color)
setWidth(width)
undraw()

#GraphicsError类

#GraphicsOject类

#Oval类

#Polygon类
绘制多边形
p = Polygon(p1,p2,p3,p4...)
按p1,p2,p3,p4的顺序连接各点
#方法：
a.draw(graphwin)   在graphwin上显示线a
a.setFill(color)   改变内部的颜色
a.setOutline(color)  改变线的颜色

#Rectangle类
Rectangle(p1, p2)
画矩形

#Text类
text01 = Text(p, text)
绘制文字
#方法：
clone() 
getAnchor()         返回p对象
getText()           返回text字符串
setFace(face)       设置字体，有['helvetica','arial','courier','times roman']
setSize(size)       设置字体大小
setStyle(style)     设置字体格式，有['bold','normal','italic', 'bold italic']
setText(text)       设置text
setTextColor(color) 设置text颜色
#继承自GraphicsObject
draw(win)
move(dx, dy)
setFill(color)
setOutline(color)
setWidth(width)
undraw()

#Transform类


