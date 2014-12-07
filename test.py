__author__ = 'jrootham'

from Tkinter import *

root = Tk()
canvas = Canvas(bg='white', width = 200, height = 200)
canvas.pack()

canvas.create_line(0, 0, 199, 199, fill="black", width = 5)
canvas.create_line(0, 199, 199, 0, fill="black", width = 5)

canvas.update()
canvas.postscript(file = "x.ps")

root.mainloop()