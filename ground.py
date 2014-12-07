__author__ = 'jrootham'

import fns

WIDTH = .25
HEIGHT = .25

class Ground:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def connect(self):
        return (self.x + .125, self.y)

    def draw(self, canvas):
        canvas.create_line(fns.inch(self.x + WIDTH / 2), fns.inch(self.y),
                           fns.inch(self.x + WIDTH / 2), fns.inch(self.y + HEIGHT / 4))

        left = self.x
        right = self.x + WIDTH
        y = self.y + HEIGHT / 4
        canvas.create_line(fns.inch(left), fns.inch(y), fns.inch(right), fns.inch(y), width = 2)

        left = self.x + WIDTH * 1 / 6
        right = self.x + WIDTH * 5 /6
        y = self.y + HEIGHT / 4 + HEIGHT / 8
        canvas.create_line(fns.inch(left), fns.inch(y), fns.inch(right), fns.inch(y), width = 2)

        left = self.x + WIDTH * 2 / 6
        right = self.x + WIDTH * 4 / 6
        y = self.y + (HEIGHT / 4) + (HEIGHT / 4)
        canvas.create_line(fns.inch(left), fns.inch(y), fns.inch(right), fns.inch(y), width = 2)
