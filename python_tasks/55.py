import tkinter

canvas = tkinter.Canvas(bg='white', width=400, height=400)
canvas.pack()

robotx, roboty = 200, 200
dlzka, uhol = 40, 0

def vykonaj(prikaz):
    global robotx, roboty, dlzka, uhol
    if prikaz == 'ciara':
        if uhol == 0:
            x, y = robotx, roboty - dlzka
        elif uhol == 90:
            x, y = robotx + dlzka, roboty
        elif uhol == 180:
            x, y = robotx, roboty + dlzka
        elif uhol == 270:
            x, y = robotx - dlzka, roboty
        canvas.create_line(robotx, roboty, x, y, width=3)
        robotx, roboty = x, y
    elif prikaz == 'vlavo':
        uhol -= 90
        if uhol < 0:
            uhol += 360
    elif prikaz == 'vpravo':
        uhol = (uhol + 90) % 360

def zosuboru():
    subor = open('subory/kresliaci_robot2.txt')
    pocetopakovani = 0
    zoznam = []
    for riadok in subor:
        prikaz = riadok.strip()
        casti = prikaz.split()
        if casti[0] == 'opakuj':
            pocetopakovani = int(casti[1])
        elif casti[0] == 'koniecopakuj':
            for i in range(pocetopakovani):
                for prikaz in zoznam:
                    vykonaj(prikaz)
            zoznam = []
            pocetopakovani = 0
        else:
            if pocetopakovani > 0:
                zoznam.append(prikaz)
            else:
                vykonaj(prikaz)
    subor.close()

button1 = tkinter.Button(text='Vykonaj príkazy zo súboru', command=zosuboru)
button1.pack()
