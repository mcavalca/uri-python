while True:
    n, d = input().split()
    if n == '0' and d == '0':
        break
    l = []
    for i in range(int(d)):
        l.append([int(x) for x in input().split()])
    s = 'no'
    for j in range(int(n)):
        print(l[:][j], end = ' ')
        if all(l[j][:]) and l[j][:] == 1:
            s = 'yes'
            break
    print(s)