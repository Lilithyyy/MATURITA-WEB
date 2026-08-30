import tkinter
canvas = tkinter.Canvas(width=480, height=520, bg='white')
canvas.pack()
nespokojni = [0] * 24

subor = open('input/39.txt', 'r')
for riadok in subor:
    riadok = riadok.strip()
    info = riadok.split()
    spokojnost = info[1]
    cas = info[0].split(':')
    hodina = int(cas[0])
    if spokojnost == 'nie':
        nespokojni[hodina] += 1

pocet_nespokojnych = sum(nespokojni)
pocet_zle = max(nespokojni)
hodina = nespokojni.index(pocet_zle)
print('Najviac nespokojných zák. ({}) je cez hodinu:{}'.format(pocet_zle,
                                                               hodina))
for i in range(24):
    if nespokojni[i] > 0:
        print('Hodina:{} Nespokojných zákazníkov:{}'.format(i, nespokojni[i]))
    canvas.create_rectangle(i*20, 500, i*20+18, 500-nespokojni[i],
                            fill='red')
    canvas.create_text(i*20+9, 510, text='{:02}'.format(i), fill='red')
