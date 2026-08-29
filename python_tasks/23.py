def sifruj(vstup, kluc, desifrovat):
    dlzka_vstupu = len(vstup)
    opakovany_kluc = kluc * (1 + dlzka_vstupu // len(kluc))   #  {riadok A}
    vystup = ''
    i = 0
    for znak in vstup:
        if 'a' <= znak <= 'z':
            posun = ord(opakovany_kluc[i]) - 97 + 1
            if desifrovat:
                posun *= -1
            vystup += chr( (ord(znak)-97 +  posun) % 26 + 97) #  {riadok B}
        else:
            vystup += znak
        i += 1
    return vystup

kluc = input('Zadaj kluc:')
#vstup = input('Zadaj vstupný reťazec:')
chce_desifrovat = input('Ak chceš dešifrovať napíš A:')
desifrovat = False
vstupny_subor = 'subory/vstupny_text.txt'
vystupny_subor = 'subory/zasifrovany_text_1.txt'

if chce_desifrovat == 'A':
    desifrovat = True
    vstupny_subor, vystupny_subor = vystupny_subor, vstupny_subor #  {riadok C}
subor1 = open(vstupny_subor, 'r')
subor2 = open(vystupny_subor, 'w')
for riadok in subor1:
    novy_riadok = sifruj(riadok, kluc, desifrovat)
    subor2.write(novy_riadok)
    print(riadok)
    print(novy_riadok)
subor1.close()
subor2.close()
