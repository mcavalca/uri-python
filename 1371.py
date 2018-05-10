while True:
    n = int(input())
    if n == 0:
        break
    l = []
    i = 1
    while(i**2 <= n):
        l.append(i**2)
        i += 1
    
    for i in range(len(l)):
        if i < len(l)-1:
            print('%d ' %l[i], end='')
        else:
            print('%d' %l[i])