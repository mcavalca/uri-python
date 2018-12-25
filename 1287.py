def strtoint(palavra):
    inteiro = ''
    lista_int = '1234567890'
    check = 0
    for letra in palavra:
        if letra in lista_int:
            inteiro += letra
        else:
            if letra == 'l':
                inteiro += '1'
            elif letra == 'o' or letra == 'O':
                inteiro += '0'
            elif letra != ',' and letra != ' ':
                check = 1
                break

    try:
        inteiro = int(inteiro)
        if inteiro > 2147483647:
            check = 1
    except ValueError:
        inteiro = 'error'

    if check:
        inteiro = 'error'

    return inteiro

while True:
    try:
        entrada = input()
        entrada = strtoint(entrada)
        print(entrada)
    except EOFError:
        break
