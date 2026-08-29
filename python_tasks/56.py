import tkinter

strana = 40
sirka = 10
vyska = 10
siet = []

canvas = tkinter.Canvas(width=sirka * strana, height=vyska * strana)

for r in range(vyska):
    riadok = []
    for s in range(sirka):
        riadok.append(canvas.create_rectangle(s*strana, r*strana,
                                              (s+1)*strana, (r+1)*strana,
                                              fill='#FFFFFF'))
    siet.append(riadok)

def klik(event):
    canvas.itemconfig(siet[event.y // strana][event.x // strana],
                      fill=entry1.get())

def save():
    subor = open('subory/editor_levelov1_vystup.txt', 'w')
    for r in range(vyska):
        for s in range(sirka):
            subor.write(canvas.itemcget(siet[r][s], 'fill'))
        subor.write('\n')
    subor.close()

canvas.pack()
entry1 = tkinter.Entry()
entry1.insert(0, '#FF0000')
entry1.pack()
button1 = tkinter.Button(text='Uložiť', command=save)
button1.pack()
canvas.bind('<Button-1>', klik)
