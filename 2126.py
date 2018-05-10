caso = 1
while True:
    try:
        n1 = input()
        n2 = input()
        print('Caso #%d:' % caso)
        qt = n2.count(n1)
        if qt == 0:
            print('Nao existe subsequencia')
        else:
            print('Qtd.Subsequencias: %d' % qt)
            qt = n2.rfind(n1)
            print('Pos: %d' % (int(qt)+1))
        print()
        caso += 1
        
    except EOFError:
        break