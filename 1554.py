from math import sqrt

c = int(input())
while c:
    c -= 1
    n = int(input())
    x, y = [int(i) for i in input().split()]
    perto = 999999999

    for cont in range(n):
        n -= 1
        xb, yb = [int(i) for i in input().split()]
        d = sqrt(abs(x - xb)**2 + abs(y - yb)**2)
        if d < perto:
            perto = d
            pos = cont + 1

    print(pos)
