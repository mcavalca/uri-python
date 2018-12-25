while True:
    try:
        t = int(input())
        pol = input().split(' + ')
        der = []
        for i in pol:
            x = i.split('x')
            valor = int(x[0]) * int(x[1])
            if (int(x[1]) - 1) != 1:
                der.append(str(valor) + 'x' + str(int(x[1]) - 1))
            else:
                der.append(str(valor) + 'x')
        der = ' + '.join(der)
        print(der)

    except EOFError:
        break
