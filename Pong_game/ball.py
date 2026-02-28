from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.setheading(0)
        self.goto(0, 0)
        self.speed('fastest')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.06

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def reset_the_position(self):
        self.goto(0, 0)
        self.move_speed = 0.06
        self.x_move *= -1
        self.y_move = random.choice([-10, 10])