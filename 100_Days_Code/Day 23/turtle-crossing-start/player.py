from turtle import  Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("orange")
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def has_finished(self):
        return self.ycor() > FINISH_LINE_Y

    def collision_with_car(self, car_list):
        for car in car_list:
            player_x = self.xcor()
            player_y = self.ycor()
            car_x = car.xcor()
            car_y = car.ycor()
            if car.xcor() < 40  and car.xcor() > -40 and abs(self.ycor() - car.ycor()) < 20:
                # print(f"({player_x}, {player_y})")
                # print(f"({car_x}, {car_y})")
                # print(f"x distance {player_x - car_x}")
                # print(f"y distance {player_y - car_y}")
                return True
        return False

    def reset_player(self):
        self.goto(STARTING_POSITION)




