import tkinter

obrazok = []
strana = 2
subor = open('results/subory/preklopenie_obrazka.txt')
riadok = subor.readline()
cisla = riadok.split()
sirka = int(cisla[0])
vyska = int(cisla[1])

canvas = tkinter.Canvas(width=sirka*strana, height=vyska*strana,
                        background='white')
canvas.pack()

def zrkadlo():
    global sirka, vyska, strana
    canvas.delete('all')
    for i in range(vyska):
        for j in range(sirka):
            if int(obrazok[i][j]) == 0:
                farba = 'white'
            else:
                farba = 'black'
            canvas.create_rectangle((sirka-j-1)*strana, i*strana,
                                    (sirka-j)*strana, (i+1)*strana,
                                    width=0, fill=farba)

button1 = tkinter.Button(text='Preklop', command=zrkadlo)
button1.pack()

pocet_jednotiek = 0
for r in range(vyska):
    riadok = subor.readline()
    cisla = riadok.split()
    obrazok.append(cisla)
    for s in range(sirka):
        if cisla[s] == '0':
            farba = 'white'
        else:
            pocet_jednotiek += 1
            farba = 'black'
        canvas.create_rectangle(s*strana, r*strana,
                                (s+1)*strana, (r+1)*strana,width=0,
                                fill=farba)
subor.close()
print('Obrázok má {} pixelov.'.format(vyska * sirka))
print('V popise obrázku je {} jednotiek.'.format(pocet_jednotiek))
canvas.mainloop()
