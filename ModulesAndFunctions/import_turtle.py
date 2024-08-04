# import turtle

# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()

from turtle import *
from math import radians, cos


def square(length: int) -> None:
    """Draws a square of length `length`"""
    # So python only has to look up in the global namespace once
    inner_forward = forward
    inner_right = right
    for side in range(4):
        inner_forward(length)
        inner_right(90)


def encircled_square(length: int) -> None:
    """
    Draws a square of length `length`,
    then encloses it in a circle
    """
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    right(135)
    circle(radius)
    left(135)
    print(f'Inside function, namespace is : {dir()}')
    print(f'locals: {locals()}')


# encircled_square(300)
speed('fast')
Screen().tracer(0)  # disable the turtle animation

for s in range(72):
    encircled_square(120)
    left(5)

Screen().update()   # update the screen
done()

print(dir())
g = globals()
print(g['square'])

print(dir(__builtins__))