import tkinter
canvas = tkinter.Canvas(width=1000, height=650, bg='white')
canvas.pack()

obrazok = tkinter.PhotoImage(file='subory/obr6.png')

sirka = obrazok.width()
vyska = obrazok.height()
canvas['width'] = sirka
canvas['height'] = vyska

canvas.create_image(0, 0, anchor='nw', image=obrazok)
canvas.update()
for y in range(vyska):
    for x in range(sirka):
        farba = obrazok.get(x, y)
        farba = (farba[0] + farba[1] + farba[2]) // 3
        #farba = ''
        farba = '#' + 3 * '{:02x}'.format(farba)
        obrazok.put(farba, (x, y))
    canvas.update()

obrazok.write(filename='subory/obr6_cb.png')
