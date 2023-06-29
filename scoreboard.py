import turtle
from turtle import Turtle
ALIGN = "center"
FONT =  ("courier", 20, "bold")
class Scoreboard(Turtle):
    def __init__(self,color):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.score_board()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_board()

