from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)
        if(self.ycor()>=FINISH_LINE_Y):
            return 1
    def down(self):
        self.backward(MOVE_DISTANCE)

    def reset(self):
        self.hideturtle()
        self.goto(0 ,-280)
        self.showturtle()

