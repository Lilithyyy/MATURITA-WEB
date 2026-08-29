import tkinter

canvas = tkinter.Canvas(width=600, height=100, background='white')
canvas.pack()

operand = 0
vysledok = 0
displej = canvas.create_text(3, 3, anchor='nw', font='Courier 30', text=0)

def stlac(event):
    global vysledok, displej, operacia, operand
    if event.y >= 70:
        tlacidlo = event.x // 30
        if tlacidlo < 4:
            if tlacidlo == 0:
                vysledok = 0
            elif tlacidlo == 1:
                operacia = '+'
                operand = vysledok
                vysledok = 0
            elif tlacidlo == 2:
                operacia = '-'
                operand = vysledok
                vysledok = 0
            elif tlacidlo == 3:
                if operacia == '+':
                    vysledok += operand
                elif operacia == '-':
                    vysledok = operand - vysledok
            canvas.itemconfig(displej, text=vysledok)

    elif event.y >= 40:
        cislica = event.x // 30
        if cislica < 10:
            vysledok = vysledok * 10 + cislica
            canvas.itemconfig(displej, text=vysledok)

for i in range(10):
    canvas.create_rectangle(i * 30, 40, (i + 1) * 30, 70)
    canvas.create_text(i * 30 + 15, 55, text=i)
for i in range(4):
    canvas.create_rectangle(i * 30, 70, (i + 1) * 30, 100)
canvas.create_text(15, 85, text='C')
canvas.create_text(45, 85, text='+')
canvas.create_text(75, 85, text='-')
canvas.create_text(105, 85, text='=')

canvas.bind('<Button-1>', stlac)
