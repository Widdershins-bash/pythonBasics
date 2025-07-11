from turtle import Turtle
import random
from player import MOVE_DISTANCE

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self, screen_width, screen_height):
        self.cars = {}
        self.release_timer = 0
        self.order_num = 0
        self.speed = STARTING_MOVE_DISTANCE
        self.spawn_cars(screen_width, screen_height)


    def create_cars(self, amount):
        used_numbers = []
        for _ in range(amount):

            #creats random a but different car id for every car
            while self.order_num in used_numbers:
                self.order_num = random.randint(0, amount)
            used_numbers.append(self.order_num)
            
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=(MOVE_DISTANCE /20))
            self.cars[self.order_num] = car 
        

    def spawn_cars(self, screen_width, screen_height):
        self.create_cars(round((screen_height -40) / MOVE_DISTANCE))
        y_start = (screen_height / -2) + (20 + MOVE_DISTANCE) 
        
        # sets a starting position for every car
        for car in self.cars:
            self.cars[car].goto(screen_width / 2 + 20, y_start)
            y_start += MOVE_DISTANCE


    def move_cars(self, screen_width, screen_height): 
        for car_id in self.cars:
            vehicle = self.cars[car_id]

            #checks for reaching the end of the screen
            if vehicle.xcor() < screen_width / -2:
                max_y = screen_height / 2
                min_y = (screen_height / -2) + (20 + MOVE_DISTANCE)
                
                vehicle.goto((screen_width / 2), round(random.randint(min_y, max_y) / MOVE_DISTANCE) * MOVE_DISTANCE)
            
            else:
                if round(self.release_timer) > car_id:
                    vehicle.backward(self.speed)  

        #determines when a car should go at the start of the game - creates randomness
        self.release_timer += .1


    def speed_up(self):
        self.speed += MOVE_INCREMENT
