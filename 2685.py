while True:
    try:
        n = int(input())
        if (n >= 0 and n < 90) or n == 360:
            print('Bom Dia!!')
        elif n >=90 and n < 180:
            print('Boa Tarde!!')
        elif n >= 180 and n < 270:
            print('Boa Noite!!')
        else:
            print('De Madrugada!!')
        
    except EOFError:
        break