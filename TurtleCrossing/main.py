#TODO 1.2: add a blinking effect upon new level
#TODO 2: maybe add some creative addons to cars

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

while True:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen_height = screen.window_height()
    screen_width = screen.window_width()
    screen.tracer(0)
    screen.listen()

    player = Player(screen_height)
    screen.onkeypress(player.move_up, "space")
    car_manager = CarManager(screen_width, screen_height)
    scoreboard = Scoreboard(screen_height)

    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.move_cars(screen_width, screen_height)

        for car in car_manager.cars:
            if player.distance(car_manager.cars[car]) < 20:
                game_is_on = False

        if player.ycor() > screen_height / 2:
            scoreboard.next_level()
            car_manager.speed_up()
            player.goto(player.starting_position)
            screen.update()
            time.sleep(1)

    #game over sequence
    screen.tracer(1)
    if scoreboard.game_over():
        exit()

    else:
        screen.clear()