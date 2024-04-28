from turtle import Turtle

CORDINATES = [(350, 0), (-350 , 0)]


class Paddle:

    def __init__(self):
        self.pad = []
        self.make_paddle()
        self.f_pad = self.pad[0]
        self.l_pad = self.pad[1]

    def make_paddle(self):
        for cor in CORDINATES:
            self.paddl(cor)

    def paddl(self, cor):
        pl = Turtle()
        pl.shape("square")
        pl.color("white")
        pl.left(90)
        pl.penup()
        pl.goto(cor)
        pl.shapesize(1, 5)
        self.pad.append(pl)

    def up(self):
        self.f_pad.forward(20)

    def down(self):
        self.f_pad.backward(20)

    def upp(self):
        self.l_pad.forward(20)

    def downn(self):
        self.l_pad.backward(20)


