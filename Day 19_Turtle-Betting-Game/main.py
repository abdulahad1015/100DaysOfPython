from turtle import Turtle,Screen
import random
screen=Screen()
turtles=[]
draw=Turtle()
draw.hideturtle()
draw.penup()
draw.goto(300,-150)
draw.pendown()
for i in range(-150,150,10):
    if((i/10)%2==0):
        draw.pendown()
    else:
        draw.penup()
    draw.goto(300,i)

colours=['red','yellow','purple','blue','green']
y_cord=-100
for i in range(5):
    turtles.append(Turtle("turtle"))
    turtles[i].color(colours[i])
    turtles[i].penup()
    turtles[i].goto(-300, y_cord)
    y_cord += 50

user_bet=screen.textinput("Make your bet","Which turtle will win the race ? Enter a Color: ")

race_end=0
while(race_end==0):
    race_end=1
    for i in turtles:
        pos=i.xcor()
        rand=random.randint(0,10)
        if(pos<300):
            race_end=0
            if(rand+pos>300):
                i.goto(300,i.ycor())
            else:
                i.forward(rand)
        else:
            if (i.color()[0] == user_bet):
                print("You won the bet")
            else:
                print(i.color()[0]," Won !!!")
                print("You Lost the bet")
            race_end = 1
            break
screen.exitonclick()
