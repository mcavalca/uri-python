def maior_lucro(dia):
    max_menor = max_maior = dia[0]
    for i in dia[1:]:
        max_menor = max(i, max_menor + i)
        max_maior = max(max_maior, max_menor)
    return max_maior

while True:
    try:
        n = int(input())
        custo = int(input())
        dia = []
        while n:
            n -= 1
            dia.append(int(input()) - custo)
        lucro = maior_lucro(dia)
        if lucro < 0:
            lucro = 0
        print(lucro)

    except EOFError:
        break
