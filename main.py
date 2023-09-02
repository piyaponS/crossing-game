import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    car.create_car()
    car.move()
    screen.update()

    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            screen.update()

    if player.ycor() > 300:
        player.restart()
        car.speed_up()
        scoreboard.level_up()

screen.exitonclick()

