from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("yellow")
        self.speed("fastest")
        self.respawn()


    def respawn(self):
        random_x = round(random.randint(-280, 280) / 20) * 20
        random_y = round(random.randint(-280, 280) / 20) * 20
        self.setheading(random.randint(0, 360))
        self.goto(random_x, random_y)