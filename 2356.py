while True:
    try:
        d = input()
        s = input()
        if s in d:
            print('Resistente')
        else:
            print('Nao resistente')
        
    except EOFError:
        break