import tkinter

canvas = tkinter.Canvas(width=500, height=400, bg='white')
canvas.pack()

        subor = open('input/59.txt', 'r')
kapacita = 0
zastavky = []
pocet = 0
y = 20

for riadok in subor:
    if kapacita == 0:
        kapacita = int(riadok)
    else:
        casti = riadok.split()
        pocet += int(casti[0])
        pocet -= int(casti[1])
        zastavky.append(pocet)
        canvas.create_text(5, y, text=' '.join(casti[2:]), anchor='nw')
        y += 20
subor.close()

y = 20

def stlac(event):
    global y
    if len(zastavky) > 0:
        canvas.create_rectangle(100, y + 2, 200, y + 18)
        aktpocet = zastavky.pop(0)
        if aktpocet > kapacita:
            farba = 'red'
        else:
            farba = 'green'
        canvas.create_rectangle(100, y + 2, 100 + 100 * aktpocet / kapacita,
                                y + 18, fill=farba)
        y += 20

canvas.focus_set()
canvas.bind('<Key>', stlac)
