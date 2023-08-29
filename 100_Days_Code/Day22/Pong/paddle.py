from turtle import Turtle

WIDTH = 800
HEIGHT = 600
MOVE_DISTANCE = 10
FONT = ("Arial", 20, "bold")


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle_width = 5
        self.paddle_length = 1
        self.color("orange")
        self.turtlesize(stretch_wid=self.paddle_width, stretch_len=self.paddle_length)
        self.shape("square")
        self.penup()
        self.goto(position)

    def move_up(self):
        top_screen = (HEIGHT / 2) - ((self.paddle_width * 25) / 2)
        if self.ycor() < top_screen:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        bottom_screen = -((HEIGHT / 2) - ((self.paddle_width * 25) / 2))
        if self.ycor() > bottom_screen:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
