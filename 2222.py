for t in range(int(input())):
    conjunto = []
    for n in range(int(input())):
        conjunto.append(set(input().split()[1:]))

    for q in range(int(input())):
        op = [int(x) for x in input().split()]
        if op[0] == 1:
            resultado = conjunto[op[1] - 1] & conjunto[op[2] - 1]
        elif op[0] == 2:
            resultado = conjunto[op[1] - 1] | conjunto[op[2] - 1]
        print(len(resultado))
