__author__ = 'jrootham'

import fns
import ground
import battery
import horn
import sound

WIDTH = 2.0
HEIGHT = 2.0
MIC_WIDTH = .25
OFFSET = .5

class Mic:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        if dir:
            ground_pos = WIDTH - ground.WIDTH
            battery_pos = self.x + (WIDTH / 2)
        else:
            ground_pos = 0
            battery_pos = self.x + (WIDTH / 2 - battery.WIDTH) - MIC_WIDTH

        self.ground = ground.Ground(self.x + ground_pos, self.y + .5)
        self.battery = battery.Battery(battery_pos, self.y, dir)


    def draw(self, canvas):
        self.ground.draw(canvas)
        self.battery.draw(canvas)


        if self.dir:
            battery_connect = self.battery.right_connect()
            other_connect = self.battery.left_connect()

        else:
            battery_connect = self.battery.left_connect()
            other_connect = self.battery.right_connect()

        fns.up_down(canvas, self.ground.connect(), battery_connect)

        left = self.x + ((WIDTH / 2) - (MIC_WIDTH / 2))
        top = self.y + HEIGHT / 3
        right = self.x + ((WIDTH / 2) + (MIC_WIDTH / 2))
        bottom = self.y + ( 2 * (HEIGHT / 3))

        canvas.create_rectangle(fns.inch(left), fns.inch(top), fns.inch(right), fns.inch(bottom),
            fill='black', stipple = 'gray25')

        middle = top + (bottom - top) / 2

        if self.dir:
            place = left
        else:
            place = right

        mic_horn = horn.Horn(place, middle, self.dir)
        mic_horn.draw(canvas)

        small_sound = sound.Sound(place, middle, self.dir, sound.SMALL, OFFSET)
        large_sound = sound.Sound(place, middle, self.dir, sound.LARGE, OFFSET)

        small_sound.draw(canvas)
        large_sound.draw(canvas)

        fns.sideways(canvas, other_connect, ((left + (right-left) / 2), top))
        fns.up_down(canvas, ((left + (right-left) / 2), bottom), self.connect())

    def connect(self):
        result = 0

        if (self.dir):
            result = (self.x + WIDTH, self.y + HEIGHT   )
        else:
            result = (self.x, self.y + HEIGHT)

        return result