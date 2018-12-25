n, m = [int(x) for x in input().split()]
t = []
possibleX = []
possibleY = []

for i in range(n):
    t.append([int(x) for x in input().split()])
    if (i > 0) and (i < n - 1) and (42 in t[i]):
        indexes = [index for index, x in enumerate(t[i]) if x == 42]
        possibleX.extend([i] * len(indexes))
        possibleY.extend(indexes)

x = y = 0

for i in range(0, len(possibleX)):
    if (possibleX[i] > 0) and (possibleX[i] < n-1) and (possibleY[i] > 0) and (possibleY[i] < m-1):
        soma = 0
        for i2 in range(possibleX[i]-1, possibleX[i] + 2):
            for j2 in range(possibleY[i] - 1, possibleY[i] + 2):
                soma += t[i2][j2]
        if soma == 98:
            x = possibleX[i] + 1
            y = possibleY[i] + 1
            break

print(x, y)

'''
    if t[possibleX[i]-1][possibleY[i]-1] == t[possibleX[i]-1][possibleY[i]] == t[possibleX[i]-1][possibleY[i]+1] == 7:
        if t[possibleX[i]][possibleY[i]-1] == t[possibleX[i]+1][possibleY[i]-1] == t[possibleX[i]+1][possibleY[i]] == 7:
            if t[possibleX[i]+1][possibleY[i]+1] == t[possibleX[i]][possibleY[i]+1] == 7:
                x = possibleX[i] + 1
                y = possibleY[i] + 1
'''
