instancia = 1
while True:
    try:
        n = int(input())
        menor = 11
        repr = ''
        while n:
            n -= 1
            nome, nota = input().split()
            if int(nota) == menor and repr < nome:
                repr = nome
                menor = int(nota)
            elif int(nota) < menor:
                repr = nome
                menor = int(nota)

        print('Instancia %d' % instancia)
        print(repr)
        print()
        instancia += 1

    except EOFError:
        break
