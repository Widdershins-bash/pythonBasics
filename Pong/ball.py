from turtle import Turtle
from paddle import Paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

        self.x_speed = 3
        self.y_speed = 3
        
    def move(self):
        self.floor_colision()
        y_pos = self.ycor() + self.y_speed
        x_pos = self.xcor() + self.x_speed

        self.goto(x_pos, y_pos)

    def floor_colision(self):
        if self.ycor() > 285 - self.y_speed or self.ycor() < -280: 
            self.bounce("y")

    def hit_wall(self):
        if self.xcor() > 380 - self.y_speed or self.xcor() < -385:
            return True 
        else:
            return False

    def bounce(self, bounce_type):
        if bounce_type == "x":
            self.x_speed *= -1
        elif bounce_type == "y":
            self.y_speed *= -1



