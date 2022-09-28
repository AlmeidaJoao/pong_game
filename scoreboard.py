from turtle import Turtle
FONT = ("Arial", 40, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(2, 200)
        self.color("white")
        self.penup()
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.player_2_score}   {self.player_1_score}", font=FONT, align=ALIGNMENT)

    def increment_score(self, player):
        exec (f"self.player_{player}_score += 1")
