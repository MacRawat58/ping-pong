from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player1_score, align=ALIGNMENT, font=FONT)
        self.goto(0, 200)
        self.write(":", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.player2_score, align=ALIGNMENT, font=FONT)

    def increase_player1_score(self):
        self.player1_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_player2_score(self):
        self.player2_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):

        self.goto(0, 0)

        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
