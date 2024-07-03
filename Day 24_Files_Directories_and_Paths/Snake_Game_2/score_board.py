from turtle import Turtle

class score_board(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.goto(-120,275)
        self.penup()
        self.highscore=0
        self.score=0
        file = open("myfile.txt")
        self.highscore = int(file.read())
        file.close()

    def gameover(self):
        self.home()
        self.backward(50)
        self.color("yellow")

        if(self.score>self.highscore):
            print("Score")
            self.write("Game Over\n New High Score", font={"Arial", 28, "normal"})
            with open("myfile.txt",mode="w") as data:
                data.write(f"{self.score} ")
        else:
            self.write("Game Over", font={"Arial",28,"normal"})

    def show_score(self,score):
        self.clear()
        self.score=score
        self.color("white")
        self.write(f"Score = {self.score} HighScore = {self.highscore}", font={"calibri", 18, "normal"})