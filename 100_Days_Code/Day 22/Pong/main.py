from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("dark slate blue")
screen.tracer(0)
screen.listen()

right = ((WIDTH / 2 - 20), 0)
left = (-(WIDTH / 2 - 20), 0)
right_paddle = Paddle(right)
left_paddle = Paddle(left)
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")
screen.onkeypress(fun=left_paddle.move_up, key="w")
screen.onkeypress(fun=left_paddle.move_down, key="s")

is_game_over = False
while not is_game_over:
    time.sleep(.01)
    screen.update()
    ball.move()
    if ball.top_bottom_collision():
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.xcor() > 365 and ball.distance(right_paddle) <= 50:
        ball.bounce_x()

    # Detect collision with left paddle
    if ball.xcor() < -365 and ball.distance(left_paddle) <= 50:
        ball.bounce_x()

    # Check for right paddle misses
    if ball.xcor() > WIDTH / 2:
        scoreboard.increase_left_score()
        ball.reset()

    # Check for left paddle misses
    if ball.xcor() < -(WIDTH / 2):
        scoreboard.increase_right_score()
        ball.reset()

    # if ball.paddle_collision(right_paddle):
    #     ball.bounce_x()
    #
    # if ball.paddle_collision(left_paddle):
    #     ball.bounce_x()

screen.exitonclick()
