from turtle import Turtle, Screen
import colorgram
import random

WIDTH = 800
HEIGHT = 800
RADIUS = 20
NUM_COLORS = 30
colors = colorgram.extract("image.jpg", NUM_COLORS)
image_colors = []
timmy = Turtle()
timmy.hideturtle()
timmy.speed(0)
timmy.penup()
timmy.setposition(-int(WIDTH/2)+50, int(HEIGHT/2)-50)
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.colormode(255)


# fill list of colors from image
def format_rgb(extracted_colors):
    for num in range(NUM_COLORS):
        r = colors[num].rgb.r
        g = colors[num].rgb.g
        b = colors[num].rgb.b
        rgb = (r, g, b)
        image_colors.append(rgb)


# def draw_circle(turtle):
def draw_circle_row():
    for _ in range(int(WIDTH / 100)):
        timmy.pendown()
        timmy.begin_fill()
        random_color = random.choice(image_colors)
        timmy.color(random_color)
        timmy.circle(RADIUS)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(100)


format_rgb(colors)
num_circle_rows = int(HEIGHT / 100)
for row in range(num_circle_rows):
    draw_circle_row()
    timmy.backward(WIDTH)
    timmy.right(90)
    timmy.forward(100)
    timmy.setheading(0)

screen.exitonclick()
