import tkinter, random

canvas = tkinter.Canvas(width=600, height=200, background='white')
canvas.pack()

a = random.randint(11, 20)
b = random.randint(2, 9)

canvas.create_text(10, 10, text=str(a) + ' : ' + str(b) + ' =',
                   anchor='nw', font='Courier 30')

def over():
    global a, b
    farby = ('red', 'green', 'blue')
    vysledok = a // b
    if int(entry1.get()) == vysledok:
        txt = 'SPRÁVNE'
    else:
        txt = 'NESPRÁVNE'
    canvas.create_text(10, 50, anchor='nw', text=txt, font='Courier 30')
    x = 10
    f = 0
    for i in range(a):
        if i >= vysledok * b:
            farba = 'yellow'
            if i == vysledok * b:
                x += 30
        else:
            if i % b == 0:
                f = (f + 1) % len(farby)
            farba = farby[f]
        canvas.create_oval(x, 100, x + 20, 120, width=0, fill=farba)
        x += 30

entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='Over', command=over)
button1.pack()
