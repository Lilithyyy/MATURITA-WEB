import tkinter

nazov = 'input/29.txt'
subor = open(nazov, 'r')
riadok = subor.readline()
subor.close()
velkost = riadok.split()
sirka = int(velkost[0])
vyska = int(velkost[1])

canvas = tkinter.Canvas(width=sirka, height=vyska, bg='white')
canvas.pack()

def body(x, y, pocet):
    canvas.create_rectangle(x, y, x+1, y+1, width=0, fill='black')

def vykresli(prva):
    subor = open(nazov, 'r')
    riadok = subor.readline()
    y = 0
    for riadok in subor:
        postupnost = riadok.split()
        x = 0
        farba = prva
        for prvok in postupnost:
            pocet = int(prvok)
            if farba:
                body(x, y, pocet)
            farba = not farba
            x += pocet
        canvas.update()
        y += 1
    subor.close()

def inak():
    vykresli(False)

button1 = tkinter.Button(text='inak', command=inak)
button1.pack()
vykresli(True)
