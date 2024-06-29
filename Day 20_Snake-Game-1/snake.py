import time
import turtle
from turtle import Turtle

class Snake():
    def __init__(self):
        self.segments=[]
        self.temp=Turtle("square")
        self.temp.color('white')
        self.temp.penup()
        self.temp.hideturtle()
        xcord=0
        for i in range(10):
            self.segments.append(Turtle("square"))
            self.segments[i].color('white')
            self.segments[i].penup()
            self.segments[i].speed(0)
            self.segments[i].goto(xcord,self.segments[i].ycor())
            xcord-=20

    def right(self):
        xcord=self.segments[0].xcor()
        ycord = self.segments[0].ycor()
        head=self.segments.pop()
        self.temp.goto(xcord+20,ycord)
        head.hideturtle()
        self.temp.showturtle()
        head.goto(xcord+20,ycord)
        head.showturtle()
        self.temp.hideturtle()
        self.segments.insert(0,head)

    def left(self):
        xcord=self.segments[0].xcor()
        ycord = self.segments[0].ycor()
        head = self.segments.pop()
        self.temp.goto(xcord - 20, ycord)
        head.hideturtle()
        self.temp.showturtle()
        head.goto(xcord - 20, ycord)
        head.showturtle()
        self.temp.hideturtle()
        self.segments.insert(0,head)

    def down(self):
        xcord=self.segments[0].xcor()
        ycord = self.segments[0].ycor()
        head = self.segments.pop()
        self.temp.goto(xcord, ycord-20)
        head.hideturtle()
        self.temp.showturtle()
        head.goto(xcord, ycord-20)
        head.showturtle()
        self.temp.hideturtle()
        self.segments.insert(0,head)

    def up(self):
        xcord=self.segments[0].xcor()
        ycord = self.segments[0].ycor()
        head = self.segments.pop()
        self.temp.goto(xcord, ycord+20)
        head.hideturtle()
        self.temp.showturtle()
        head.goto(xcord , ycord+20)
        head.showturtle()
        self.temp.hideturtle()
        self.segments.insert(0,head)



