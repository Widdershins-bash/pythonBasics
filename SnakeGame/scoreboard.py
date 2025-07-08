from turtle import Turtle

FONT = ("Mighty Souly", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.increase_score(0)

    def increase_score(self, score_increase):
        self.score += score_increase
        
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)