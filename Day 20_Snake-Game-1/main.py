import turtle
from turtle import Turtle,Screen
import random
from snake import Snake
screen=Screen()
screen.setup(1000,600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake=Snake()
screen.listen()
key =0

def up():
    key=1
    screen.delay(0.5)
    snake.up()
    screen.update()

def down():
    key=2
    screen.delay(0.5)
    snake.down()
    screen.update()

def left():
    key = 3
    screen.delay(0.5)
    snake.left()
    screen.update()

def right():
    key=4
    screen.delay(0.5)
    snake.right()
    screen.update()

screen.onkey(up,"w")
screen.onkey(down,"s")
screen.onkey(left,"a")
screen.onkey(right,"d")

while(1):
    screen.listen()
    if(key==1):
        screen.delay(0.5)
        snake.up()
        screen.update()
    if (key == 2):
        snake.down()
    if (key == 3):
        snake.left()
    if (key == 4):
        snake.right()

screen.exitonclick()
