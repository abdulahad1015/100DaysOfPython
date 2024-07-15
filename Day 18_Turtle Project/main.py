import turtle
from turtle import Screen,Turtle
from random import randint


tim = Turtle()
screen=Screen()
tim.speed(1000)
tim.width(1)
turtle.colormode(255)

def color_gen():
    r=randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r,g,b)

num=0
for j in range(50):
    num+=1
    for i in range(3, 50):
        num = randint(0, 4)
        tim.pencolor(color_gen())
        tim.circle(90)
        tim.right(10-num)


screen.exitonclick()