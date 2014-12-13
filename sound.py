__author__ = 'jrootham'

import Tkinter as tk
import fns

OFFSET = .5
SMALL = .2
LARGE = .3

class Sound:

    def __init__(self, x, y, dir, size, offset):
        self.x = x
        self.y = y
        self.dir = dir
        self.size = size
        self.offset = offset

    def draw(self, canvas):
        if self.dir:
            left_x = (self.x - self.offset) - self.size
            right_x = (self.x - self.offset) + self.size
        else:
            left_x = (self.x + self.offset) - self.size
            right_x = (self.x + self.offset) + self.size

        top_y = self.y - self.size
        bottom_y = self.y + self.size

        start = 315 if self.dir else 135

        canvas.create_arc(fns.inch(left_x), fns.inch(top_y), fns.inch(right_x), fns.inch(bottom_y),
                          style = tk.ARC, start = start, extent = 90)