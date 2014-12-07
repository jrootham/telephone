__author__ = 'jrootham'

import Tkinter as tk
import fns

WIDTH = .5
HEIGHT = .5
HALF = .4

class Horn:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir


    def draw(self, canvas):
        if dir:
            x_start = self.x - HALF
            x_end = self.x + HALF
            y_start_top = self.y - HALF
            y_end_top = self.y + HALF
            start_top = 270
        else:
            x_start = self.x (WIDTH - HALF)
            x_end = self.x + (WIDTH + HALF)
            y_start_top = self.y - HALF
            y_end_top = self.y + HALF
            start_top = 180

        canvas.create_arc(fns.inch(x_start), fns.inch(y_start_top),
                          fns.inch(x_end), fns.inch(y_end_top),
                          style = tk.ARC, start = start_top, extent = 90)

