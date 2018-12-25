cont = 1
while True:
    try:
        n = input()
        calc = input().split()
        if cont > 1:
            print()
        f = m = pares = 0
        for i in range(0, len(calc), 2):
            if calc[i] == n:
                pares += 1
                if calc[i + 1] == 'F':
                    f += 1
                else:
                    m += 1

        print('Caso %d:' % cont)
        print('Pares Iguais: %d' % pares)
        print('F: %d' % f)
        print('M: %d' % m)
        cont += 1

    except EOFError:
        break
