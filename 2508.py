import string
letras = list(string.ascii_lowercase)
l1 = letras[:9]
l2 = letras[9:18]
l3 = letras[18:]
while True:
    try:
        nome = input().lower()
        valor = 0
        for x in nome:
            if x in l1:
                valor += l1.index(x) + 1
            elif x in l2:
                valor += l2.index(x) + 1
            elif x in l3:
                valor += l3.index(x) + 1

        valor = str(valor)
        while len(valor) > 1:
            total = 0
            for x in valor:
                total += int(x)
            valor = str(total)
        print(valor)
    except EOFError:
        break
