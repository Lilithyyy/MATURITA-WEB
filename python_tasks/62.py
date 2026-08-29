import tkinter

def vykresli():
    canvas.delete('all')
    canvas.create_text(10, 10, anchor='nw', text=otazka)
    sucet = 0
    najviac = 0
    for p in pocty:
        sucet += p
        najviac = max(najviac, p)
    for i in range(3):
        canvas.create_text(10, (i + 1) * 30 + 8, anchor='nw',
                           text=str(i + 1) + ') ' +
                                odpoved[i] + ' - ' + str(pocty[i]))
        if pocty[i] == nejvac:
            farba = 'green'
        else:
            farba = 'red'
        canvas.create_rectangle(100, (i + 1) * 30 + 5,
                                100 + pocty[i]/sucet*200, (i + 1) * 30 + 25,
                                width=0, fill=farba)

def stlac(event):
    if event.char == '1':
        pocty[0] += 1
    elif event.char == '2':
        pocty[1] += 1
    elif event.char == '3':
        pocty[2] += 1
    vykresli()
    subor = open('subory/anketa.txt', 'w')
    subor.write(otazka+'\n')
    subor.write(str(pocty[0])+' '+str(pocty[1])+' '+str(pocty[2]))
    subor.close()

subor = open('subory/anketa.txt')
otazka = subor.readline().strip()
riadok = subor.readline()
subor.close()
odpoved = ('Áno', 'Nie', 'Neviem')
pocty = []
cisla = riadok.split()
for i in range(3):
    pocty.append(int(cisla[i]))
canvas = tkinter.Canvas(width=600, height=200, background='white')
canvas.pack()
canvas.focus_set()
vykresli()
canvas.bind('<Key>', stlac)
#canvas.mainloop()
