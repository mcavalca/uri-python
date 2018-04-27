f = []
b = []
n = int(input())
for i in range(n):
    f.append(input().split())
    for j in range(n):
        f[i][j] = int(f[i][j])
        
for i in range(n*2):
    x, y = input().split()
    b.append(f[int(x)-1][int(y)-1])
b = set(b)
    
print(len(b))