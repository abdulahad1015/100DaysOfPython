import time
from turtle import Turtle
from random import randint
class Snake():
    def __init__(self):
        self.segments=[]
        self.num_of_segments=3
        self.temp=Turtle("square")
        self.temp.color('white')
        self.temp.penup()
        self.temp.hideturtle()
        self.score=0
        xcord=0

        for i in range(3):
            self.segments.append(Turtle("square"))
            self.segments[i].color('white')
            self.segments[i].penup()
            self.segments[i].goto(xcord,self.segments[i].ycor())
            xcord-=20

        self.point = Turtle("circle")
        self.point.color('red')
        self.point.penup()
        self.point.goto(randint(-24, 24)*20, randint(-14, 14)*20)

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
        if(head.xcor()>490):
            return 1
        else:
            if (self.snake_point()):
                return 1
            else:
                return 0
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
        if (head.xcor() < -490):
            return 1
        else:
            if (self.snake_point()):
                return 1
            else:
                return 0
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
        if (head.ycor() < -290):
            return 1
        else:
            if (self.snake_point()):
                return 1
            else:
                return 0
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
        if (head.ycor() > 290):
            return 1
        else:
            if(self.snake_point()):
                return 1
            else:
                return 0

    def snake_point(self):
        for i in range(1,self.num_of_segments):
            if(self.segments[i].pos()==self.segments[0].pos()):
                return 1
        if(self.segments[0].pos()==self.point.pos()):
            self.segments.append(Turtle("square"))
            self.segments[self.num_of_segments].color('white')
            self.segments[self.num_of_segments].penup()
            self.segments[self.num_of_segments].goto(self.segments[self.num_of_segments-1].xcor(),self.segments[self.num_of_segments-1].ycor())
            self.num_of_segments+=1
            self.point.hideturtle()
            self.point.goto(randint(-24, 24)*20, randint(-14, 14)*20)
            self.point.showturtle()
            self.score+=10



