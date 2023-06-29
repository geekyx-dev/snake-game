import time
import turtle
import winsound
from gfx import bg
from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#222")  

screen.bgpic("img/banner.gif")  
turtle.update()  
screen.title("Snake Game")

loader = turtle.Turtle()


def loadming():
    loader.color("white")
    loader.penup()
    loader.hideturtle()
    x, y = -150, -20
    loader.goto(x, y)
    for i in range(10):
        loader.write(arg="🟨", font=("courier", 30, "bold"))
        x += 30
        loader.goto(x, y)
        time.sleep(0.2)
    loader.clear()
    loader.goto(-150, y)
    loader.write(arg=f"Starting", font=("courier", 30, "bold"))
    x = 20
    for i in range(0, 5):
        loader.write(arg=".", font=("courier", 30, "bold"))
        x += 20
        loader.goto(x, y)
        time.sleep(0.2)
    loader.clear()


loadming()

screen.bgpic("img/bg.gif")
snake = Snake()
food = Food()
scoreboard = Scoreboard("Yellow")

game_is_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def countdown():
    for i in range(3, -1, -1):
        loader.goto(-20, 50)
        loader.color("Yellow")
        loader.write(f"{i}", font=("Arial", 50, "bold"))
        time.sleep(0.5)
        loader.clear()


countdown()
del loader
screen.tracer(0)

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collison with food
    if snake.head.distance(food) < 15:
        winsound.Beep(1000, 100)
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collison with wall
    if (
        snake.head.xcor() > 300
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -300
    ):
        winsound.Beep(1000, 1200)
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            winsound.Beep(1000, 1500)
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
