from turtle import Turtle, Screen
from random import randint
import random

WIDTH = 1000
HEIGHT = 1000
BGCOLOR = (72, 61, 139)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rbg = (r, g, b)
    if rbg == BGCOLOR:
        return (g, b, r)
    return rbg


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.colormode(255)
screen.bgcolor("dark slate blue")
timmy = Turtle()
timmy.shape("turtle")
timmy.color("dark orange")
timmy.pensize(1)
timmy.speed(0)

for num in range(0, 360, 5):
    timmy.setheading(num)
    timmy.color(random_color())
    timmy.circle(100)


# # Random Walk
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.setheading(random.choice(directions))
#     timmy.forward(30)

# sides = 3
# while sides < 11:
#     angle = (sides - 2) * 180 / sides
#     timmy.color(random.choice(colors))
#     for _ in range(sides):
#         timmy.right(180 - angle)
#         timmy.forward(100)
#     sides += 1

screen.exitonclick()
