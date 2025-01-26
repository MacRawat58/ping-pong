from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from time import sleep


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)


soreboard = Scoreboard()
# Create the paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create the ball
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles and bounce
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect when the ball goes out of bounds
    if ball.xcor() > 380:
        soreboard.increase_player1_score()
    if ball.xcor() < -380:
        soreboard.increase_player2_score()

    # Detect when the game is over
    if soreboard.player1_score == 5 or soreboard.player2_score == 5:
        soreboard.game_over()
        game_is_on = False

    # Reset the ball position
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()

    # Bounce the ball when it goes out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()

screen.exitonclick()
