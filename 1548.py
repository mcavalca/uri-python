n = int(input())
while n > 0:
    n -= 1
    m = int(input())
    a = input().split()
    for ind, i in enumerate(a):
        a[ind] = int(a[ind])
    b = sorted(a)
    b.reverse()
    total = 0
    for ind, i in enumerate(a):
        if (a[ind] == b[ind]):
            total +=1
    print(total)