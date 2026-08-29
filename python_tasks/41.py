import tkinter

canvas = tkinter.Canvas(width=420, height=150, bg='white')
canvas.pack()

farby = ['green', 'red', 'blue', 'orange']
skratky = 'zcmo'
x, y, vel = 10, 40, 100

def vykresli():
    for i in range(len(farby)):
        canvas.create_rectangle(x+i*vel, y, x+i*vel+vel-2, y+vel-2,
                                fill=farby[i], outline='')

def klik(sur):
    if y < sur.y < y + vel:
        poradie = (sur.x - x) // vel
        if 0 <= poradie < len(farby):
            print(poradie)
            student = entry1.get()
            if student != '':
                subor = open('subory/vyber_jedla.txt', 'a')
                subor.write(student+' '+skratky[poradie]+'\n')
                subor.close()

canvas.create_text(210, 20, text='VÝBER JEDLA', font='Arial 20', fill='red')
subor = open('subory//vyber_jedla.txt', 'w')
subor.close()

vykresli()
canvas.bind('<Button-1>', klik)
label1 = tkinter.Label(text='kód študenta:')
label1.pack()
entry1 = tkinter.Entry()
entry1.pack()
