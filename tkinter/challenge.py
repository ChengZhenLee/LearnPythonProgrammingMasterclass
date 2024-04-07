# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindowPadding = 8

# Create the window
mainWindow.title("Calculator")
mainWindow.geometry("480x500")
mainWindow['padx'] = 10

# Create the result field
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

# Button dictionary
buttonDict = {'C': (0, 0), 'CE': (0, 1),
              '7': (1, 0), '8': (1, 1), '9': (1, 2), '+': (1, 3),
              '6': (2, 0), '5': (2, 1), '4': (2, 2), '-': (2, 3),
              '3': (3, 0), '2': (3, 1), '1': (3, 2), '*': (3, 3),
              '0': (4, 0), '/': (4, 3)}

# Create the frame to store the buttons
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

# Create the buttons
for button in buttonDict:
    tkinter.Button(keyPad, text=button).grid(row=buttonDict[button][0], column=buttonDict[button][1], sticky='nsew')
tkinter.Button(keyPad, text='=').grid(row=4, column=1, columnspan=2, sticky='nsew')

# Any pending events are processed before entering the main loop.
# i.e. drawing the widgets, such that the width and height info
# exists, so that it can be used in the minsize and maxsize calls.
mainWindow.update()
# Set the maximum and minimum size of the window
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, keyPad.winfo_height() + result.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + mainWindowPadding + 100, result.winfo_height() + keyPad.winfo_height() + 100)

mainWindow.mainloop()