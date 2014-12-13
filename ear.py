__author__ = 'jrootham'

import coil
import horn
import ground
import sound
import fns

WIDTH = 2.0
HEIGHT = 2.0
OFFSET = .1
Y_COIL = .25
BAR_WIDTH = .05

class Ear:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        print(self.x, self.y,self.dir)

    def draw(self, canvas):
        pos = self.x + WIDTH *.75  if self.dir else self.x + WIDTH * .25

        electromagnet = coil.Coil(pos, self.y + Y_COIL, self.dir)
        electromagnet.draw(canvas)
        fns.up_down(canvas, electromagnet.top(), self.connect())

        (e_x, e_y) = electromagnet.bottom()
        earth = ground.Ground(e_x, e_y + .25)
        earth.draw(canvas)

        fns.up_down(canvas, electromagnet.bottom(), earth.connect())

        if self.dir:
            bar = e_x - (coil.WIDTH + OFFSET)
            edge = bar - BAR_WIDTH / 2
        else:
            bar = e_x + (coil.WIDTH + OFFSET)
            edge = bar + BAR_WIDTH / 2

        canvas.create_line(fns.inch(bar), fns.inch(self.y + Y_COIL), fns.inch(bar), fns.inch(e_y),
                           width = fns.inch(BAR_WIDTH))

        middle = (self.y + Y_COIL) + coil.HEIGHT / 2

        ear_horn = horn.Horn(edge, middle, self.dir)
        small_sound = sound.Sound(edge, middle, not self.dir, sound.SMALL, -.1)
        large_sound = sound.Sound(edge, middle, not self.dir, sound.LARGE, -.1)

        ear_horn.draw(canvas)
        small_sound.draw(canvas)
        large_sound.draw(canvas)

    def connect(self):
        result = 0

        if (self.dir):
            result = (self.x + 2, self.y)
        else:
            result = (self.x, self.y)

        return result