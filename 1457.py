t = int(input())

while t > 0:
    t -= 1
    f = input()
    n = ''
    k = 0
    
    while True:
        if(f[k] != '!'):
            n += f[k]
            k += 1
        else:
            n = int(n)
            k = len(f) - k
            break
    
    f = 1
    for i in range(n, 1, -k):
        f *= i
    print(f)