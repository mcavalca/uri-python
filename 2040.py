while True:
    n = int(input())
    if n == 0:
        break
    time = {}
    for i in range(n):
        entrada = input().split()
        time[entrada[0]] = int(entrada[1])
    for i in range(n//2):
        jogo = input().split()
        ponto = [int(i)*3 for i in jogo[1].split('-')]
        if ponto[0] > ponto[1]:
            a = 5
            b = 0
        elif ponto[0] < ponto[1]:
            a = 0
            b = 5
        else:
            a = b = 1
        time[jogo[0]] += ponto[0] + a
        time[jogo[2]] += ponto[1] + b

    vencedor = [max(time, key=time.get), max(time.values())]
    if vencedor[0] == 'Sport':
        print('O Sport foi o campeao com %d pontos :D' % vencedor[1])
    else:
        print('O Sport nao foi o campeao. O time campeao foi o % com %d pontos :(' % (vencedor[0], vencedor[1]))
    print()
