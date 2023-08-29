import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("dark slate blue")
screen.tracer(0)
screen.listen()
player = Player()
traffic = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(fun=player.move_up, key="Up")

counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Only create cars every 5 loops
    if counter % 5 == 0:
        traffic.create_n_cars(1)

    # Check player collision with car
    if player.collision_with_car(traffic.car_list):
        print("GAME OVER, You got hit by a car")
        scoreboard.game_over()
        game_is_on = False

    traffic.move_cars()

    # Check to see if player made it across to the next level
    if player.has_finished():
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        traffic.increase_car_speed()
        player.reset_player()

    counter += 1

screen.exitonclick()
