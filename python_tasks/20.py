subor = open('subory/tabulka_pocetnosti.txt')
pocty = [0] * 26
for riadok in subor:
    print(riadok, end='')
    for znak in riadok:
        velke = znak.upper()
        if 'A' <= velke <= 'Z':
            pocty[ord(velke) - 65] += 1
print()
print('Počty jednotlivých znakov v texte:')
for i in range(26):
    if pocty[i] != 0:
        print(chr(65 + i), '-', pocty[i])

print('Nevyskytujú sa:')
for i in range(26):
    if pocty[i] == 0:
        print(chr(65 + i), end=' ')
