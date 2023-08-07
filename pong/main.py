from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


player_1_paddle = Paddle(x_pos=350)
player_2_paddle = Paddle(x_pos=-350)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1_paddle.go_up, 'Up')
screen.onkey(player_1_paddle.go_down, 'Down')

screen.onkey(player_2_paddle.go_up, 'w')
screen.onkey(player_2_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_1_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(player_2_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_score += 1
        ball.reset()
        scoreboard.update_score()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_score += 1
        scoreboard.update_score()


    time.sleep(0.1)

screen.exitonclick()