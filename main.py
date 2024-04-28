from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoarboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 800 , height = 600)
screen.bgcolor("black")
screen.tracer(0)



pa = Paddle()
ba = Ball()
score1 = Scoreboard((100, 200))
score2 = Scoreboard((-100, 200))


screen.listen()
screen.onkeypress(pa.up,"Up")
screen.onkeypress(pa.down,"Down")
screen.onkeypress(pa.upp,"w")
screen.onkeypress(pa.downn,"s")



game_is_on = True

Time = 0.06
while game_is_on:
    time.sleep(Time)
    screen.update()
    ba.ball_move()
    if (ba.ycor() > 280 or ba.ycor() < -280):
        ba.bounce_y()

    if (ba.distance(pa.f_pad) < 50 and ba.xcor() > 320) or (ba.distance(pa.l_pad) < 50 and ba.xcor() < -320):
        ba.bounce_x()
        Time -= 0.001

    if(ba.xcor() > 380):
        ba.refactor_1()
        Time = 0.06
        score2.refresh_score2()


    if (ba.xcor() < -380):
        ba.refactor_2()
        Time = 0.06
        score1.refresh_score1()






























screen.exitonclick()