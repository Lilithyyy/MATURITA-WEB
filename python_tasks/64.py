import tkinter, random

canvas = tkinter.Canvas(width=500, height=400, bg='white')
canvas.pack()

sirka, vyska = 90, 50
studenti = []
subor = open('input/64.txt', 'r')
for riadok in subor:
    student = riadok.strip().split(';')
    studenti.append((student[0], student[1]))
subor.close()
pocet = len(studenti)

def oznam(info):
    canvas.delete('all')
    canvas.create_text(250, 200, text=info, fill='red', font='Arial 20')

def kresli(x, y, usadit, maxx, maxy):
    canvas.delete('all')
    for iy in range(maxy):
        for ix in range(maxx):
            canvas.create_rectangle(x+ix*sirka, y+iy*vyska,
                                    x+(ix+1)*sirka-10, y+(iy+1)*vyska-10)
            if usadit != []:
                meno, priezvisko = usadit.pop()
                canvas.create_text(x+ix*sirka + (sirka-10)//2, y+iy*vyska+10,
                                   text=meno, fill='red')
                canvas.create_text(x+ix*sirka + (sirka-10)//2, y+iy*vyska+30,
                                   text=priezvisko, fill='blue')
    
def spracuj():
    radov = int(entry1.get())
    vrade = int(entry2.get())
    if pocet > radov * vrade:
        oznam('Máte málo lavíc na usadenie študentov!')
    else:
        random.shuffle(studenti)
        kresli(20, 20, studenti[:], radov, vrade)

label1 = tkinter.Label(text='Počet radov:')
label2 = tkinter.Label(text='Lavíc v rade:')
entry1 = tkinter.Entry()
entry2 = tkinter.Entry()
button1 = tkinter.Button(text='Potvrď vstup', command=spracuj)
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button1.pack()
