def spracuj_riadok(vstup):
    vstup = vstup.strip()
    postupnost = vstup.split()
    farba = 0
    vystup = ''
    for prvok in postupnost:
        pocet = int(prvok)
        vystup = vystup + pocet * str(farba)
        farba = 1 - farba                           #  {riadok A}
    return vystup + '\n'                            #  {riadok B}
    
subor = open('subory/dekompresia_obrazka_1.txt', 'r')
subor_out = open('subory/dekompresia_obrazka_vystup.txt', 'w')
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
    subor_out.write(spracuj_riadok(riadok))         #  {riadok C}
subor.close()
subor_out.close()
