from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    tim.setheading(90)

screen.listen()

tim.setheading(90)
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(clear, "c")

screen.exitonclick()



