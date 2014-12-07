__author__ = 'jrootham'

import fns

class Line:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas):
        start_x, start_y = self.start
        end_x, end_y = self.end

