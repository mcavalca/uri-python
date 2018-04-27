while True:
    n = int(input())
    if(n == 0):
        break
    l = input().split()
    for i in range(n):
        l[i] = int(l[i])
        
    r = sorted(l, key=int)
    for ind, i in enumerate(l):
        if i == r[n-2]:
            print(ind+1)
            break
    