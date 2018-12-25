while True:
    a, d = [int(x) for x in input().split()]
    if not (a or d):
        break
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    b.sort()
    c.sort()
    if (b[0] >= c[1]):
        print('N')
    else:
        print('Y')
