import math

while True:
    l, c, r1, r2 = [int(x) for x in input().split()]
    if (l == 0 and c == 0 and r1 == 0 and r2 == 0):
        break

    lc = (r1 + r1) * 2
    r1, r2 = r1 * 2, r2 * 2

    if l > c:
        if (l >= lc) and ((c >= r1) or (c >= r1)):
            print('S')
        else:
            print('N')

    elif c > l:
        print(c, lc, l, r1, r2)
        if (c >= lc) and ((l >= r1) or (l >= r2)):
            print('S')
        else:
            print('N')

    else:
        if (l >= lc) and ((c >= r1) or (c >= r2)):
            print('S')
        elif (c >= lc) and ((l >= r1) or (l >= r2)):
            print('S')
        else:
            print('N')
