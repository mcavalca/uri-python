n = int(input())
for i in range(n):
    k, j = input().split()
    l = []
    for m in range(int(k)):
        l.append(m+1)
    while(len(l) > 1):
        for m in range(1, int(j)):
            l.append(l[0])
            l.pop(0)
        l.pop(0)
    print('Case %d: %d'%(i+1, l[0]))
    