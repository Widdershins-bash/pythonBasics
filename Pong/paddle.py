from turtle import Turtle, Screen as s

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.go_up = False
        self.go_down = False

    def go_up_true(self):
        self.go_up = True 


    def go_up_false(self):
        self.go_up = False

    def go_down_true(self):
        self.go_down = True      


    def go_down_false(self):
        self.go_down = False
       
    
    def move(self, input_up, input_down, move_speed):
        s().onkeypress(self.go_up_true, input_up)
        s().onkeyrelease(self.go_up_false, input_up)
        s().onkeypress(self.go_down_true, input_down)
        s().onkeyrelease(self.go_down_false, input_down) 
        if self.go_up:
            y_pos = self.ycor() + move_speed
            self.sety(y_pos)       
        
        elif self.go_down:
            y_pos = self.ycor() - move_speed
            self.sety(y_pos)