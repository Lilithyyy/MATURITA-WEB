import tkinter

stvorcek = 50
subor = open('subory/lodicky.txt')
cisla = subor.readline().split()
sirka = int(cisla[0])
vyska = int(cisla[1])
pristav = []
for r in range(vyska):
    pristav.append(subor.readline().split())
subor.close()

canvas = tkinter.Canvas(width=stvorcek * sirka, height=stvorcek * vyska)
canvas.pack()

r = 0
s = 0

def pridaj():
    global r, s
    nasiel = False
    while r < vyska and not nasiel:
        if pristav[r][s]=='0' and pristav[r][s+1]=='0' and pristav[r][s+2]=='0':
            canvas.create_rectangle(s * stvorcek + 2, r * stvorcek + 2,
                                    (s+3)*stvorcek-2, (r+1)*stvorcek-2,
                                    width=0, fill='yellow')
            nasiel = True
            s += 4
            if s > sirka - 3:
                r += 1
                s = 0
        else:
            s += 1
            if s > sirka - 3:
                r += 1
                s = 0
    if not nasiel:
        canvas.create_text(sirka * stvorcek / 2, vyska * stvorcek / 2,
                           text='PRÍSTAV JE PLNÝ', font='Arial 30')

for r in range(vyska):
    for s in range(sirka):
        if pristav[r][s] == '1':
            farba = 'grey'
        else:
            farba = 'skyblue'
        canvas.create_rectangle(s * stvorcek, r * stvorcek,
                                (s + 1) * stvorcek, (r + 1) * stvorcek,
                                width=0, fill=farba)

button1 = tkinter.Button(text='Pridaj lodičku', command=pridaj)
button1.pack()
#canvas.mainloop()
