import turtle
from turtle import Turtle
from gfx import heads,body
COORDINATES = [(0, 0), (-15, 0), (-30, 0)]
MOVE_DISTANCE = 15

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        for h in heads:
            turtle.register_shape(h)
        turtle.register_shape(body)
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for coordinate in COORDINATES:
            self.add_segements(coordinate)
        self.head = self.segments[0]
        self.head.shape(heads[2])

    def add_segements(self, coordinate):
        new_segment = Turtle("img/b.gif")
        new_segment.penup()
        new_segment.goto(coordinate)
        self.segments.append(new_segment)

    def extend(self):
        ##add new segments to the snake
        self.add_segements(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.shape(heads[3])
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.shape(heads[0])
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.shape(heads[1])
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.shape(heads[2])
            self.segments[0].setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]