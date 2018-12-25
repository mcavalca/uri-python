while True:
    n, m = input().split()
    n, m = int(n), int(m)
    if n == m == 0:
        break
    carac = 4
    competidor = []
    for i in range(n):
        competidor.append([int(x) for x in input().split()])

    # Caracteristica 1
    # Ninguem resolveu todos
    for i in range(n):
        p = competidor[i].count(1)
        if p == m:
            carac -= 1
            break

    # Caracteristica 2
    # Todo problema foi resolvido por pelo menos 1
    problema = [0] * m
    for i in range(n):
        for j in range(m):
            if competidor[i][j] == 1:
                problema[j] += 1
    if problema.count(0) > 0:
        carac -= 1

    # Caracteristica 3
    # Nao ha nenhum problema resolvido por todos

    for j in range(m):
        if problema[j] == n:
            carac -= 1
            break

    # Caracteristica 4
    # Todos resolveram pelo menos 1

    for i in range(n):
        p = competidor[i].count(0)
        if p == m:
            carac -= 1
            break

    print(carac)
