import tkinter, random

canvas = tkinter.Canvas(width=450, height=200)
canvas.pack()

taha = 1
pocet_zapaliek = 15

def zapalka(x, y):
    canvas.create_line(x, y, x, y+100, width=5, fill='yellow',
                       tags='zapalka')
    canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown',
                       tags='zapalka')

def vykresli(pocet):
    canvas.delete('zapalka')
    for i in range(pocet):
        zapalka(i*20+20, 50)

def napis_oznam(hrac, pocet):
    canvas.delete('oznam')
    canvas.create_text(200, 10, text='ťahá hráč:'+str(hrac), tags='oznam')
    canvas.create_text(200, 30, text='počet zápaliek:'+str(pocet),
                       tags='oznam')

def gratulacia(hrac):
    canvas.delete('oznam')
    canvas.create_text(225, 100, text='Gratulujem, vyhral hráč:'+str(hrac),
                       fill='red', font='Arial 30')
    
def vstup(event):
    if '1' <= event.char <= '3':                  
        potiahnut = int(event.char)
        global pocet_zapaliek, taha             
        if pocet_zapaliek - potiahnut >= 0:
            pocet_zapaliek -= potiahnut
            vykresli(pocet_zapaliek)
            if pocet_zapaliek == 0:
                gratulacia(taha)
            else:
                taha = 3 - taha
                napis_oznam(taha, pocet_zapaliek)

vykresli(pocet_zapaliek)
napis_oznam(taha, pocet_zapaliek)
canvas.bind_all('<Key>', vstup)
