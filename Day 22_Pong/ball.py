from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.left(random.randint(10,40))
        self.speed(0)

    def reset(self,r_score,l_score):
        self.hideturtle()
        self.clear()
        self.goto(-15,270)
        self.color("yellow")
        self.write(f"{r_score} : {l_score}", font={"calibri", 18, "normal"})
        self.home()
        self.left(random.randint(10, 40))
        self.color("white")
        self.showturtle()
