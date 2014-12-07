__author__ = 'jrootham'

def inch(n):
    return str(n) + 'i'

def line(canvas, start, end):
    start_x, start_y = start
    end_x, end_y = end

    canvas.create_line(inch(start_x), inch(start_y), inch(end_x), inch(end_y))

def up_down(canvas, start, end):
    start_x, start_y = start
    end_x, end_y = end

    line(canvas, start, (start_x, end_y))
    line(canvas, (start_x, end_y), end)

def sideways(canvas, start, end):
    start_x, start_y = start
    end_x, end_y = end

    line(canvas, start, (end_x, start_y))
    line(canvas, (end_x, start_y), end)

