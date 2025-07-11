from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()   
scoreboard = Scoreboard()

ball_query = "left"
winner = ""
power = True
while power:
    time.sleep(.01)
    screen.update()
    ball.move()
    l_paddle.move("w", "s", 5)
    r_paddle.move("Up", "Down", 5)

    #detect paddle collision
    if (ball.xcor() > r_paddle.xcor() - 20 and ball.distance(r_paddle) < 55) or (ball.xcor() < l_paddle.xcor() + 20 and ball.distance(l_paddle) < 55): 
        if ball.xcor() > 0 and  ball_query != "right":
                ball.bounce("x")
                ball_query = "right"
                
        
        elif ball.xcor() < 0 and ball_query != "left":
                ball.bounce("x")
                ball_query = "left"
                

        
    #detect point collision
    if ball.hit_wall():    
        if ball.xcor() > 0:
            ball_query = "right"
            ball.y_speed += .5
            ball.x_speed += .5
            scoreboard.add_score(1, 1)
        elif ball.xcor() < 0:
            ball_query = "left"        
            ball.y_speed -= .5
            ball.x_speed -= .5
            scoreboard.add_score(2, 1)
        
        power = scoreboard.did_win()
        if power:
            ball.home()        
            ball.bounce("x")


scoreboard.display_winner()
screen.exitonclick()
