n = int(input())
while n > 0:
    n -= 1
    ra = input()
    saida = 'INVALID DATA'
    if len(ra) == 20:
        if ra[0:2] == 'RA':
            if ra[2:].isdigit():
                saida = int(ra[2:])
    print(saida)
