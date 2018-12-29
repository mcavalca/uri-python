from math import sqrt

t = [int(x) for x in input().split()]
t.sort()
if (t[0] + t[1]) <= t[2] or (t[0] + t[2]) <= t[1] or (t[1] + t[2]) <= t[0]:
    print('n')
else:
    raiz = sqrt(t[0]**2 + t[1]**2)
    if raiz > t[2]:
        print('a')
    elif raiz == t[2]:
        print('r')
    else:
        print('o')
