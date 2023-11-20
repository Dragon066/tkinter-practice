import tkinter
import math
from random import randint

window = tkinter.Tk()
window.title('Tkinter')
window.geometry('800x800')

c = tkinter.Canvas(width=800, height=800)

colors_available = ['#{:02X}{:02X}{:02X}'.format(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(50)]

R = 1
r = 10
center = (400, 400)
N = 20
colors = []
circles = []
angleold = 138

angle_slider = tkinter.Scale(window, from_=0, to=360, orient='horizontal', label="Угол между кругами", length=360)
angle_slider.set(138)  
angle_slider.pack()

for i in range(N):
    circles.append([])

def move(l, R, n, angle):
    global circles
    global colors
    phi = [l + angle * i for i in range(N)]
    colors.append(colors_available[((n+50)//7) % 50])
    if len(circles[0]) > 54:
        return
    for i in range(N):
        l = phi[i]
        circles[i].append(c.create_oval(R * math.cos(l * math.pi / 180) + center[0], R * math.sin(l * math.pi / 180) + center[1], R * math.cos(l * math.pi / 180) + center[1] + 2 * r, R * math.sin(l * math.pi / 180) + center[1] + 2 * r, fill='white'))
        c.pack()

def clear_canvas():
    global circles
    global colors
    for circle_list in circles:
        for circle_id in circle_list:
            c.delete(circle_id)
    circles = []
    for i in range(N):
        circles.append([])
    colors.clear()

def change_color(n):
    global colors
    for i in range(len(circles[0])):
        for j in range(N):
            c.itemconfig(circles[j][i], fill=colors[i])
    colors = colors[1:] + [colors[0]] if colors else []

def main(l, R, color):
    global angleold
    global colors_available
    angle = angle_slider.get()
    if angle != angleold:
        clear_canvas()
        colors_available = ['#{:02X}{:02X}{:02X}'.format(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(50)]
        angleold = angle
        l=0
        R=1
        color=0
    move(l, R, color, angle)
    change_color(color)
    l += 1300 / R
    R += 5
    color += 1
    window.after(10, lambda: main(l, R, color))

main(0, R, 0)
    
window.mainloop()
