import random
import time
import tkinter as tk
from tkinter import Label

gx, gy = 15, 15  #棋盘大小
#网格状态
EMPTY = '#0000FF'
SNAKE = '#FFFF00'
FRUIT = '#00FF00'
g = [[EMPTY for x in range(gx)] for y in range(gy)]  #棋盘

snake = []
#列表每一个(y,x)表示蛇的身体坐标
#snake[0]蛇尾, snake[-1]蛇头

UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
position = DOWN

class Die(Exception):  #死亡时抛出这个异常
    pass

def spawnfruit():  #生成一个食物
    available = [(y,x) for y in range(gy) for x in range(gx) if g[y][x]==EMPTY]
    if available:
        y, x = random.choice(available)  #随机选一个位置放置食物
        g[y][x] = FRUIT
        labels[y][x]['background'] = FRUIT
    else:
        raise Die()

def delchunk():  #删除蛇尾
    y, x = snake[0]
    g[y][x] = EMPTY
    labels[y][x]['background'] = EMPTY
    del snake[0]

def moveto(y, x):  #把蛇移动到(y,x)位置
    fruit_flag = False  #碰到食物的flag
    
    if not((0<=y<gy) and (0<=x<gx)): #碰到边界就会死
        raise Die()

    if g[y][x] == SNAKE:  #碰到自己就会死
        raise Die()

    if g[y][x] == FRUIT:  #碰到食物
        fruit_flag = True

    snake.append((y,x))
    g[y][x] = SNAKE
    labels[y][x]['background'] = SNAKE

    if fruit_flag:
        spawnfruit()  #生成新的食物
    else:
        delchunk()  #正常移动，删除蛇尾

def push():  #蛇头往前方向增长一格
    now_y, now_x = snake[-1]  #蛇头原本位置
    if position == UP:
        moveto(now_y-1, now_x)
    elif position == DOWN:
        moveto(now_y+1, now_x)
    elif position == LEFT:
        moveto(now_y, now_x-1)
    elif position == RIGHT:
        moveto(now_y, now_x+1)

def init():  #初始化
    #清空棋盘
    while snake:
        delchunk()
    for y in range(gy):
        for x in range(gx):
            g[y][x] == EMPTY

    #生成一条蛇和一个食物
    for y, x in [(1,0),(2,0),(3,0)]:
        snake.append((y,x))
        g[y][x] = SNAKE
    spawnfruit()

def game_controller():  #整个游戏的流程
    init()
    while True:
        try:
            push()
            time.sleep(0.5)
        except Die:
            init()

labels = [[None for x in range(gx)] for y in range(gy)]
for y in range(gy):
    for x in range(gx):
        labels[y][x] = Label(tk, text='  ',font='-size 10',background = EMPTY)
        labels[y][x].grid(row=y,column=x)

def setposition(pos):
    global position
    if position==UP and pos==DOWN: #不能把方向变成相反的
        return
    if position==DOWN and pos==UP:
        return
    if position==LEFT and pos==RIGHT:
        return
    if position==RIGHT and pos==LEFT:
        return
    position=pos

tk.bind('<Up>',lambda _: setposition(UP))
tk.bind('<Down>',lambda _: setposition(DOWN))
tk.bind('<Left>',lambda _: setposition(LEFT))
tk.bind('<Right>',lambda _: setposition(RIGHT))

