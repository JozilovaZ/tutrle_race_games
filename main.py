
from turtle import Screen
from player import Player
from car_manager import CarManager
import time

screen=Screen()
screen.title("Tutrle Race Game")
screen.bgcolor("white")
screen.setup(600,600)
screen.tracer(0)
screen.listen()

player=Player()
car_manager=CarManager()

screen.onkeypress(player.move_up,"Up")
screen.onkeypress(player.move_down,"Down")




game_is_on=True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()
    if player.ycor()>280:
        player.begin()
    # if car_manager.all_cars[0].distance(player)<15:
    #     game_is_on=False










screen.exitonclick()


