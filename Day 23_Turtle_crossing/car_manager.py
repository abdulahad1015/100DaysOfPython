from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

class CarManager(Turtle):
    move = STARTING_MOVE_DISTANCE
    def __init__(self):
        super().__init__(visible=False,shape="square")
        self.color(COLORS[random.randint(0,5)])
        self.shapesize(stretch_len=2)
        self.speed(1)
        self.penup()
        self.speed(0)
        self.goto(410+random.randint(0,700),(random.randint(-13, 14)*20))
        self.setheading(180)
        self.showturtle()

    def reset(self):
        self.hideturtle()
        self.goto(410+random.randint(0,700), (random.randint(-13, 14)*20) )
        self.color(COLORS[random.randint(0, 5)])
        self.showturtle()

    def start_reset(self):
        self.hideturtle()
        self.goto(410 , (random.randint(-13, 14)*20) )
        self.color(COLORS[random.randint(0, 5)])
        self.showturtle()

    def forward(self):
        super().forward(CarManager.move)

    @staticmethod
    def increase_speed():
        CarManager.move+=MOVE_INCREMENT

