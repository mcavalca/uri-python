while True:
    n, m = input().split()
    if n == m == '0':
        break

    linha = []
    for x in range(int(n)):
        linha.append(input())
    a, b = input().split()
    a = int(int(a)/int(n))
    b = int(int(b)/int(m))
    redim = []

    for x in linha:
        r = ''
        for y in x:
            r += y * b
        for y in range(int(a)):
            redim.append(r)

    for x in redim:
        print(x)

    print()
