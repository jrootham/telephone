__author__ = 'jrootham'

import fns
import ground
import battery
import horn

WIDTH = 2
HEIGHT = 1
MIC_WIDTH = .25

class Mic:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        if dir:
            ground_pos = 0
            battery_pos = self.x + (WIDTH / 2) - battery.WIDTH
        else:
            ground_pos = WIDTH - ground.WIDTH
            battery_pos = self.x + (WIDTH / 2) + battery.WIDTH

        self.ground = ground.Ground(self.x + ground_pos, self.y + .5)
        self.battery = battery.Battery(battery_pos, self.y, dir)
  #      self.horn = horn.Horn()


    def draw(self, canvas):
        self.ground.draw(canvas)
        self.battery.draw(canvas)
        battery_connect = self.battery.left_connect() if self.dir else  self.battery.right_connect()
        fns.up_down(canvas, self.ground.connect(), battery_connect)

        print(
            fns.inch((self.x + ((WIDTH / 2) - (MIC_WIDTH / 2)))),
            fns.inch(self.y + HEIGHT / 3),
            fns.inch((self.x + ((WIDTH / 2) + (MIC_WIDTH / 2)))),
            fns.inch(self.y + ( 2 * (HEIGHT / 3))))

        canvas.create_rectangle(
            fns.inch((self.x + ((WIDTH / 2) - (MIC_WIDTH / 2)))),
            fns.inch(self.y + HEIGHT / 3),
            fns.inch((self.x + ((WIDTH / 2) + (MIC_WIDTH / 2)))),
            fns.inch(self.y + ( 2 * (HEIGHT / 3))),
            fill='black', stipple = 'gray50')


    def connect(self):
        result = 0

        if (self.dir):
            result = (self.x + 2, self.y + 1)
        else:
            result = (self.x, self.y + 1)

        return result