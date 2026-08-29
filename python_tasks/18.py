import tkinter

canvas = tkinter.Canvas(bg='white', width=400, height=400)
canvas.pack()

robotx, roboty, uhol = 200, 200, 0

def vykonaj(prikaz):
    global robotx, roboty, uhol
    casti = prikaz.split()
    if casti[0] == 'ciara':
        dlzka = int(casti[1])
        if uhol == 0:
            x, y = robotx, roboty - dlzka
        elif uhol == 90:
            x, y = robotx + dlzka, roboty
        elif uhol == 180:
            x, y = robotx, roboty + dlzka
        elif uhol == 270:
            x, y = robotx - dlzka, roboty
        else:
            x, y = robotx, roboty
        canvas.create_line(robotx, roboty, x, y, fill='black', width=3)
        robotx, roboty = x, y
    elif casti[0] == 'vlavo':
        uhol -= 90
        if uhol < 0:                    
            uhol += 360                 
    elif casti[0] == 'vpravo':
        uhol = (uhol + 90) % 360        

def vykonaj1():
    vykonaj(entry1.get())

entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='Vykonaj', command=vykonaj1)
button1.pack()
canvas.mainloop()
