i = 1
while True:
    r, n = [int(x) for x in input().split()]
    check = 1
    if n == r == 0:
        break

    if n >= r:
        print('Case %d: 0' % i)

    else:
        for j in range(1, 27):
            if n * (j + 1) >= r:
                print('Case %d: %d' % (i, j))
                check = 0
                break
        if check:
            print('Case %d: impossible' % i)

    i += 1
