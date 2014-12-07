__author__ = 'jrootham'

WIDTH = 2
HEIGHT = 1

class Ear:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def draw(self, canvas):
        pass

    def connect(self):
        result = 0

        if (self.dir):
            result = (self.x + 2, self.y)
        else:
            result = (self.x, self.y)

        return result