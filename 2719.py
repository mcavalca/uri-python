t = int(input())
while t:
    t -= 1
    n, m = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]
    viagem = 1
    i = 1
    peso = p[0]
    while i < n:
        if peso + p[i] > m:
            viagem += 1
            peso = p[i]
        else:
            peso += p[i]

        i += 1

    print(viagem)
