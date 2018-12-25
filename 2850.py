while True:
    try:
        c = input()
        if c == 'esquerda':
            print('ingles')
        elif c == 'direita':
            print('frances')
        elif c == 'nenhuma':
            print('portugues')
        elif c == 'as duas':
            print('caiu')

    except EOFError:
        break
