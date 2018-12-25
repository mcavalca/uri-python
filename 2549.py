while True:
    try:
        n, a = input().split()
        n = int(n)
        lista = []
        for aluno in range(n):
            nome = input().split()
            inicial = ''
            for i in nome:
                inicial += i[0]
            inicial += a
            if inicial not in lista:
                lista.append(inicial)
        fora = n - len(lista)
        print(fora)

    except EOFError:
        break
