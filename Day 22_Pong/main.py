from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

r_score=0
l_score=0
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball(0, 0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# screen.tracer()

print(ball.heading())
Game = True
while (Game):
    ball.forward(5)
    # screen.update()
    print(ball.heading())
    if (ball.xcor() >= 329 and ball.xcor() <= 340 and abs(r_paddle.ycor() - ball.ycor()) <= 50):
        ball.left(180 - 2 * (ball.heading() % 90))
    elif (ball.xcor() <= - 329 and ball.xcor() >= - 340 and abs(l_paddle.ycor() - ball.ycor()) <= 50):
        ball.left(180 - 2 * (ball.heading() % 90))
    elif (ball.ycor() >= 290):
        ball.left(180 - 2 * (ball.heading() % 90))
    elif (ball.ycor() <= - 290):
        ball.left(180 - 2 * (ball.heading() % 90))
    elif (ball.xcor() >= 380):
        ball.reset(r_score,l_score)
        l_score+=1
        time.sleep(1)
    elif (ball.xcor() <= -380):
        ball.reset(r_score,l_score)
        r_score+=1
        time.sleep(1)

screen.exitonclick()
screen.mainloop()
