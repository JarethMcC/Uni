import turtle
import random

#colors is used later to in conjunction with random to get a color for the square
#noSquares takes input for how many squares the program should create
colors = ['red', 'blue', 'green']
noSquares = int(input('How many squares would you like to see?: ')))

def main():
    turtle.hideturtle()
    for i in range(noSquares):
        square(random.randint(-200, 200), random.randint(-200, 200), random.randint(1, 200), random.choice(colors))
        #square(random.randint(-200, 200), random.randint(-200, 200), random.randint(1, 200), random.choice(colors))
        #square(random.randint(-200, 200), random.randint(-200, 200), random.randint(1, 200), random.choice(colors))

# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.

def square(x, y, width, color):
    turtle.penup()            # Raise the pen
    turtle.goto(x, y)         # Move to the specified location
    turtle.fillcolor(color)   # Set the fill color
    turtle.pendown()          # Lower the pen
    turtle.begin_fill()       # Start filling
    for count in range(4):    # Draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # End filling

# Call the main function.
main()
