import random

vstup = input('Zadaj tip na 6 čísel v lotérii:')

def zrebovanie():
    cisla = []
    for i in range(1, 50):
        cisla.append(i)
    random.shuffle(cisla)
    return cisla[:6]
        
def na_zoznam(retazec):
    zoz = retazec.strip().split()
    for i in range(len(zoz)):
        zoz[i] = int(zoz[i])
    return zoz

def rovnake(post1, post2):
    pocet = 0
    vystup = ''
    for a in post1:
        if a in post2:
            vystup += str(a)+' '
            pocet += 1
    return vystup[:-1], pocet
    
vyzrebovane = zrebovanie()
print('Vyžrebované čísla:', vyzrebovane)
tip = na_zoznam(vstup)
uhadnute, pocet = rovnake(vyzrebovane, tip)
print('Počet uhádnutých:', pocet, ' uhádnuté:', uhadnute)

uhadnutych = [0] * 7                                       
subor = open('subory/loteria_2.txt', 'r')
for riadok in subor:
    cisla_tipu = na_zoznam(riadok)
    uhadnute, pocet = rovnake(cisla_tipu, vyzrebovane)
    uhadnutych[pocet] += 1
subor.close()
for i in range(len(uhadnutych)):
    print('{} čísel uhádlo {} účastníkov'.format(i, uhadnutych[i]))
