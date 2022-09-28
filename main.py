from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DASH_SIZE = 20
RIGHT = 350
LEFT = -350


def draw_divider():
    divider = Turtle()
    divider.color("white")
    divider.hideturtle()
    divider.penup()
    divider.goto(0, SCREEN_HEIGHT / 2)
    divider.setheading(270)
    divider.pendown()
    for _ in range(int(SCREEN_HEIGHT / DASH_SIZE)):
        divider.forward(20)
        divider.penup()
        divider.forward(20)
        divider.pendown()


def start_game():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)
    draw_divider()
    screen.listen()

    is_game_on = True

    player_1 = Paddle(380, 0)
    player_2 = Paddle(-380, 0)
    ball = Ball()
    scoreboard = ScoreBoard()
    scoreboard.update_score()

    screen.onkeypress(key="Up", fun=player_1.move_up)
    screen.onkeypress(key="Down", fun=player_1.move_down)
    screen.onkeypress(key="w", fun=player_2.move_up)
    screen.onkeypress(key="s", fun=player_2.move_down)

    while is_game_on:
        screen.update()
        time.sleep(ball.speed)
        ball.move()

        # Detect ball collision w/ paddle
        if (ball.distance(player_1) < 30 and ball.xcor() > RIGHT) or (ball.distance(player_2) < 30 and ball.xcor() < LEFT):
            ball.bounce_x()

        if ball.xcor() > 380:
            scoreboard.increment_score(2)
            scoreboard.update_score()
            ball.reset()
        if ball.xcor() < -380:
            scoreboard.increment_score(1)
            scoreboard.update_score()
            ball.reset()

    screen.exitonclick()


start_game()
