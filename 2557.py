while True:
    try:
        conta = input()
        conta = conta.replace('=','+')
        conta = conta.split('+')
        if conta[0].isdigit() == False:
            resultado = int(conta[2]) - int(conta[1])
        elif conta[1].isdigit() == False:
            resultado = int(conta[2]) - int(conta[0])
        elif conta[2].isdigit() == False:
            resultado = int(conta[0]) + int(conta[1])
        print(resultado)

    except EOFError:
        break
