import tkinter

def klik(event):
    global zac_r, zac_s
    r = event.y // strana
    s = event.x // strana
    if zac_r == -1:  # Začiatočný bod steny
        zac_r, zac_s = r, s
        canvas.itemconfig(siet[r][s], fill='#0000FF')
    else:   # Koncový bod steny
        if zac_r == r:  # Vodorovná stena
            for i in range(min(s, zac_s), max(s, zac_s) + 1):
                canvas.itemconfig(siet[r][i], fill='#0000FF')
        elif zac_s == s:  # Zvislá stena
            for i in range(min(r, zac_r), max(r, zac_r) + 1):
                canvas.itemconfig(siet[i][s], fill='#0000FF')
        else:  # Ak som klikol šikmo, zruším označenie začiatku steny
            canvas.itemconfig(siet[zac_r][zac_s], fill='#FFFFFF')
        zac_r, zac_s = -1, -1

strana = 40
sirka = 10
vyska = 10
canvas = tkinter.Canvas(width=sirka * strana, height=vyska * strana)
siet = []
for r in range(vyska):
    riadok = []
    for s in range(sirka):
        riadok.append(canvas.create_rectangle(s*strana, r*strana,
                                              (s+1)*strana, (r+1)*strana,
                                              fill='#FFFFFF'))
    siet.append(riadok)
canvas.pack()
zac_r, zac_s = -1, -1
canvas.bind('<Button-1>', klik)
#canvas.mainloop()
