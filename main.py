from turtle import Turtle, Screen
import time
import random
from Snake import Snake
import food
from score import Score

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.listen()
my_screen.tracer()
fred = Snake()
food = food.Food()
my_screen.title("Snake Game")
score = Score()


my_screen.onkeypress(fun=fred.move_up, key="Up")
my_screen.onkeypress(fun=fred.move_down, key="Down")
my_screen.onkeypress(fun=fred.move_left, key="Left")
my_screen.onkeypress(fun=fred.move_right, key="Right")


game_on = True
while game_on:
    my_screen.update()
    time.sleep(.1)
    fred.move()

    if fred.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        fred.extend()

    if fred.head.xcor() > 280 or fred.head.xcor() < -280 or fred.head.ycor() > 280 or fred.head.ycor() < -280:
        game_on = False
        score.game_over()

    for i in fred.turts[1:]:
        if fred.head.distance(i) < 10:
            game_on = False
            score.game_over()














my_screen.exitonclick()