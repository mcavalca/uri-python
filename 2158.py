c = 1
while True:
    try:
        fp, fh = input().split()
        lig = (5*int(fp)+6*int(fh))//2
        ato = (5*int(fp)+6*int(fh))//3
        ato = 2 + lig - int(fp) - int(fh)
        print('Molecula #%d.:.' % c)
        print('Possui %d atomos e %d ligacoes' % (ato, lig))
        print()
        c += 1
        
    except EOFError:
        break