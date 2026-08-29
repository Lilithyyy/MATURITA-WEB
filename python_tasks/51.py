sprava = input('Zadajte informáciu pre cestujúcich: ')
slova = sprava.split()
print('Počet slov:', len(slova))
stlacena = ''
velke = True
for slovo in slova:
    if velke:
        stlacena += slovo.upper()
        velke = False
    else:
        stlacena += slovo.lower()
        velke = True
print('Stlačená správa:', stlacena)

# Spätný prevod zo stlačenej správy na pôvodný oznam
print('Na obrazovke: ', end='')
velke = True
for znak in stlacena:
    if velke != ('A' <= znak <= 'Z'):             #  {riadok A}
        print(end=' ')
        velke = not velke
    print(znak.upper(), end='')
