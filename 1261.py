hay_point = {}

m, n = [int(x) for x in input().split()]

while m:
    m -= 1
    cargo, salario = input().split()
    hay_point[cargo] = int(salario)

while n:
    n -= 1
    salario = 0
    descricao = input().split()
    ponto = input()
    for palavra in descricao:
        try:
            salario += hay_point[palavra]
        except KeyError:
            continue

    print(salario)
