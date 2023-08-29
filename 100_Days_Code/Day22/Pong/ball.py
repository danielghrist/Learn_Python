from turtle import Turtle

WIDTH = 800
HEIGHT = 600


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.__x_move = 2
        self.__y_move = 2
        #self.speed_value = 1


    # Check for top or bottom wall collision
    def top_bottom_collision(self):
        if self.ycor() > HEIGHT / 2 - 20 or self.ycor() < -(HEIGHT / 2 - 20):
            return True

    def bounce_y(self):
        self.__y_move *= -1

    def bounce_x(self):
        self.__x_move *= -1
        #self.speed_value *= .09

    # def speed_up(self):
    #     speed_increment = .5
    #     if self.__x_move < 0:
    #         self.__x_move -= speed_increment
    #     else:
    #         self.__x_move += speed_increment
    #
    #     if self.__y_move < 0:
    #         self.__y_move -= speed_increment
    #     else:
    #         self.__y_move += speed_increment

    def reset(self):
        self.home()
        self.bounce_x()
        #self.speed_value = .09


    def move(self):
        self.clear()
        new_x = self.__x_move + self.xcor()
        new_y = self.__y_move + self.ycor()
        self.goto(new_x, new_y)
        self.write("😎", align="center", font=("Arial", 20, "bold"))

