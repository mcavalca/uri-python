f = [1]
for i in range(1, 2**16):
    f.append(i+f[i-1])
    
n = int(input())

for i in range(n):
    m = int(input())
    print(f[m])