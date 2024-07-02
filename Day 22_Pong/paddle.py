from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(xcor, ycor)
        self.color("white")
        self.left(90)
        self.speed(0)

    def go_down(self):
        if(self.ycor() > -250):
            self.backward(30)

    def go_up(self):
        if (self.ycor() < 250):
            self.forward(30)