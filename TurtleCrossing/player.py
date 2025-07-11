from turtle import Turtle


MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, screen_height):
        super().__init__(shape="turtle")
        self.starting_position = (0, screen_height / -2 + 20)
        self.setheading(90)
        self.penup()
        self.goto(self.starting_position)

    def move_up(self):
        y_pos = self.ycor() + MOVE_DISTANCE
        self.sety(y_pos)


    
