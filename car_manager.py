from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.pre_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        num = random.randint(1, 7)
        if num == 4:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.pre_speed
            car.goto(new_x, car.ycor())

    def speed_up(self):
        self.pre_speed += MOVE_INCREMENT


    
