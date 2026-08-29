import tkinter

canvas = tkinter.Canvas(width=1000, height=400, bg='white')

subor = open('subory/trasa_linky_metra.txt')
metro = subor.readlines()
subor.close()
farba = metro.pop(0).strip()                                #  {riadok A}
x = 20
canvas.create_line(x, 205, x + 40 * (len(metro) - 1), 205,
                   width=3, fill=farba)

for i in range(len(metro)):
    nazov = metro[i].strip()
    if nazov[0] == '*':
        nazov = nazov[1:]
        expres = True
    else:
        expres = False
    canvas.create_text(x, 200, text=nazov,
                       angle=45, anchor='sw', font='Arial')
    if i == 0 or i == len(metro) - 1:  # Konečné stanice    #  {riadok B}
        canvas.create_rectangle(x - 20, 200, x, 220, fill=farba, width=0)
    elif expres:
        canvas.create_oval(x - 10, 200, x, 210,
                           width=2, fill='white', outline=farba)
    else:
        canvas.create_oval(x - 10, 200, x, 210, fill=farba, width=0)
    x += 40

canvas.pack()
#canvas.mainloop()
