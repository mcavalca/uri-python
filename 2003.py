while True:
    try:
        hora = input().split(':')
        n = int(hora[0])*60 + int(hora[1]) - 420
        if n < 0:
            n = 0
        print('Atraso maximo: %d' % n)
        
    except EOFError:
        break