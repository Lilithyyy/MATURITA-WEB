def spracuj_riadok(vstup):
    vstup = vstup.strip()
    dlzka = len(vstup)
    vystup = ''
    if vstup[0] == '1':
        vystup += '0 '
    pocet, i = 0, 0
    spracovavam = vstup[0]
    for znak in vstup:
        if znak == spracovavam:
            pocet += 1
        else:
            vystup += str(pocet) + ' '
            spracovavam = znak
            pocet = 1
    vystup += str(pocet) + ' '                #  {riadok A}
    return vystup[:-1] + '\n'                 #  {riadok B}
    
subor = open('subory/kompresia_obrazka_1.txt', 'r')
subor_out = open('subory/kompresia_obrazka_vystup.txt', 'w')
riadok = subor.readline()
velkost = riadok.split()
subor_out.write(riadok)
sirka = int(velkost[0])
vyska = int(velkost[1])
print('Obrázok má rozmery {}x{} bodov'.format(sirka, vyska))
print('V obrázku je {} bodov'.format(sirka * vyska))
riadok = subor.readline()
print(repr(riadok))
spracovane = spracuj_riadok(riadok)
print(repr(spracovane))
subor_out.write(spracovane)
for riadok in subor:                          
    subor_out.write(spracuj_riadok(riadok))   #  {riadok C}
subor.close()
subor_out.close()
