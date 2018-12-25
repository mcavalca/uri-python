while True:
    try:
        n, k = [int(x) for x in input().split()]
        notas = [int(x) for x in input().split()]
        notas.sort()
        maior = 0
        maior = sum(notas[n-k:n])
        print(maior%1000000007)

    except EOFError:
        break
