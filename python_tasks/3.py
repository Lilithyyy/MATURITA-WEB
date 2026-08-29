import tkinter

canvas = tkinter.Canvas(width=600, height=100, bg='black')
canvas.pack()
canvas.focus_set()

subor = open('results/subory/zastavky.txt', 'r')
zastavky = []
for zastavka in subor:
    zastavky.append(zastavka.strip())

aktualna = 0
konecna = False
nazov = ''

def animacia():
    global nazov
    nazov = nazov[1:] + nazov[0]           
    canvas.delete('all')
    canvas.create_text(300, 50, text=nazov,
                       fill='red', font=('Courier New', 35, 'bold'))
    canvas.after(100, animacia)
    
def vypis(index, zastavky, konecna):
    global nazov
    nazov = zastavky[index] + ' '
    if konecna:
        nazov += ' - konečná zastávka, vystúpte '
    nazov = nazov + ' '*(20 - len(nazov))  
    
def dalsia(event):
    global aktualna, konecna
    if not konecna:
        aktualna += 1
        if aktualna == len(zastavky)-1:
            konecna = True
        vypis(aktualna, zastavky, konecna)

vypis(aktualna, zastavky, konecna)
animacia()
print(zastavky)
canvas.bind('<Key>', dalsia)
canvas.mainloop()
