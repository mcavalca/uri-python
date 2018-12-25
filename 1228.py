t = 3

while t:
    t -= 1
    n = int(input())
    l = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    ult = 0
    for i in range(n):
        for j in range(i, n):
            if (l[i] == c[j]):
                ult += (j - i)
                break
    print(ult)
