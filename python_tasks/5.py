subor = open('subory/objednane_jedla.txt', 'r')

s = {'z':0, 'c':0, 'h':0, 'm':0}         
pocet = 0
for riadok in subor:
    info = riadok.split()
    jedlo = info[1]
    pocet += 1
    s[jedlo] = s.get(jedlo, 0) + 1       

print('počet jedál:', pocet)


malo = ''
for jedlo, pocet in s.items():
    print('Kod jedla:{} počet objednávok:{}'.format(jedlo, pocet))
    if pocet < 20:
        malo = malo + str(jedlo) + ', ' 

        
malo = malo[:-2]                        
if malo != '':
    print('Málo objednávok majú tieto jedlá:', malo)
else:
    print('Všetky jedlá si objednalo aspoň 20 ľudí')

subor.close()
