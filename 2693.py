while True:
    try:
        q = int(input())
        a = []
        while q:
            q -= 1
            a.append(input().split())
            a[-1][2] = int(a[-1][2])
        a.sort(key=lambda x: (x[2], x[1], x[0]))
        for nome in a:
            print(nome[0])

    except EOFError:
        break
