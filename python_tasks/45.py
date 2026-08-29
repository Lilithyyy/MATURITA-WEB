sk = []
en = []
subor = open('subory/ucenie_sa_slovicok.txt', 'r')
i = 0
for riadok in subor:
    if i%2 == 0:
        sk.append(riadok.strip())
    else:
        en.append(riadok.strip())
    i += 1
subor.close()
jazyk = input('Ak Ti mám zadávať slovenské slovíčka napíš A:')
slovenske = jazyk=='A'
a, b = en[:], sk[:]
if slovenske:
    a, b = b, a
zle = 0
while len(a) > 0:
    slovo1 = a.pop(0)
    slovo2 = b.pop(0)
    odpoved = input('Zadaj preklad slova ' + slovo1 + ':')
    if odpoved != slovo2:
        a.append(slovo1)
        b.append(slovo2)
        zle += 1
        print('Nesprávne!')
    else:
        print('Správne!')
print('Počet nesprávych odpovedí:'+str(zle))
