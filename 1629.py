while True:
    n = int(input())
    if n == 0:
        break
    while n > 0:
        n -= 1
        um = 0
        zero = 0
        linha = input()
        for i in range(len(linha)):
            if i % 2 == 0:
                zero += int(linha[i])
            else:
                um += int(linha[i])
        resultado = 0
        while (zero):
            resultado += (zero % 10)
            zero = int(zero/10)
        while (um):
            resultado += (um % 10)
            um = int(um/10)
        print(resultado)
