from math import pi, sqrt

while True:
    try:
        lado = float(input())
        borda = (- lado) * lado * (3 * (sqrt(3) - 4) + 2 * pi) / 3
        estrela = 4 * (lado * lado * (1 - pi/4) - (borda) / 2)
        centro = lado * lado - estrela - borda
        print('%.3f %.3f %.3f' % (centro, estrela, borda))
    except EOFError:
        break
