turma = 1
while True:
    n = int(input())
    if n == 0:
        break

    c = []
    while n:
        n -= 1
        c.append([int(x) for x in input().split()])

    maior = max([x[1] for x in c])
    estagio = [str(x[0]) for x in c if x[1] == maior]

    print('Turma %d' % turma)
    print(' '.join(estagio), '')
    print()
    turma += 1
