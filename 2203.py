from math import sqrt, pow

while True:
    try:
        xf, yf, xi, yi, vi, r1, r2 = [int(x) for x in input().split()]
        distancia = sqrt(pow((xf - xi), 2) + pow((yf - yi), 2))
        if (r1 + r2) >= (distancia) + 1.5 * vi:
            print('Y')
        else:
            print('N')
    except EOFError:
        break
