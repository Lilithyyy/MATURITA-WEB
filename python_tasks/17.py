txt = input('Zadajte vetu napísanú veľkými písmenami: ')
tabulka = [0] * 10

for znak in txt:
    if znak == ' ':
        tabulka[0] += 1
        print(0, end=' ')
    else:
        kod = ord(znak) - 65
        policko = kod // 3 + 1
        pocet = kod % 3 + 1
        tabulka[policko] += pocet
        print(str(policko) * pocet, end=' ')
print()

m = max(tabulka)
print('Najčastejšie zvolené políčka:')
for i in range(10):
    if tabulka[i] == m:
        print(i, end=' ')
