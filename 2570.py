l, c, n = [int(x) for x in input().split()]

game = [[0]*(l+1) for x in range(c+1)]

ponto = 1
for i in range(n):
    j, k = input().split()
    k = int(k)
    if j == 'L':
        for h in range(l+1):
            game[k-1][h] = ponto
    else:
        for h in range(l+1):
            game[h][k-1] = ponto
    ponto += 1
    if ponto == 5:
        ponto = 1

ponto = [0, 0, 0, 0, 0, 0]
for i in range(l):
    for j in range(c):
        ponto[game[i][j]] += 1

print('R%d H%d C%d P%d' % (ponto[1], ponto[2], ponto[3], ponto[4]))