from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20
s = Screen()

class Snake:
    def __init__(self, length, color):
        self.starting_segments = length
        self.color = color
        self.snake_color = self.color
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]


    def create_snake(self):
        for i in range(self.starting_segments):
            self.add_segment(((i + 1) * -MOVE_DISTANCE, 0))

    def add_segment(self, position):
            segment = Turtle(shape="square")
            self.snake_color = (self.snake_color[0], self.snake_color[1], self.snake_color[2] - 5)
            segment.color(self.snake_color)
            segment.penup()
            segment.goto(position)
            self.snake_segments.append(segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def reset(self):
        time.sleep(1)
        for seg in self.snake_segments:
            seg.goto(2000, 2000)
        self.snake_segments.clear()
        self.snake_color = self.color
        self.create_snake()
        self.head = self.snake_segments[0]

    def move_snake(self):
        for seg_num in range(len(self.snake_segments) - 1, 0,-1):
            X = self.snake_segments[seg_num -1].xcor()
            Y = self.snake_segments[seg_num -1].ycor()
            self.snake_segments[seg_num].goto(X, Y)
        
        #temporary movement
        self.head.forward(MOVE_DISTANCE)

        s.onkey(self.up, "w")
        s.onkey(self.down, "s")
        s.onkey(self.left, "a")
        s.onkey(self.right, "d")
    
    def up(self):
        if not self.snake_segments[0].heading() == 270:
            self.head.setheading(90)
    
    def down(self):
        if not self.snake_segments[0].heading() == 90:
            self.head.setheading(270)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
