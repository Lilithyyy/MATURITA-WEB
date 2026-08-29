subor = open('subory/dopravny_prieskum.txt')
zastavky = []
pocet = 0
maxpocet = 0
for riadok in subor:
    casti = riadok.split(';')
    nastup = int(casti[0])
    vystup = int(casti[1])
    pocet += nastup
    pocet -= vystup
    maxpocet = max(maxpocet, pocet)
    zastavky.append((casti[2].strip(), pocet, nastup >= 10,
                     nastup < 3 and vystup < 3))                #  {riadok A}
subor.close()

print('Zastávka - Počet cestujúcich')
for zastavka in zastavky:
    print(zastavka[0], '-', zastavka[1])

print('Odporúčaný typ električky:', end='')
if maxpocet > 100:
    print('dlhá')
elif maxpocet > 50:
    print('štandardná')
else:
    print('krátka')

print('Zastávky vhodné na umiestnenie automatu:')
for zastavka in zastavky:
    if zastavka[2]:
        print(zastavka[0])
print('Vhodné zastávky na znamenie:')
for zastavka in zastavky:
    if zastavka[3]:
        print(zastavka[0])
