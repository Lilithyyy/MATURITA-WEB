from random import *
from math import *
import tkinter

canvas = tkinter.Canvas(width=500, height=500, bg='white')
canvas.pack()

N = 4
r = 20
zx, zy = r, r
dx, dy = 2, 0
kruhy = []

def stlac(event):
    global dx, dy
    if event.char == 'w':
        dx, dy = 0, -2
    elif event.char == 's':
        dx, dy = 0, 2
    elif event.char == 'a':
        dx, dy = -2, 0
    elif event.char == 'd':
        dx, dy = 2, 0

def run():
    global zx, zy
    
    zx += dx
    zy += dy
    canvas.move(zrut, dx, dy)

    # kontrola zjedenia jabĺčka
    for i in range(len(kruhy)-1, -1, -1):
        if hypot(kruhy[i][0] - zx, kruhy[i][1] - zy) <= 2*r:
            canvas.delete(kruhy[i][2])
            kruhy.pop(i)

    # ak sú všetky zjedené
    if len(kruhy) == 0:
        canvas.create_text(250, 250,
                           text='Všetky jabĺčka sú zjedené!',
                           font='Arial 30')
    else:
        canvas.after(50, run)

zrut = canvas.create_oval(zx-r, zy-r, zx+r, zy+r,
                          width=0, fill='blue')

for i in range(N):
    while True:
        x = randint(r, 500-r)
        y = randint(r, 500-r)

        if hypot(x - zx, y - zy) > 2*r:
            break

    kruhy.append((x, y,
        canvas.create_oval(x-r, y-r, x+r, y+r,
                           width=0, fill='red')))

canvas.focus_set()
canvas.bind('<Key>', stlac)

canvas.after(10, run)
canvas.mainloop()
