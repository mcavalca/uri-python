n = int(input())
n -= 1
e = 0
y = [0 for i in range(n+1)]
x = [int(i) for i in input().split()]
e = sum(x)

i = 0
while x[i] != 0:
    if(x[i]%2 == 0):
        j = -1
    else:
        j = 1
    x[i] -= 1
    y[i] = 1
    i += j
    e -= 1
    if i > len(x)-1 or i < 0:
        break
    
print(y.count(1),e)