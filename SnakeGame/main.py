from turtle import Screen
import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

GAME_IS_ON = True

screen = Screen()
screen.clear()
turtle.colormode(255)
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()


snake = Snake(3, (255, 255, 255))
food = Food()
scoreboard = Scoreboard()

while GAME_IS_ON:

    screen.update()
    time.sleep(.1)
    snake.move_snake()


    #detect food collision
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.extend()
        scoreboard.increase_score(1)

    #detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect tail collision
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    