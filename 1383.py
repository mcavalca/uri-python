def is_sudoku(matriz):

    for linha in matriz:
        check = [0] * 9
        for elemento in linha:
            check[elemento - 1] += 1
            if check[elemento - 1] > 1:
                return 'NAO'
    return 'SIM'



n = int(input())
for i in range(n):
    sudoku = []
    for linha in range(9):
        sudoku.append([int(x) for x in input().split()])
    print(sudoku)
    saida = is_sudoku(sudoku)
    print('Instancia %d' % (i+1))
    print(saida)
    print()
