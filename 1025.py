caso = 0
while True:
    n, q = [int(x) for x in input().split()]
    if n == q == 0:
        break
    caso += 1
    marmore = [0]
    while n > 0:
        n -= 1
        marmore.append(int(input()))
    marmore.sort()
    print('CASE# %d:' % (caso))
    while q > 0:
        q -= 1
        n = int(input())
        if n in marmore:
            print('%d found at %d' %(n, marmore.index(n)))
        else:
            print('%d not found' % n)
