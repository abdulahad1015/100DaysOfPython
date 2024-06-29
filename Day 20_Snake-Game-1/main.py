from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")

xcord=0
scord=0
segments=[]
for j in range(10):
    scord+=10
    xcord=scord
    for i in range(3):
        segments.append(Turtle("square"))
        segments[i].color('white')
        segments[i].penup()
        segments[i].goto(xcord,0)
        xcord -= 20
screen.exitonclick()
