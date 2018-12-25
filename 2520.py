while True:
    try:
        n, m = [int(x) for x in input().split()]
        matriz = []
        for i in range(n):
            matriz.append(input().split())

        a = [(index, j.index('2')) for index, j in enumerate(matriz) if '2' in j]
        b = [(index, j.index('1')) for index, j in enumerate(matriz) if '1' in j]

        x = (abs(a[0][0] - b[0][0]))
        y = (abs(a[0][1] - b[0][1]))
        print(x + y)

    except EOFError:
        break
