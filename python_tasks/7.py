import random
pocet_studentov = int(input('Zadaj počet študentov:'))
pocet_otazok = int(input('Zadaj počet otázok:'))

while pocet_otazok < pocet_studentov:
    print('Chyba: počet otázok nemôže byť menší ako počet študentov!')
    pocet_otazok = int(input('Zadaj počet otázok:'))

studenti = []
otazky = []

for i in range(pocet_studentov):
    studenti.append(i+1)
for i in range(pocet_otazok):
    otazky.append(i+1)

# aby párne a nepárne otázky neboli za sebou
parne_otazky = otazky[1::2]
neparne_otazky = otazky[::2]
random.shuffle(neparne_otazky)
random.shuffle(parne_otazky)
otazky = []


for i in range(len(parne_otazky)):
    otazky = otazky + [parne_otazky[i], neparne_otazky[i]]
if len(neparne_otazky) > len(parne_otazky):
    otazky.append(neparne_otazky[-1])
# koniec úseku 

random.shuffle(studenti)
#random.shuffle(otazky)       
print('Poradie odpovedajúcich a ich číslo otázky:')
for i in range(pocet_studentov):
    oznam = '{}. študent: {}, otázka:{}'.format(i+1, studenti[i], otazky[i])
    print(oznam)
