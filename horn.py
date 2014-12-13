__author__ = 'jrootham'

import Tkinter as tk
import fns

ARC_WIDTH = .2
SPACE = .05
HEIGHT = 2 * (ARC_WIDTH + SPACE)

class Horn:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir


    def draw(self, canvas):
        x_start = self.x - ARC_WIDTH
        x_end = self.x + ARC_WIDTH
        y_start_top = self.y - (SPACE + 2 * ARC_WIDTH)
        y_end_top = self.y - SPACE
        y_start_bottom = self.y + SPACE
        y_end_bottom = self.y + (SPACE + 2 * ARC_WIDTH)

        if self.dir:
            start_top = 180
            start_bottom = 90
        else:
            start_top = 270
            start_bottom = 0

        canvas.create_arc(fns.inch(x_start), fns.inch(y_start_top),
                          fns.inch(x_end), fns.inch(y_end_top),
                          style = tk.ARC, start = start_top, extent = 90, width = 2)

        canvas.create_arc(fns.inch(x_start), fns.inch(y_start_bottom),
                          fns.inch(x_end), fns.inch(y_end_bottom),
                          style = tk.ARC, start = start_bottom, extent = 90, width = 2)

