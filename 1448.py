n = int(input())
for i in range(n):
    frase = input()
    p1 = p2 = 0
    time1 = input()
    time2 = input()
    tam = len(frase)
    for letra in range(tam):
        if (letra < len(time1)) and (frase[letra] == time1[letra]):
            p1 += 1
        if (letra < len(time2)) and (frase[letra] == time2[letra]):
            p2 += 1

    print('Instancia %d' % (i + 1))
    if p1 > p2:
        print('time 1')
    elif p2 > p1:
        print('time 2')
    else:
        print('empate')
    print()
