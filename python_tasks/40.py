vyjadreni = [0] * 24

subor = open('subory/spokojnost_0.txt', 'r')
dni = 0
cas1 = '00:00'
pocet_v_dni = 0
for riadok in subor:
    riadok = riadok.strip()
    info = riadok.split()
    cas2 = info[0]
    cas2_roz = info[0].split(':')
    hodina = int(cas2_roz[0])
    minuta = int(cas2_roz[1])
    vyjadreni[hodina] += 1
    if cas2 < cas1:
        dni += 1
        print('{}. deň - počet reakcií:{}'.format(dni, pocet_v_dni))
        pocet_v_dni = 1
    else:
        pocet_v_dni += 1    
    cas1 = cas2
print('{}. deň - počet reakcií:{}'.format(dni, pocet_v_dni))
pocet_vyjadreni = sum(vyjadreni)
print('Počet všetkých vyjadrení:', pocet_vyjadreni)
for i in range(24):
    if vyjadreni[i] > 0:
        print('Hodina:{} Reakcií zákazníkov:{}'.format(i, vyjadreni[i]))
print('Počet dní:', dni)
