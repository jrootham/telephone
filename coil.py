__author__ = 'jrootham'

import Tkinter as tk
import fns

DEPTH = .25
COUNT = 4
WIDTH = DEPTH / 2
HEIGHT = COUNT * DEPTH

class Coil:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def top(self):
        return (self.x, self.y)

    def bottom(self):
        return (self.x, self.y + HEIGHT)

    def draw(self, canvas):
        start = 90 if self.dir else 270
        left = self.x - WIDTH
        right = self.x + WIDTH

        for i in range(0, COUNT):
            top = self.y + i * DEPTH
            bottom = top + DEPTH
            canvas.create_arc(fns.inch(left), fns.inch(top), fns.inch(right), fns.inch(bottom),
                              style = tk.ARC, start = start, extent = 180)
