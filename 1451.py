while True:
    try:
        texto = input()
        tam = len(texto)
        ponto = 1
        palavra = ''
        temp = ''
        for letra in range(tam):
            ch = texto[letra]
            if ch != '[' and ch != ']':
                if ponto:
                    palavra += ch
                else:
                    temp += ch
            if ch == '[':
                if ponto:
                    ponto = 0
                else:
                    palavra = temp + palavra
                    temp = ''
            elif ch == ']':
                ponto = 1
                palavra = temp + palavra
                temp = ''

        if temp:
            palavra = temp + palavra
        print(palavra)


    except EOFError:
        break
