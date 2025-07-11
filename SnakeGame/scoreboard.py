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
        self.highscore = 0
        with open("Day20-21\SnakeGame\highscore.txt", mode="r") as file_h:
            self.highscore = int(file_h.read())

        
        self.increase_score(0)

    def increase_score(self, score_increase):
        self.score += score_increase
        
        self.clear()
        self.write(arg=f"Score: {self.score}    High Score: {self.highscore}", align="center", font=FONT)


    def reset(self):
        if self.score > self.highscore:
            with open("Day20-21\SnakeGame\highscore.txt", mode="w") as file_h:
                file_h.write(str(self.score)) 
            self.highscore = self.score
        self.score = 0
        self.increase_score(0)