import random
subor = open('input/27.txt', 'r')
riadky = subor.readlines()
subor.close()

def vypis():
    for riadok in riadky:
        print(riadok, end='')
    
def rozhodnutie():
    return random.choice((True, False))

def spracuj_riadok(riadok):
    slova = []
    slova = riadok.split()
    if rozhodnutie():
        random.shuffle(slova)
    novy_riadok = ''
    for slovo in slova:
        if rozhodnutie():
            slovo = slovo[::-1]
        novy_riadok += slovo + ' ' 
    return novy_riadok[:-1] + '\n'

def uloz_do_suboru(nazov):
    subor = open(nazov, 'w')
    subor.writelines(riadky)
    subor.close()

vypis()
print('='*60)

if rozhodnutie():
    random.shuffle(riadky)
for i in range(len(riadky)):                 #  {riadok A}
    riadok = riadky[i]
    riadky[i] = spracuj_riadok(riadok[:-1])  #  {riadok B}

vypis()
uloz_do_suboru('subory/virus_vystup.txt')
