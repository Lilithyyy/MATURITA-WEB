import random
subor = open('subory/obesenec.txt', 'r')
slova = subor.readlines()
subor.close()
random.shuffle(slova)
slovo = slova[0].strip()
uhadnute = '.' * len(slovo)
print('Hádaj písmená v slove!')
print(uhadnute)
zle = 0
while uhadnute != slovo and zle < 10:             #  {riadok A}
    pismeno = input('Zadaj jedno pismeno:')[0]
    if pismeno in slovo:                          #  {riadok B}
        nove_slovo = ''
        for i in range(len(slovo)):
            if pismeno == slovo[i]:
                nove_slovo += pismeno             #  {riadok C}
            else:
                nove_slovo += uhadnute[i]
        print('písmeno ', pismeno, ' sa nachádza v slove')
        uhadnute = nove_slovo
    else:
        zle += 1
        print('nie je tam...')
    print(uhadnute)

if uhadnute == slovo:
    print('Gratulujem, uhádol si celé slovo!')
else:
    print('Skončil si, 10x si si netipol správne!')
