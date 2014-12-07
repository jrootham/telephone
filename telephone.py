__author__ = 'jrootham'

from Tkinter import *
import pole
import line

class Telephone:

    def __init__(self):
        self.poleList = [pole.Pole(2, 2), pole.Pole(3.5, 2), pole.Pole(5, 2)]
        self.lineList = []
        self.lineList.append(line.Line(self.poleList[0].left_point(), self.poleList[1].left_point()))


    def draw(self, canvas):
        canvas.create_text('3i', '.25i', font = ('Helvetica', '20'), text='Telephone schematic - telephone.py')
        for pole in self.poleList:
            pole.draw(canvas)

root = Tk()
canvas = Canvas(bg='white', width = '7.5i', height = '7.5i')
canvas.pack()

t = Telephone()

t.draw(canvas)

canvas.update()
canvas.postscript(file = "telephone.ps")

root.mainloop()