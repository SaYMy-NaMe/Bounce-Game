import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Bounce Game")
screen.bgcolor("black")
screen.setup(600, 600)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3  # ball's x velocity
ball.dy = -3  # ball's y velocity

# Create the paddle
paddle = turtle.Turtle()
paddle.penup()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.goto(0, -250)

# Function to move the paddle left
def move_left():
    x = paddle.xcor()
    x -= 20
    if x < -280:
        x = -280
    paddle.setx(x)

# Function to move the paddle right
def move_right():
    x = paddle.xcor()
    x += 20
    if x > 280:
        x = 280
    paddle.setx(x)

# Set up the keyboard bindings
screen.listen()
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collisions with the walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        screen.bye()  # Game over if ball hits bottom

    # Check for collision with the paddle
    if not (not (-240 > ball.ycor() > -250) or not (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50)):
        ball.dy *= -1  
