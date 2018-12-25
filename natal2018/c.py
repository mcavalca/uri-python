n = int(input())
pulos = 0
gelo = []
while n:
    n -= 1
    gelo.append(input())

espaco = 0
for i in gelo:
    if i[0] == '.':
        espaco += 1
        if espaco > 2:
            pulos = 'N'
            espaco = 0
            break
    elif i[0] == '-' and espaco > 0:
        espaco = 0
        pulos += 1
if espaco > 0:
    pulos += 1
print(pulos)
