""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""
# Change the Turtle Image

import turtle

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

# set_turtle_image(t, "leaguebot_bolt.gif")
t.shape("turtle")
t.penup()
t.speed(3)
t.turtlesize(stretch_wid=10, stretch_len=10, outline=1)

sides = 5
angles = 360/sides

for i in range(sides):
    t.forward(100)
    t.left(angles)


turtle.done()     



... # Your Code Here