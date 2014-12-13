__author__ = 'jrootham'

import fns

WIDTH = .25
HEIGHT = .25

class Ground:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def connect(self):
        return (self.x, self.y)

    def draw(self, canvas):
        canvas.create_line(fns.inch(self.x), fns.inch(self.y),
                           fns.inch(self.x), fns.inch(self.y + HEIGHT / 4))

        left = self.x - WIDTH / 2
        right = self.x + WIDTH /2
        y = self.y + HEIGHT / 4
        canvas.create_line(fns.inch(left), fns.inch(y), fns.inch(right), fns.inch(y), width = 2)

        left = self.x - WIDTH * 1 / 3
        right = self.x + WIDTH * 1 / 3
        y = self.y + HEIGHT / 4 + HEIGHT / 8
        canvas.create_line(fns.inch(left), fns.inch(y), fns.inch(right), fns.inch(y), width = 2)

        left = self.x - WIDTH * 1 / 6
        right = self.x + WIDTH * 1 / 6
        y = self.y + (HEIGHT / 4) + (HEIGHT / 4)
        canvas.create_line(fns.inch(left), fns.inch(y), fns.inch(right), fns.inch(y), width = 2)
