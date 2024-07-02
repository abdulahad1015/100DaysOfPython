from turtle import Turtle
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(-380, 275)
        self.write("Score : 0",font=FONT)

    def update(self,score):
        self.clear()
        self.write(f"Score : {score}", font=FONT)
    def end(self):
        self.goto(-70,270)
        self.clear()
        self.write("Game Over !", font=("Arial", 18, "normal"))

