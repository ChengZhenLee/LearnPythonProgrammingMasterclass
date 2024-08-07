try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

import math


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


# Modify the circle function so that it allows the colour of the
# circle to be specified and defaults to red if a colour is not given.
# You may want to review the previous lectures about named parameters
# and default values.
def circle(page, radius, g, h, colour="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width = 2)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    # This is to determine the edge of the axes
    # as opposed to the "origin" (0, 0)
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    # Sets the axis values
    # Note that in Tkinter, the y-axis is negative from the top and 
    # increases downwards, as opposed to normal axes in math
    # scrollregion units are in PIXELS
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    # print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -(y + 1), fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
# canvas2.grid(row=0, column=1)

# print(repr(canvas), repr(canvas2))
draw_axes(canvas)
# draw_axes(canvas2)

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()