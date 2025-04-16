from turtle import Turtle
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.turts = []
        self.snake_body()
        self.head = self.turts[0]
        
        
    def snake_body(self):
        for i in self.starting_position:
            self.add_segment(i)

    def add_segment(self, i):
        new_piece = Turtle("square")
        new_piece.color("white")
        new_piece.penup()
        new_piece.goto(i)
        self.turts.append(new_piece)

    def extend(self):
        self.add_segment(self.turts[-1].position())
    
    def move(self):
        for i in range(len(self.turts) - 1, 0, -1):
            new_x = self.turts[i - 1].xcor()
            new_y = self.turts[i - 1].ycor()
            self.turts[i].goto(new_x, new_y)
        return self.turts[0].forward(15)

    def move_left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(RIGHT)
    def move_up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)
    
    