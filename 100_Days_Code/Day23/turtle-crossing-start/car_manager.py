from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_n_cars(self, num_cars):
        for i in range(num_cars):
            car = Turtle()
            car.starting_y_cor = random.randint(-250, 250)
            car.color(random.choice(COLORS))
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.goto(300, car.starting_y_cor)
            if i - 1 >= 0:
                if self.car_list[i].distance(self.car_list[i - 1]) < 20:
                    car.goto(300, car.starting_y_cor)
                else:
                    car.goto(300, car.starting_y_cor + 10)
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT

