from math import sqrt

while True:
    try:
        m1, m2, m3 = [float(x) for x in input().split()]
        # Area em funcao das medianas #
        sm = (m1 + m2 + m3) / 2.0
        try:
            area = 4 * sqrt(sm * (sm - m1) * (sm - m2) * (sm - m3)) / 3.0
        except ValueError:
            area = -1.0
        if area == 0:
            area = -1.0
        print('%.3f' % area)
    except EOFError:
        break
