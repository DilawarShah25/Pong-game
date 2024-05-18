# PONG game
from scoreboard import Scoreboard
from paddle import Paddle
from turtle import Screen
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_position = (360, 0)
r_paddle = Paddle(r_position)
r_paddle.color("green")
r_paddle.fillcolor("red")

l_position = (-360, 0)
l_paddle = Paddle(l_position)
l_paddle.color("green")
l_paddle.fillcolor("red")

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.y_bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.ycor() > -320:
        ball.x_bounce()

    # Detect r_paddle collision
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l_paddle collision
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
