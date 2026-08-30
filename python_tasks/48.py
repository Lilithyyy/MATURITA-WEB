import random

def generuj_priklad():
    a, b = random.randrange(11), random.randrange(11)
    priklad = '{} * {} = '.format(a, b)
    return priklad, a * b                         #  {riadok A}

subor = open('output/48.txt', 'w')
priklady = []
for i in range(10):
    priklad = generuj_priklad()
    print(priklad[0], file=subor)
    priklady.append(priklad)
subor.close()

pocet, body = 0, 0
while len(priklady) > 0:
    pocet += 1
    priklad = priklady.pop(0)
    print(priklad[0], end='')                     #  {riadok B}
    vstup = input('')
    odpoved = int(vstup)
    if odpoved != priklad[1]:
        priklady.append(priklad)
    elif pocet < 10:
        body +=1
print('Počet získaných bodov:', body)
