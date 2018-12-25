while True:
    n = int(input())
    if n == 0:
        break
    menor = 9999
    prim = ''
    while n > 0:
        n -= 1
        p, a, d = input().split()
        if menor > int(a)-int(d):
            menor = int(a)-int(d)
            prim = p
    print(prim)
