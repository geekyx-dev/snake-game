import turtle
from turtle import Turtle
import random
from gfx import foods
import scoreboard


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        for f in foods:
            turtle.register_shape(f)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.penup()
        self.goto(random_x, random_y)
        self.shape(random.choice(foods))
        
