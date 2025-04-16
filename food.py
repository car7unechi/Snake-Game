from turtle import Turtle
import  random

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(x=ran_x, y=ran_y)
        
    def refresh(self):
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(x=ran_x, y=ran_y)