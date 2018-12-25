while True:
    try:
        texto = input().split('-')
        cobol = ''
        for palavra in texto:
            i = palavra[0].lower()
            f = palavra[len(palavra) - 1].lower()
            if len(cobol) == 0 and (i == 'c' or f == 'c'):
                cobol += 'c'
            elif len(cobol) == 1 and (i == 'o' or f == 'o'):
                cobol += 'o'
            elif len(cobol) == 2 and (i == 'b' or f == 'b'):
                cobol += 'b'
            elif len(cobol) == 3 and (i == 'o' or f == 'o'):
                cobol += 'o'
            elif len(cobol) == 4 and (i == 'l' or f == 'l'):
                cobol += 'l'

        if cobol == 'cobol':
            print('GRACE HOPPER')
        else:
            print('BUG')
    except EOFError:
        break
