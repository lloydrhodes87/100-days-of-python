from turtle import Turtle
STARTING_POSITIONS =  [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """The snake class"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.speed = 0.1
    def add_segment(self, position):
        """increase snake size"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment) 

    def create_snake(self):
        """creates the snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        """extends the snake"""
        self.add_segment(self.segments[-1].position())

    
    def move(self):
        """Controls the movement of the snake"""

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)

   
        

    def up(self):
        """moves the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """moves the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """moves the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """moves the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)