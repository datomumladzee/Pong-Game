from turtle import Turtle

class Menu(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.game_mode = None

    def show(self):
        self.write(
            "PONG GAME\n\nPress 1 for Single Player\nPress 2 for Two Players",
            align="center",
            font=("Courier", 24, "bold")
        )

    def choose_ai(self):
        self.game_mode = "AI"

    def choose_2p(self):
        self.game_mode = "2P"

    def clear_menu(self):
        self.clear()