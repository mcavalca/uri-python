n = int(input())
while n:
    n -= 1
    feira = {}
    final = 0.0

    m = int(input())
    while m:
        m -= 1
        item, valor = input().split()
        feira[item] = float(valor)

    p = int(input())
    while p:
        p -= 1
        item, qt = input().split()
        final += feira[item] * int(qt)

    print('R$ %.2f' % final)
