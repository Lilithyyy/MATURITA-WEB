subor = open('input/4.txt', 'r')

pocet = 0
zoz = []
teploty = []
ibateploty = []

for r in subor:
    info = r.strip()
    teplota = info[21:26]
    teplota = float(teplota.replace(',', '.'))  
    teploty.append((teplota, info[:3]))        
    ibateploty.append(teplota)
    print(teplota)
    pocet += 1
    zoz.append(info)

subor.close()

print('Počet meraní:', pocet)
print('Maximum bolo v stanici:', max(teploty)[1])
priemer = sum(ibateploty)/len(teploty)
print('Priemerná teplota bola: {:5.2f} stupňov'.format(priemer))
