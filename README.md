# Learning-Python
From 2015-11-11 to
=======
Hi Humans!

import turtle

def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)   
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)  
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0, 0)   
    pythonsize = 40
    turtle.pensize(pythonsize)  
    turtle.pencolor("red")
    turtle.seth(-40)    
    drawSnake(40, 80, 5, pythonsize/2)

main()
