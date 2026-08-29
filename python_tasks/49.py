import tkinter

canvas = tkinter.Canvas(width=600, height=300, bg='white')
canvas.pack()

pocetradov = 10
VEL = 40
busx, busy = 50, 50
obsadene = []
volne = []

def zafarbi(sedadlo, farba):
    canvas.itemconfig('sedadlo_' + str(sedadlo), fill=farba)
    
def kresli(x, y, pocet):
    cislo = 0
    for i in range(pocet):
        for j in range(4):
            cislo += 1
            canvas.create_rectangle(x+i*VEL, y+j*VEL,
                                    x+(i+1)*VEL-10, y+(j+1)*VEL-10,
                                    tags='sedadlo_'+str(cislo))
            canvas.create_text(x+i*VEL+VEL/2-5, y+j*VEL+VEL/2-5, text=cislo)

def obsad(sedadlo):
    global obsadene, volne
    index = volne.index(sedadlo)
    volne.pop(index)
    obsadene.append(sedadlo)
    zafarbi(sedadlo, 'red')

def uvolni(sedadlo):
    global obsadene, volne
    index = obsadene.index(sedadlo)
    obsadene.pop(index)
    volne.append(sedadlo)
    zafarbi(sedadlo, 'lightgreen')

def info():
    canvas.delete('info')
    canvas.create_text(busx, 220, text='Počet voľných: '+str(len(volne)),
                       tags='info', anchor='nw')
    canvas.create_text(busx, 240, text='Počet obsadených: '+str(len(obsadene)),
                       tags='info', anchor='nw')
    volne_pri_ulicke = 0
    for sedadlo in volne:
        if 2 <=sedadlo % 4 <= 3:
            volne_pri_ulicke += 1
    canvas.create_text(busx, 260, text='Počet voľných pri uličke: '+
                       str(volne_pri_ulicke), tags='info', anchor='nw')
    
def klik(event):
    if (busx < event.x < busx + VEL * pocetradov and
        busy < event.y < busy + VEL * 4):
        ix = (event.x - busx) // VEL
        iy = (event.y - busy) // VEL
        sedadlo = ix * 4 + iy + 1
        zafarbi(sedadlo, 'red')
        if sedadlo in volne:
            obsad(sedadlo)
        else:
            uvolni(sedadlo)
        info()
        
def uloz():
    subor = open('subory/rezervacia_miesteniek_vystup.txt', 'w')
    for j in range(1, 5):
        riadok = ''
        for i in range(j, pocetradov*4+1, 4):
            if i in volne:
                riadok += '{:2} '.format(i)
            else:
                riadok += ' X' + ' '
        riadok = riadok[:-1] + '\n'
        subor.write(riadok)
    subor.close()
        
kresli(busx, busy, pocetradov)
canvas.bind('<Button-1>', klik)
button1 = tkinter.Button(text='save', command=uloz)
button1.pack()

obsadene = []
volne = []
for i in range(pocetradov*4):
    volne.append(i+1)
    zafarbi(i+1, 'lightgreen')
info()
