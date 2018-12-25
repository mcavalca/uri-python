while True:
    n = int(input())
    if n == 0:
        break
    conjunto = []
    prefixo = 0
    while n:
        n -= 1
        conjunto.append(input())
        if not prefixo:
            for palavra in range(len(conjunto) - 1):
                if (conjunto[-1] in conjunto[palavra]) or (conjunto[palavra] in conjunto[-1]):
                    prefixo = 1
                    break

    if prefixo:
        print('Conjunto Ruim')
    else:
        print('Conjunto Bom')
