i, d = input().split()
col = abs(ord(i[0]) - ord(d[0]))
lin = abs(int(i[1]) - int(d[1]))

if (col == 1 and lin == 2) or (col == 2 and lin == 1):
    print('VALIDO')
else:
    print('INVALIDO')
