import tkinter, random

canvas = tkinter.Canvas(width=200, height=200, bg='white')
canvas.pack()

kod = ''
subor = open('subory/ciarovy_kod_1.txt', 'r')
precitane = False

def generuj_kod():
    kod = chr (random.randrange(9) + ord('1'))
    for i in range(7):
        kod += chr (random.randrange(10) + ord('0'))
    return kod

def kresli_kod(x, y, kod):
    for i in range(len(kod)):
        sirka = int(kod[i])
        if sirka > 0:
            canvas.create_line(x+i*10, y, x+i*10, y+80, width=sirka)
    canvas.create_rectangle(x+5, y+65, x+65, y+80, width=0, fill='white')
    canvas.create_text(x+37, y+72, text=kod, font=('Courier New', 9))

def kresli(event):
    global precitane
    if not precitane:
        canvas.delete('all')
        for ix in range(2):
            for iy in range(2):
                kod = subor.readline().strip()
                if kod != '':
                    kresli_kod(ix * 100 + 10, iy * 100 + 10, kod)
                else:
                    precitane = True
        if precitane:
            subor.close()

kod = generuj_kod()
print(kod)
kresli_kod(20, 10, kod)

canvas.bind_all('<space>', kresli)
