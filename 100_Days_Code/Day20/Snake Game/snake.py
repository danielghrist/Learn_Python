from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = self.head.heading()

    # Creates a snake of made of 3 square turtle objects
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Moves the last segment of the snake into the one in front of it's position
    # then moves the head of the snake forward
    def move(self):
        if self.segments == None:
            return

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        snake_segment = Turtle()
        snake_segment.color("orange")
        snake_segment.shape("square")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)
        # Original way I did this, without a coordinate array
        # if num > 0:
        #     snake_body[num].setposition(snake_body[num-1].xcor() - 20, snake_body[num].ycor())

    def extend(self):
        self.add_segment(self.segments[len(self.segments) - 1].position())

    def wall_collision(self, width, height):
        top = (height / 2) - 20
        bottom = -((height / 2) - 20)
        right = (width / 2) - 20
        left = -((width / 2)) + 20
        if self.head.xcor() > right or self.head.xcor() < left:
            return True
        elif self.head.ycor() > top or self.head.ycor() < bottom:
            return True
        else:
            return False
        # if self.head.distance(self.head.xcor(), (height / 2)) == 0:
        #     return True
        # if self.head.distance(self.head.xcor(), -(height / 2)) == 0:
        #     return True
        # if self.head.distance((width / 2), self.head.ycor()) == 0:
        #     return True
        # if self.head.distance(-(width / 2), self.head.ycor()) == 0:
        #     return True
        # else:
        #     return False

    def exit(self):
        self.segments = None

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
