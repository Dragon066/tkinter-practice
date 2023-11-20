import tkinter
import math
import numpy as np


window = tkinter.Tk()
window.title('Tkinter')
window.geometry('800x800')

c = tkinter.Canvas(width=800, height=800)
c.pack()

TIME = 10
a = 300
DELTA = 0.01
CENTER = (400, 400)
d = 4
    
    
def get_x(l, k):
    r = a * math.sin(k * l)
    return r * math.cos(l) + CENTER[0]


def get_y(l, k):
    r = a * math.sin(k * l)
    return r * math.sin(l) + CENTER[1]


def main(k):
    c.delete('all')
    
    phi = np.linspace(0, d * np.pi, 1000)
    
    lst = [(get_x(i, k), get_y(i, k)) for i in phi]
    
    c.create_line(*lst, smooth=True)
    
    k += DELTA
    window.after(TIME, lambda: main(k))


main(0)
    
window.mainloop()
