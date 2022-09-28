from turtle import Turtle

MOVE_SPEED = 20
TOP_LIMIT = 280
BOTTOM_LIMIT = -280


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(x_position, y_position)
        self.shapesize(stretch_wid=3, stretch_len=.5)

    def move_up(self):
        if not self.ycor() > TOP_LIMIT:
            self.goto(self.xcor(), self.ycor() + MOVE_SPEED)

    def move_down(self):
        if not self.ycor() < BOTTOM_LIMIT:
            self.goto(self.xcor(), self.ycor() - MOVE_SPEED)
