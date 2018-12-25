n = int(input())
dado = [1, 2, 3, 4, 5, 6]
while n > 0:
    n -= 1
    c = []
    c.append(int(input()))
    x = input().split()
    for i in x:
        c.append(int(i))
    c.append(int(input()))
    d = sorted(c)
    if (d != dado) or (c[0]+c[5] != 7) or (c[1]+c[3]!=7) or (c[2]+c[4] != 7):
        print('NAO')
    else:
        print('SIM')