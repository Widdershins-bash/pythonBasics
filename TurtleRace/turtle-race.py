from turtle import Turtle as t, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
pen = t(visible=False)
pen.penup()
pen.goto(-200, 0)


def set_start_pos(list_of_turtles):
    x = -230
    y = round(len(list_of_turtles)/2) * -30
    for turtle in list_of_turtles:
        turtle.penup()
        turtle.goto(x, y)
        y += 30

def create_racers(racer_amount):
    turtles = []
    turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for racer in range(racer_amount):
        new_turtle = t(shape="turtle")
        new_turtle.color(turtle_colors[racer % len(turtle_colors)])
        turtles.append(new_turtle)

    return turtles
    
is_race_on = False
racer_amount = int(screen.textinput(title="Turtles participating", prompt="How many turtles should participate? (2-15): "))

while not is_race_on:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a number: ")
    if user_bet:
        is_race_on = True


turtles = create_racers(racer_amount)
set_start_pos(turtles)
        
while is_race_on:
    for i in range(len(turtles)):
        turtles[i].forward(random.randint(1, 10))
        if turtles[i].xcor() > 230:
            is_race_on = False
            if i == user_bet:
                pen.write(f"Your turtle won!\nTurtle {i + 1} was the winner.", font=("Ariel", 20, "bold"))
    
            else:
                pen.write(f"Your turtle lost.\nTurtle {i + 1} was the winner.", font=("Ariel", 20, "bold"))
        

screen.exitonclick()
