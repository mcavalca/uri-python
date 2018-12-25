while True:
    n = int(input())
    if n == 0:
        break
    a = [int(x) for x in input().split()]
    total = 0
    aux = 0
    i = 0
    while (a[i] != 0) or (a.count(0) == n):
        print(a)
        for j in range(i, n):
            if j != i:
                if (a[i] > 0 and a[j] < 0) or (a[i] < 0 and a[j] > 0):
                    total += (j - i) * a[i]
                    aux = a[i]
                    a[i] += a[j]
                    a[j] += aux
                    if(a[i] == 0):
                        i += 1
    print(a)
    print(total)
