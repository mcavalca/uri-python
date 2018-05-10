def jos(k, j):
    if k == 1:
        return 0
    else:
        return (jos(k-1, j) + j) % k + 1
    

n = int(input())
for i in range(n):
    k, j = input().split()
    k = int(k)
    j = int(j)
    result = jos(k, j)
    print('Case %d: %d'%(i+1, result))
    