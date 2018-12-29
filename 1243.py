while True:
    try:
        enunciado = input().split()

        palavra = 0
        while palavra < len(enunciado):

            if any(ch.isdigit() for ch in enunciado[palavra]):
                del enunciado[palavra]
                palavra -= 1
            elif enunciado[palavra].count('.') > 1:
                del enunciado[palavra]
                palavra -= 1

            palavra += 1

        comprimento = 0
        for palavra in enunciado:
            if (palavra.count('.') == 0) or (palavra.index('.') == len(palavra) - 1):
                comprimento += len(palavra)
                if '.' in palavra:
                    comprimento -= 1

        if len(enunciado):
            comprimento = comprimento//len(enunciado)

        if comprimento <= 3:
            pontos = 250
        elif comprimento <= 5:
            pontos = 500
        else:
            pontos = 1000

        print(pontos)

    except EOFError:
        break
