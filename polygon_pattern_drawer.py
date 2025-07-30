import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Polygon Pattern Drawer")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Colors to cycle through
colors = ["red", "yellow", "green", "cyan",
           "blue", "magenta", "orange", "white"]

# Get number of sides from the user
try:
    sides = screen.textinput("Polygon Pattern Drawer",
         "Enter number of sides (e.g. 5 for pentagon):")
    sides = int(sides)
    if sides < 3:
        raise ValueError("Polygon must have at least 3 sides.")
except:
    print("Invalid input! Defaulting to 5 sides.")
    sides = 5

# Angle between sides
angle = 360 / sides

# Draw the polygon pattern
for i in range(100):
    pen.color(colors[i % len(colors)])
    for _ in range(sides):
        pen.forward(100)
        pen.left(angle)
    pen.left(10)

# Finish
pen.hideturtle()
turtle.done()
