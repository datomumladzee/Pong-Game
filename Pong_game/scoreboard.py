from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()

        self.draw_center_line()
        self.update_scoreboard()

    def draw_center_line(self):
        self.goto(0, 300)
        self.setheading(270)

        for i in range(20):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)

        self.penup()

    def update_scoreboard(self):
        self.clear()
        self.draw_center_line()

        self.goto(70, 240)
        self.write(f"{self.r_score}", align="center",font=("Courier", 35, "bold"))

        self.goto(-70, 240)
        self.write(f"{self.l_score}", align="center",font=("Courier", 35, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()