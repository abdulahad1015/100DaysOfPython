import turtle
from turtle import Turtle,Screen
import random
import time
from snake import Snake
screen=Screen()
screen.setup(1000,600)
screen.bgcolor("black")
screen.title("My Snake Game")



snake=Snake()
screen.listen()

key =0
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
screen.onkey(up,"w")
screen.onkey(down,"s")
screen.onkey(left,"a")
screen.onkey(right,"d")


while(True):
    screen.update()
    if(key==1):
        screen.delay(0.5)
        if (snake.up()):
            print("Game Over")
            break
        screen.update()
    if (key == 2):
        screen.delay(0.5)
        if(snake.down()):
            print("Game Over")
            break
        screen.update()
    if (key == 3):
        screen.delay(0.5)
        if (snake.left()):
            print("Game Over")
            break
        screen.update()
    if (key == 4):
        screen.delay(0.5)
        if (snake.right()):
            print("Game Over")
            break
    time.sleep(0.1)

print("Your score is : ",snake.score)
screen.exitonclick()
screen.mainloop()

