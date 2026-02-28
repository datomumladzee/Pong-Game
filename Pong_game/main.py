from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from menu import Menu


screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

#menu object
menu = Menu()
menu.show()

screen.listen()
screen.onkey(menu.choose_ai, "1")
screen.onkey(menu.choose_2p, "2")

# To choose the game mode
while menu.game_mode is None:
    screen.update()

menu.clear_menu()

#Two paddle objects, left and right
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#ball object
ball = Ball()
#scoreboard objects
score = Scoreboard()

#moving keys
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

if menu.game_mode == "2P":
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

game_is_on=True
while game_is_on:

    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    #if game is with AI
    if menu.game_mode == "AI":
        if l_paddle.ycor() < ball.ycor() - 15:
            l_paddle.sety(l_paddle.ycor() + 12)
        elif l_paddle.ycor() > ball.ycor() + 15:
            l_paddle.sety(l_paddle.ycor() - 12)

    #collision with the top walls, bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #collision with the side walls, restart the game and give ball to another player
    if ball.xcor()>390:
        ball.reset_the_position()
        score.l_point()
    if ball.xcor()<-390:
        ball.reset_the_position()
        score.r_point()

    #detect collision with paddle
    if 320 < ball.xcor() < 340 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
    if -340 < ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

screen.exitonclick()