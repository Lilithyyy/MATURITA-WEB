import tkinter

canvas = tkinter.Canvas(width=800, height=200, background='white')
canvas.pack()

def vykresli():
    subor = open('subory/zastavba_na_ulici.txt')
    limit = int(entry1.get())
    y = 150
    x = 10
    vyska2 = 0
    for riadok in subor:
        cisla = riadok.split()
        sirka = int(cisla[0])
        vyska = int(cisla[1])
        if vyska > 0:
            canvas.create_rectangle(x, y - vyska, x + sirka, y, fill='grey')
        else:
            canvas.create_line(x, y, x + sirka, y, width=3, fill='green')
        if vyska != 0 and vyska2 != 0 and abs(vyska - vyska2) > limit:
            canvas.create_line(x, y - vyska, x, y - vyska2,
                               width=3, fill='red')
        x += sirka
        vyska2 = vyska
    subor.close()

entry1 = tkinter.Entry()
entry1.pack()
entry1.insert(0, '60')
button1 = tkinter.Button(text='Vykresli ulicu', command=vykresli)
button1.pack()
canvas.mainloop()
