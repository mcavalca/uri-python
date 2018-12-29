# Fill
m = [[0 for x in range(500)] for y in range(500)]

q = int(input())
while q:
    q -= 1

    try:
        entrada = input().split()
        u = entrada[0]
        x = int(entrada[1]) - 1
        y = int(entrada[2]) - 1
        z = int(entrada[3])
        w = int(entrada[4])
        v = int(entrada[5])
    except IndexError:
        pass

    if u == 'U':
        for i in range(x, z):
            for j in range(y, w):
                m[i][j] += v
    elif u == 'A':
        print(m[x][y])
