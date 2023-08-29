from turtle import Turtle, Screen
import random

WIDTH = 500
HEIGHT = 400
NUM_TURTLES = 6
colors = ["blue", "green", "yellow", "orange", "cyan", "red"]
all_turtles = []
screen = Screen()
screen.setup(WIDTH, HEIGHT)


def move_random(turtle):
    turtle.forward(random.randint(1, 10))


def is_winner(racers):
    for turtle in racers:
        if turtle.xcor() >= int((WIDTH / 2) - 25):
            return True
    return False


is_race_on = False
user_bet = screen.textinput("Make your bets!  ", "Which turtle will win the race?  Enter a color:  ")

start_line_y = -150
for turtle in range(NUM_TURTLES):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.speed("fastest")
    new_turtle.goto(x=-230, y=start_line_y)
    start_line_y += int(HEIGHT / NUM_TURTLES)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        move_random(turtle)
        if turtle.xcor() >= (int(WIDTH/2)-30):
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You win! Your {user_bet} turtle is the fastest.")
            else:
                print(f"You Lost. Your {user_bet} turtle lost to the {winning_color} turtle")


screen.exitonclick()
