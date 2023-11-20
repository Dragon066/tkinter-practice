import tkinter
import time
import math


window = tkinter.Tk()
window.title('Tkinter')
window.geometry('600x600')

c = tkinter.Canvas(width=600, height=600)


speed = 1.0
reverse = 1
R = 200
r = 10
center = (300, 300)


main_circle = c.create_oval(center[0] - R + r, center[0] - R + r, center[1] + R + r, center[1] + R + r, outline='red')
circle = c.create_oval(0, 0, 2 * r, 2 * r, fill='white', outline='blue')
c.pack()


def speedup(s):
    global speed
    speed += s
    speed = round(max(0, speed), 1)
    label.config(text=speed)


def to_reverse():
    global reverse
    reverse *= -1
    b3.config(bg=('lightgreen' if reverse < 0 else 'lightgrey'))
    
    
b1 = tkinter.Button(window, text='Faster', command=lambda: speedup(0.1))
b1.pack()
b1.place(x=105, y=5)

b2 = tkinter.Button(window, text='Slower', command=lambda: speedup(-0.1))
b2.pack()
b2.place(x=10, y=5)

b3 = tkinter.Button(window, text='Reverse!', bg='lightgrey', command=to_reverse)
b3.pack()
b3.place(x=520, y=5)

label = tkinter.Label(window, text=speed)
label.pack()
label.place(x=70, y=8)


def move(l):
    if speed != 0:
        c.moveto(circle, R * math.cos(l * math.pi / 180) + center[0], R * math.sin(l * math.pi / 180) + center[1])


def main(l):
    move(l)
    l += reverse * speed
    window.after(10, lambda: main(l))


main(0)
    
window.mainloop()

