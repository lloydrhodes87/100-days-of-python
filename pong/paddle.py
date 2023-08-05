from turtle import Turtle

class Paddle(Turtle):
    """A class for a paddle"""

    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = 0
        self.create_paddle()

    def create_paddle(self):
        """creates the default paddle"""
        self.penup()
        self.shape("square")

        self.shapesize(5, 1)
        self.color("white")
        self.goto((self.x_pos, 0))
      

    def go_up(self):
        """moves the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        """moves the paddle up"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


