import random

pocty = [0] * 10
vypadnuti = []

subor = open('input/28.txt', 'r')
for riadok in subor:
    cislo = int(riadok.strip())
    pocty[cislo - 5220] += 1                            
subor.close()
print('Počet zaslaných SMS:', sum(pocty))

subor = open('input/hlasovanie_vypadnuti.txt', 'r')
for riadok in subor:
    cislo = int(riadok.strip())
    vypadnuti.append(cislo)
subor.close()

vysledky = []
for i in range(10):
    print('Súťažiaci: {} Získlal hlasov: {}'.format(i+5220, pocty[i]))
    if not i+5220 in vypadnuti:
        vysledky.append((pocty[i], i+5220))     

vypadava = min(vysledky)                       
print('Najmenej hlasov ({}) získal súťažiaci {}'.format(vypadava[0], vypadava[1]))
