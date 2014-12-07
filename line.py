__author__ = 'jrootham'

import Tkinter as tk
import fns

class Line:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas):
        start_x, start_y = self.start
        end_x, end_y = self.end

        delta = end_x - start_x
        top_y = start_y - delta / 7.5
        botttom_y = start_y + delta / 7.5

        canvas.create_arc(fns.inch(start_x), fns.inch(top_y), fns.inch(end_x), fns.inch(botttom_y),
                          style = tk.ARC, start= 180, extent = 180)
