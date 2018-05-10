while True:
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(n):
        l.append(' '.join(input().split()))
    
    m = max(len(i) for i in l)
    for i in range(len(l)):
        for j in range(m-len(l[i])):
            print(' ', end = '')
        print(l[i])
    print()