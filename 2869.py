c = int(input())
while c > 0:
    c -= 1
    n = int(input())
    for i in range(1, 1000000000000000000):
        l = []
        for j in range(1, i+1):
            if i % j == 0:
                l.append(j)
        if len(l) == n:
            break
    print(i)
