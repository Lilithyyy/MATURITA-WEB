import tkinter, random

canvas = tkinter.Canvas(width=700, height=100)
canvas.pack()

puknuty = random.randrange(10)
taniere = [0]*10
koniec = False

def kresli_tanier(x, y, znak):
    canvas.create_oval(x-30, y-30, x+30, y+30, fill='blue', width=3)
    canvas.create_oval(x-20, y-20, x+20, y+20, fill='blue')
    canvas.create_text(x, y, text=znak, font='Arial 20', fill='white')

def pismeno(poradie):
    return chr(ord('A') + poradie)

def vyhra():
    canvas.delete('all')
    canvas.create_text(350, 50, font='Arial 20', fill='blue',
                       text='Gratulujem, označil si puknutý tanier!')

def viacnasobne():
    oznacene = ''
    for i in range(len(taniere)):
        if taniere[i] > 1:
            oznacene += pismeno(i)
    canvas.create_text(350, 80, text='Viackrát si klikol na taniere: ' +
                       oznacene, font='Arial 20', fill='red')
    
def klik(sur):
    global koniec                      
    if sur.x < 10*70 and not koniec:   
        tanier = sur.x // 70
        taniere[tanier] += 1
        if tanier == puknuty:
            koniec = True
            vyhra()
            viacnasobne()

for i in range(10):
    kresli_tanier(i*70+35, 50, pismeno(i))
    
canvas.bind('<Button-1>', klik)
canvas.mainloop()
