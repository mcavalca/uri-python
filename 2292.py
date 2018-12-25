
for i in range(int(input())):
    stat, n = input().split()
    binario = ''
    for led in stat:
        if led == 'X':
            binario += '0'
        else:
            binario += '1'
    binario = bin(int(binario[::-1], 2) + int(n))
    print(binario)
    binario = str(binario)[:1:-1]
    saida = ''
    for led in range(len(stat)):
        if binario[led] == '1':
            saida += 'O'
        else:
            saida += 'X'
    print(saida)
