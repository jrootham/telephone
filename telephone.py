__author__ = 'jrootham'

from Tkinter import *
import fns
import pole
import line
import mic
import ear

WIDTH = 7.5
HEIGHT = 7.5

class Telephone:

    def __init__(self):
        self.poleList = [pole.Pole(2.5, 2), pole.Pole(3.5, 2), pole.Pole(4.5, 2)]
        self.lineList = []
        self.lineList.append(line.Line(self.poleList[0].left_point(), self.poleList[1].left_point()))
        self.lineList.append(line.Line(self.poleList[1].left_point(), self.poleList[2].left_point()))
        self.lineList.append(line.Line(self.poleList[0].right_point(), self.poleList[1].right_point()))
        self.lineList.append(line.Line(self.poleList[1].right_point(), self.poleList[2].right_point()))
        self.left_mic = mic.Mic(0, 5, True)
        self.right_mic = mic.Mic(WIDTH - mic.WIDTH, 1.5, False)
        self.left_ear = ear.Ear(0, 1.5, True)
        self.right_ear = ear.Ear(WIDTH - ear.WIDTH, .5, False)


    def draw(self, canvas):
        canvas.create_text('3i', '.25i', font = ('Helvetica', '20'), text='Telephone schematic - telephone.py')
        for pole in self.poleList:
            pole.draw(canvas)

        for line in self.lineList:
            line.draw(canvas)

        self.left_mic.draw(canvas)
        self.right_mic.draw(canvas)
        self.left_ear.draw(canvas)
        self.right_ear.draw(canvas)

        fns.sideways(canvas, self.left_mic.connect(), self.poleList[0].right_point())
        fns.up_down(canvas, self.left_ear.connect(), self.poleList[0].left_point())

        fns.up_down(canvas, self.right_mic.connect(), self.poleList[2].right_point())
        fns.sideways(canvas, self.right_ear.connect(), self.poleList[2].left_point())

root = Tk()
canvas = Canvas(bg='white', width = '7.5i', height = '7.5i')
canvas.pack()

t = Telephone()

t.draw(canvas)

canvas.update()
canvas.postscript(file = "telephone.ps")

root.mainloop()