n = int(input())
n -= 1
x = input().split()
for i in enumerate(x):
    x[i[0]] = int(x[i[0]])

i = 0
if(x[i]%2 == 0):
    j = -1
else:
    j = 1
while(i >= 0 and i <= n):
    
    i += j