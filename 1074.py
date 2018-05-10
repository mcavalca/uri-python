n = int(input())
while n > 0:
    saida = ''
    n -= 1
    i = int(input())
    if i == 0:
        saida += 'NULL'
    elif i % 2 == 0:
        saida += 'EVEN '
    elif i % 2 == 1:
        saida += 'ODD '
    if i > 0:
        saida += 'POSITIVE'
    if i < 0:
        saida += 'NEGATIVE'
    print(saida)