import tkinter, random

canvas = tkinter.Canvas(width=650, height=270)
canvas.pack()

krizovka = []
subor = open('results/subory/krizovka1-1.txt', 'r')
for r in subor:
    popis = r.split()
    riadok = (int(popis[0]), popis[1])
    krizovka.append(riadok)
najtajnicka = max(krizovka)
stlpec_tajnicky = najtajnicka[0]

def kresli_riadok(x, y, tajny_stlpec, obsah, vyplnit, VEL):
    for i in range(len(obsah)):
        farba = 'white'
        if i+1 == tajny_stlpec:
            farba = 'darkgrey'
        canvas.create_rectangle(x+i*VEL, y, x+i*VEL+VEL, y+VEL, fill=farba)
        if vyplnit:
            canvas.create_text(x+i*VEL+VEL/2, y+VEL/2, text=obsah[i],
                               font='Courier 20')

def kresli_krizovku(vstupx, y, stlpec_tajnicky, krizovka, vyplnit, VEL):
    for riadok in krizovka:
        x = vstupx
        x = x + (stlpec_tajnicky - riadok[0]) * VEL
        kresli_riadok(x, y, riadok[0], riadok[1], vyplnit, VEL)
        y += VEL

kresli_krizovku(10, 10, stlpec_tajnicky, krizovka, False, 30)
kresli_krizovku(300, 10, stlpec_tajnicky, krizovka, True, 30)

canvas.mainloop()
