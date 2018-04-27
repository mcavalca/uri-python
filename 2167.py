n = int(input())
r = []
r = input().split()
q = 0
    
for i in range(1, n):
    if (int(r[i-1]) > int(r[i])):
        q = i + 1
        break
        
print(q)