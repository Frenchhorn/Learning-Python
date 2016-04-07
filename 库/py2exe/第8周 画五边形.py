#在窗口中点击5个点来画一个五边形
from graphics import *

win = GraphWin('画五边形', 500, 500)
win.setCoords(0, 0, 500, 500)
message = Text(Point(250, 50), '点击五个点')
message.draw(win)
#获得多边形的5个点
p1 = win.getMouse()
p1.draw(win)
p2 = win.getMouse()
p2.draw(win)
p3 = win.getMouse()
p3.draw(win)
p4 = win.getMouse()
p4.draw(win)
p5 = win.getMouse()
p5.draw(win)
#使用Polygon对象绘制多边形
polygon = Polygon(p1,p2,p3,p4,p5)
polygon.setFill('red')
polygon.setOutline('blue')
polygon.draw(win)
#等待响应鼠标事件，退出程序
message.setText('点击退出')
win.getMouse()
win.close()
