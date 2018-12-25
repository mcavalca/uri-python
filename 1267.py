while True:
    n, d = input().split()
    if n == '0' and d == '0':
        break
    l = []
    s = 'no'
    jantar = [0] * int(n)
    for i in range(int(d)):
        l.append([int(x) for x in input().split()])
        for j in range(int(n)):
            if l[i][j] == 1:
                jantar[j] += 1
    if jantar.count(int(d)) > 0:
        s = 'yes'
    print(s)
