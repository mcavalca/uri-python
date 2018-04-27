b = []
for i in range(32):
    if(i<10):
        b.append(i)
    else:
        b.append(chr(i+55))
    
while(True):
    ans = ''
    n = int(input())
    if(n == 0):
        break
    while(n > 31):
        i = int(n%32)
        ans += str(b[i])
        n /= 32
    ans += str(b[int(n)])
    ans = ans[::-1]
    print(ans)