n = int(input())
while n > 0:
    n -= 1
    m = int(input())
    lista = sorted(input().split())
    impares = []
    for x in lista:
        if int(x) % 2 == 1:
            impares.append(x)
    m = len(impares)-1
    lista = []
    for x in range(m/2):
        lista.append()
    print(lista)
