import random
def sifruj(vstup, desifrovat):
    vystup = ''
    if desifrovat:
        posun = -1 * (ord(vstup[0]) - 96)
        vstup = vstup[1:]                                   
    else:
        posun = random.randint(1, 25)
        vystup += chr(posun + 96)
    for znak in vstup:
        if 'a' <= znak <= 'z':
            vystup += chr( (ord(znak)-97 +  posun) % 26 + 97) 
        else:
            vystup += znak
    return vystup

#vstup = input('Zadaj vstupný reťazec:')
chce_desifrovat = input('Ak chceš dešifrovať napíš A:')
desifrovat = False
vstupny_subor = 'subory/vstupny_text.txt'
vystupny_subor = 'subory/zasifrovany_text_2.txt'

if chce_desifrovat == 'A':
    desifrovat = True
    vstupny_subor, vystupny_subor = vystupny_subor, vstupny_subor 


subor1 = open(vstupny_subor, 'r')
subor2 = open(vystupny_subor, 'w')
for riadok in subor1:
    novy_riadok = sifruj(riadok, desifrovat)
    subor2.write(novy_riadok)
    print(riadok)
    print(novy_riadok)
    
subor1.close()
subor2.close()
