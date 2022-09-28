from turtle import Turtle

TOP_LIMIT = 280
BOTTOM_LIMIT = -280


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x_speed = 10
        self.y_speed = 10
        self.speed = 0.1
        self.color("blue")

    def move(self):
        if self.ycor() > TOP_LIMIT or self.ycor() < BOTTOM_LIMIT:
            self.bounce_y()
        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1
        self.speed *= 0.99

    def reset(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.x_speed *= -1