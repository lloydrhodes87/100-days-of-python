from turtle import Turtle

class Ball(Turtle):
    """Ball class"""

    def  __init__(self):
        super().__init__()
       
        self.shape("circle")
        self.goto(0, 0)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):

        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.x_move *= -1
        self.goto(0, 0)


        