def GCDsimp (n, d):
    if d > 0:
        return GCDsimp (d, n % d)
    return n

cont = 0
apostas = []
while True:
    try:
        n, d = input().split()
        apostas.append(GCDsimp(int(n), int(d)))
        if apostas[cont] > 5:
            print('Noel')
        else:
            print('Gnomos')

        cont += 1



    except EOFError:
        break

for i in range(cont-1, -1, -1):
    print(apostas[i], end = ' ')
print()
