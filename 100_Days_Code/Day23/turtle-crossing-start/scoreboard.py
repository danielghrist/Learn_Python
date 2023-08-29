from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-280, 265)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("orange")
        self.penup()
        self.goto(SCORE_POSITION)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER!", align="center", font=FONT)


