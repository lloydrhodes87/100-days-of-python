from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


player_1_paddle = Paddle(x_pos=350)

player_2_paddle = Paddle(x_pos=-350)

screen.listen()
screen.onkey(player_1_paddle.go_up, 'Up')
screen.onkey(player_1_paddle.go_down, 'Down')

screen.onkey(player_2_paddle.go_up, 'w')
screen.onkey(player_2_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()