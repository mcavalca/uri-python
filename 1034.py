t = int(input())
while t > 0:
    t -= 1
    n, m = input().split()
    blocos = [int(x) for x in input().split()]
    blocos.sort()
    qt = 0
    n = int(n)-1
    m = int(m)
    while m > 0:
        while m < blocos[n]:
            n -= 1
        m -= blocos[n]
        qt += 1
    print(qt)
        