teste = 1
while True:
    n = int(input())
    if n == 0:
        break
    valor = 0
    print('Teste %d' % teste)
    teste += 1
    while n:
        n -= 1
        j, z = [int(x) for x in input().split()]
        valor += (j - z)
        print(valor)

    print()
