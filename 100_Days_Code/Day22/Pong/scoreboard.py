from turtle import Turtle

FONT = ("Arial", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.score_left = 0
        self.score_right = 0
        self.update_score()
        self.draw_background()

    def draw_background(self):
        for i in range(300, -300, -100):
            turtle = Turtle()
            turtle.penup()
            turtle.color("orange")
            turtle.shape("square")
            turtle.shapesize(stretch_wid=3, stretch_len=1)
            turtle.goto(0, i-50)

    def increase_left_score(self):
        self.score_left += 1
        self.update_score()

    def increase_right_score(self):
        self.score_right += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score_left}          {self.score_right}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("🎮GAME OVER🕹", align="center", font=FONT)