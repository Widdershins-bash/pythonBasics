from turtle import Turtle, Screen
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__(visible = False)
        self.penup()
        self.goto(0, screen_height / 2 - 50)
        self.level = 0
        self.keep_score()

    def next_level(self):
        self.level += 1
        self.keep_score()

    def keep_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level + 1}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 100)
        self.write(arg="GAME OVER", align="center", font=("Courier", 24, "bold"))
        time.sleep(1)
        replay = Screen().textinput(title="play agan?", prompt="yes or no").lower()
        if replay == "yes":
            return False
        else:
            return True