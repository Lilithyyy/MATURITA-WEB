import random

subor1 = open('input/21.txt', 'r')
subor2 = open('subory/poprehadzovany_text1.txt', 'w')

for riadok in subor1:
    print(riadok, end='')
    slova = riadok.strip().split()
    for i in range(len(slova)):
        slovo = slova[i]
        pismenka = list(slovo[1:-1])                         #  {riadok A}
        random.shuffle(pismenka)
        slova[i] = slovo[0] + ''.join(pismenka) + slovo[-1]  #  {riadok B}
    riadok = ''
    for slovo in slova:
        riadok += slovo + ' '
    riadok = riadok[:-1] + '\n'
    print(riadok, end='')
    subor2.write(riadok)
        
subor1.close()
subor2.close()
