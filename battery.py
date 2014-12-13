__author__ = 'jrootham'

import fns

WIDTH = .5
HEIGHT = .25
HALF = WIDTH / 2
DELTA = WIDTH / 16

class Battery:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def left_connect(self):
        return (self.x, self.y + HEIGHT / 2)

    def right_connect(self):
        return (self.x + WIDTH, self.y + HEIGHT / 2)

    def draw(self, canvas):
        if (self.dir):
            short_delta = DELTA
            long_delta = -DELTA
        else:
            short_delta = -DELTA
            long_delta = DELTA

        long_x = self.x + HALF + long_delta
        short_x = self.x + HALF + short_delta
        canvas.create_line(fns.inch(long_x), fns.inch(self.y), fns.inch(long_x), fns.inch(self.y + HEIGHT))
        canvas.create_line(fns.inch(short_x), fns.inch(self.y + HEIGHT * 1 /4),
                           fns.inch(short_x), fns.inch(self.y + HEIGHT * 3 /4))
        canvas.create_line(fns.inch(self.x), fns.inch(self.y + HEIGHT / 2),
                           fns.inch(self.x + (HALF - DELTA)), fns.inch(self.y + HEIGHT / 2))
        canvas.create_line(fns.inch(self.x + WIDTH), fns.inch(self.y + HEIGHT / 2),
                           fns.inch(self.x + (HALF + DELTA)), fns.inch(self.y + HEIGHT / 2))

