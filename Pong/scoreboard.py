from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.winner = ""
        self.write_score()
        
    def add_score(self, player, amount):
        if player == 1:
            self.l_score += amount
        
        elif player == 2:
            self.r_score += amount

        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 230)
        self.write(arg=f"{self.l_score}    {self.r_score}", align="center", font=("Mighty Souly", 40, "normal"))

    def did_win(self):
        if self.l_score == 7: 
            self.winner = "Left Player"
            power = False

        elif self.r_score == 7:
            self.winner = "Right Player"
            power = False
        else:
            power = True

        return power
    
    def display_winner(self):
        self.goto(0, 0)
        self.write(arg=f"{self.winner} wins!", align="center", font=("Mighty Souly", 40, "normal"))

        