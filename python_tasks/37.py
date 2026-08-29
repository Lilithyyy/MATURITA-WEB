import random

subory = []
for i in range(5220, 5230):                       #  {riadok A}
    s = open('subory/'+str(i)+'.txt', 'w')
    subory.append(s)
    
subor = open('subory/hlasovanie_2.txt', 'r')
poradie = 0
for riadok in subor:
    poradie += 1
    cislo = int(riadok.strip())
    subory[cislo-5220].write(str(poradie)+'\n')
subor.close()

for s in subory:
    s.close()
    
print('Počet zaslaných SMS:', poradie)
