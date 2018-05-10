r = 'ABCDE*'
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        p = -1
        l = [int(x) for x in input().split()]
        for j in range(len(l)):
            if l[j] <= 127:
                if p != -1:
                    p = 5
                    break
                p = j
        print(r[p])