# Instructions for the game:
# 1. Use the left and right arrow keys to move the turtle.
# 2. The goal is to catch the falling shapes (circles) with the turtle.
# 3. Each shape caught increases your score by 10 points.
# 4. The game ends when you miss 5 shapes.

import turtle
import random

# Setup the screen
wn = turtle.Screen()
wn.title("Catch the Falling Shapes Game")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turn off screen updates for better performance

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.goto(0, -250)

# Create a list to store falling shapes
shapes = []
shape_colors = ["red", "blue", "yellow", "purple", "orange"]

# Function to create a new falling shape
def create_shape():
    shape = turtle.Turtle()
    shape.shape("circle")
    shape.color(random.choice(shape_colors))
    shape.penup()
    shape.speed(0)
    shape.goto(random.randint(-290, 290), 300)
    return shape

# Create initial shapes
for _ in range(5):
    shapes.append(create_shape())

# Function to move the player turtle
def move_left():
    x = player.xcor()
    x -= 20
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 290:
        x = 290
    player.setx(x)

# Keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Speed of falling shapes
fall_speed = 0.5  # Adjust this value to make shapes fall slower or faster

# Score and miss variables
score = 0
misses = 0

# Main game loop
while True:
    wn.update()

    for shape in shapes:
        shape.sety(shape.ycor() - fall_speed)

        # Check if shape has fallen below the screen
        if shape.ycor() < -300:
            shape.hideturtle()
            shapes.remove(shape)
            misses += 1
            if misses >= 10:  # Game over condition
                print("Game Over! Your final score:", score)
                turtle.bye()
                exit()
        # Check if shape has been caught by the player
        if shape.ycor() < -230 and (shape.xcor() > player.xcor() - 50 and shape.xcor() < player.xcor() + 50):
            shape.hideturtle()
            shapes.remove(shape)
            score += 10
            print(f"Score: {score}")

    # Add new shapes if there are fewer than 5
    if len(shapes) < 5:
        shapes.append(create_shape())
