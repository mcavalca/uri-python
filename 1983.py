n = int(input())
m = 0.0
al = 0
while(n > 0):
    n -= 1
    a, b = input().split()
    if float(b) > m:
        m = float(b)
        al = int(a)
        
if m >= 8:
    print(al)
else:
    print("Minimum note not reached")