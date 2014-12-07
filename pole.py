__author__ = 'jrootham'

import fns

class Pole:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.left = self.x
        self.middle = self.x + .25
        self.right = self.x + .5

        self.top = self.y
        self.top_pole = self.y + .25
        self.bottom_cross = self.y + .5
        self.bottom_pole = self.y + 2

    def left_point(self):
        return (self.left, self.top)

    def right_point(self):
        return (self.right, self.bottom_cross)

    def draw(self, canvas):

        canvas.create_line(fns.inch(self.left), fns.inch(self.top),
                           fns.inch(self.right), fns.inch(self.bottom_cross), width=3)
        canvas.create_line(fns.inch(self.middle), fns.inch(self.top_pole),
                           fns.inch(self.middle), fns.inch(self.bottom_pole), width=5)
