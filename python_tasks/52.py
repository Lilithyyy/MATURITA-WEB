sprava = input('Zadajte informáciu pre cestujúcich: ')
slova = sprava.split()
print('Počet slov:', len(slova))
stlacena = ''
for slovo in slova:
    stlacena += slovo[0].upper()+slovo[1:].lower()   #  {riadok A}
print('Stlačená správa:', stlacena)

# Spätný prevod zo stlačenej správy na pôvodný oznam
print('Na obrazovke: ', end='')
prve = True                                          #  {riadok B}
for znak in stlacena:
    if 'A' <= znak <= 'Z':
        if prve:
            prve = False
        else:
            print(end=' ')
    print(znak.upper(), end='')
