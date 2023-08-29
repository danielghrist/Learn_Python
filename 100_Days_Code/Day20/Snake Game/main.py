import sys
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

# Define the dimensions for the game window:
WIDTH = 800
HEIGHT = 800

# Define the speed intervals:
START_SPEED = 0.1
SPEED_CHANGE = 0.001


# Reset and clear the screen, then exit the program:
def end_program():
    screen.resetscreen()
    screen.clear()
    screen.bye()
    sys.exit()


# Create screen to show/play game on:
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("dark slate blue")
screen.title("Danny's Snake Game")
screen.tracer(0, None)

# Create game objects:
snake = Snake()
food = Food()
score_board = Score()


# Set up key listener:
screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=end_program, key="q")

# Start main game loop:
current_speed = START_SPEED
game_is_on = True
while game_is_on:
    # If the screen is resized then update the scoreboard so it's position is relative to new window size:
    if screen.window_height() != HEIGHT:
        score_board.update_scoreboard(current_speed)

    screen.update()
    time.sleep(current_speed)
    snake.move()

    # Check collision with food, change speed and snake length if successful:
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        score_board.update_scoreboard(current_speed)
        if current_speed > 0 + SPEED_CHANGE:
            current_speed -= SPEED_CHANGE
        snake.extend()

    # Check collision with wall and reset score, speed, and snake length:
    if snake.wall_collision(screen.window_width(), screen.window_height()):
        print("You hit the wall!")
        score_board.reset()
        snake.reset()
        current_speed = START_SPEED
        # score_board.game_over()

    # Detect collision with tail and reset score, speed, and snake length:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()
            current_speed = START_SPEED


screen.mainloop()
