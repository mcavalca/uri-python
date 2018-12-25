while True:
    b, n = input().split()
    if b == n == '0':
        break
    r = [int(x) for x in input().split()]
    for i in range(int(n)):
        d, c, v = input().split()
        r[int(d)-1] -= int(v)
        r[int(c)-1] += int(v)
    saida = 'S'
    for i in r:
        if int(i) < 0:
            saida = 'N'
            break
    print(saida)
