from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,cordinates):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(cordinates)
        self.hideturtle()
        self.create_score1()
        self.create_score2()


    def create_score1(self):
        self.write(arg= self.score1, align="center", font=('Courier', 80, 'normal'))

    def create_score2(self):
        self.write(arg= self.score2 , align="center", font=('Courier', 80, 'normal'))
    def refresh_score1(self):
        self.clear()
        self.score1 += 1
        self.create_score1()

    def refresh_score2(self):
        self.clear()
        self.score2 += 1
        self.create_score2()
