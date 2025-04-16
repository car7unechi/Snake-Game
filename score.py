from turtle import Turtle
class Score:
    def __init__(self):
        super().__init__()
        self.t = Turtle()
        self.t.color("white")
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(0, 270)
        self.t.write("Score: 0", align="center", font=("Times", 16, "normal"))
        self.score = 0

    def update_score(self):
        self.t.clear()
        self.score += 1
        self.t.write(f"Score: {self.score}", align="center", font=("Times", 16, "normal"))
    
    def game_over(self):
        self.t.goto(0, 0)
        self.t.write("GAME OVER", align="center", font=("Times", 32, "normal"))