from math import sqrt

def distancia (x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

while True:
    n = int(input())
    if n == 0:
        break
    pontos = []
    while n:
        n -= 1
        x, y = input().split()
        pontos.append([int(x), int(y)])

    distancias = []
    for i in range(len(pontos)):
        for j in range(i + 1, len(pontos)):
            distancias.append(distancia(pontos[i][0], pontos[i][1], pontos[j][0], pontos[j][1]))

    d = min(distancias)
    if d < 10000:
        print('%.4f' % d)
    else:
        print('INFINITY')
