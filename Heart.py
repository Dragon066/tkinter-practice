import tkinter
import math
import numpy as np


window = tkinter.Tk()
window.title('Tkinter')
window.geometry('800x800')

c = tkinter.Canvas(width=800, height=800)
c.pack()

TIME = 20
CENTER = (400, 400)
DELTA = 0.1
R = 20
    
    
def get_x(l):
    x = 16 * math.sin(l) ** 3
    return x


def get_y(l):
    y = 13 * math.cos(l) - 5 * math.cos(2 * l) - 2 * math.cos(3 * l) - math.cos(4 * l) # формула
    return y


def main(l):
    x = get_x(l) * R + CENTER[0]
    y = CENTER[1] - get_y(l) * R
    
    x_next = get_x(l + DELTA) * R + CENTER[0]
    y_next = CENTER[1] - get_y(l + DELTA) * R
    
    c.create_polygon((CENTER[0], CENTER[1] - 5 * R), (x, y), (x_next, y_next), fill='red')
    c.create_line((x, y), (x_next, y_next), fill='black', width=4)
    
    l += DELTA
    
    if l < 2 * np.pi:
        window.after(TIME, lambda: main(l))        

main(0)
    
window.mainloop()
