from math import sqrt
pi = 3.1415926535897

while True:
    try:
        a, b, c = [int(x) for x in input().split()]
        p = (a + b + c)/2
        triangulo = sqrt(p * (p - a) * (p - b) * (p - c))
        raio = sqrt(((p - a) * (p - b) * (p - c))/p)
        rosas = pi * raio**2

        raio = (a * b * c) / sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))
        girassois = (pi * raio**2) - triangulo
        violetas = triangulo - rosas
        
        print('%.4f %.4f %.4f' % (girassois, violetas, rosas))

    except EOFError:
        break
