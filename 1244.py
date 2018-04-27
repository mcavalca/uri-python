n = int(input())
while n > 0:
    n -= 1
    c = input().split()
    c.sort(key=len, reverse=True)
    for i in range(len(c)):
        print(c[i], end = '')
        if i != len(c)-1:
            print(' ', end = '')
    print()