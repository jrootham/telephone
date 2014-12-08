__author__ = 'jrootham'

import fns
import ground
import battery
import horn

WIDTH = 2.0
HEIGHT = 1.0
MIC_WIDTH = .25

class Mic:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        if dir:
            ground_pos = 0
            battery_pos = self.x + (WIDTH / 2 - battery.WIDTH) - MIC_WIDTH
        else:
            ground_pos = WIDTH - ground.WIDTH
            battery_pos = self.x + (WIDTH / 2) + MIC_WIDTH

        self.ground = ground.Ground(self.x + ground_pos, self.y + .5)
        self.battery = battery.Battery(battery_pos, self.y, dir)


    def draw(self, canvas):
        self.ground.draw(canvas)
        self.battery.draw(canvas)
        battery_connect = self.battery.left_connect() if self.dir else  self.battery.right_connect()
        other_connect = self.battery.left_connect() if not self.dir else  self.battery.right_connect()
        fns.up_down(canvas, self.ground.connect(), battery_connect)

        left = self.x + ((WIDTH / 2) - (MIC_WIDTH / 2))
        top = self.y + HEIGHT / 3
        right = self.x + ((WIDTH / 2) + (MIC_WIDTH / 2))
        bottom = self.y + ( 2 * (HEIGHT / 3))

        canvas.create_rectangle(fns.inch(left), fns.inch(top), fns.inch(right), fns.inch(bottom),
            fill='black', stipple = 'gray50')

        middle = (top + bottom) / 2
        the_horn = horn.Horn(left, middle - horn.HEIGHT / 2, self.dir)
        the_horn.draw(canvas)
        fns.sideways(canvas, other_connect, ((left + (right-left) / 2), top))
        fns.up_down(canvas, ((left + (right-left) / 2), bottom), self.connect())

    def connect(self):
        result = 0

        if (self.dir):
            result = (self.x + 2, self.y + 1)
        else:
            result = (self.x, self.y + 1)

        return result