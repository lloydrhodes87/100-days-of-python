from turtle import Turtle
ALIGN="center"
FONT=("Arial", 14, "normal")

class Scoreboard(Turtle):
    """A class that handles scores"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto((0, 280))
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 5
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
