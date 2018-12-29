teste = 1
while True:
    n = int(input())
    if n == 0:
        break
    j1 = input()
    j2 = input()
    resultado = []
    while n:
        n -= 1
        a, b = [int(x) for x in input().split()]
        if (a + b) % 2 == 0:
            resultado.append(j1)
        else:
            resultado.append(j2)

    print('Teste %d' % teste)
    teste += 1
    for nome in resultado:
        print(nome)
    print()
