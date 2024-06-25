import colorgram
from random import randint
import turtle
from turtle import Screen,Turtle
tim = Turtle()
turtle.colormode(255)
tim.width(15)
tim.speed(10000)
tim.ht()
# # Extract 6 colors from an image.
colors = colorgram.extract('pic.jpg', 30)

RGB = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    RGB.append((r, g, b))
print(RGB)


for i in range(-160,240,40):
    tim.up()
    tim.goto(-200,i)
    tim.down()
    for j in range(10):
        tim.pencolor(RGB[randint(1,28)])
        tim.forward(1)
        tim.penup()
        tim.forward(50)
        tim.pendown()

turtle.Screen().exitonclick()
