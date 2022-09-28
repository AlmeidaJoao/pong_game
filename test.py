from turtle import Turtle, Screen

def move_right():
    turtle.setheading(0)
    turtle.forward(25)
    screen.update()

def move_up():
    turtle.setheading(90)
    turtle.forward(25)
    screen.update()

def move_left():
    turtle.setheading(180)
    turtle.forward(25)
    screen.update()

def move_down():
    turtle.setheading(270)
    turtle.forward(25)
    screen.update()

turtle = Turtle()
screen = Screen()
screen.tracer(0)
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_down, "Down")

screen.listen()
screen.exitonclick()