c = int(input())
while c > 0:
    c -= 1
    total = []
    n = int(input())

    while n > 0:
        n -= 1
        palavra = input().split()
        if palavra[1] == 'chirrin':
            if palavra[0] not in total:
                total.append(palavra[0])
        elif palavra[1] == 'chirrion':
            if palavra[0] in total:
                total.remove(palavra[0])

    total.sort()
    print('TOTAL')
    for tausfo_tem in total:
        print(tausfo_tem)
