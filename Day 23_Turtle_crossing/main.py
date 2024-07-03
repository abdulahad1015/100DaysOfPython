import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
score=0

player = Player()

def up():
    player.forward(20)
def down():
    player.backward(20)

cars=[]
for i in range(10):
    cars.append(CarManager())
    screen.update()

screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")

game_on=True
while(game_on):
    for i in cars:
        if(player.ycor()-i.ycor()<20 and player.distance(i)<=30):
            game_on=False
            scoreboard.end()
            continue

        elif(i.xcor()<=-400):
            i.start_reset()

        else:
            i.forward()

        if(player.ycor()>280):
            for j in cars:
                j.reset()
            cars.append(CarManager())
            player.reset()
            score += 1
            CarManager.increase_speed()
            scoreboard.update(score)

    screen.update()
    time.sleep(0.01-score/1000)


screen.exitonclick()
screen.mainloop()