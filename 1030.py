from collections import deque
def jos(k, j):
    d = deque(k)
    while len(d) > 1:
        d.rotate(-j)
        d.pop()
    return(d.pop())


n = int(input())
for i in range(n):
    k, j = input().split()
    k = [x for x in range(1, int(k)+1)]
    j = int(j)
    result = jos(k, j)
    print('Case %d: %d'%(i+1, result))
