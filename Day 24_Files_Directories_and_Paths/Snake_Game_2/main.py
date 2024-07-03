from turtle import Turtle,Screen
import time
from snake import Snake
from score_board import score_board

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()

screen.listen()

Score_board = score_board()

speed = 0

key = 4
def up():
    global key
    if (key != 2):
        key = 1


def down():
    global key
    if (key != 1):
        key = 2


def left():
    global key
    if (key != 4):
        key = 3


def right():
    global key
    if (key != 3):
        key = 4


# Map keys
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")

game_off = 0
while (True):
    screen.delay(0.1)
    if (key == 1):
        game_off = snake.up()
    elif (key == 2):
        game_off = snake.down()
    elif (key == 3):
        game_off = snake.left()
    elif (key == 4):
        game_off = snake.right()
    if (game_off == 1):
        Score_board.show_score(score=snake.score)
        Score_board.gameover()
        break
    Score_board.show_score(score=snake.score)
    screen.update()
    time.sleep(0.1 - snake.score / 1000)

screen.exitonclick()
screen.mainloop()
