import math
while True:
    n = int(input())
    if n == 0:
        break
    bra = n/90
    ale = math.ceil((n*7)/90)
    print('Brasil %d x Alemanha %d' % (bra, ale))
