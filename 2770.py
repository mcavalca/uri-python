while True:
    try:
        x, y, m = [int(i) for i in input().split()]
        while m:
            m -= 1
            xi, yi = [int(i) for i in input().split()]
             if (xi <= x and yi <= y) or (xi <= y and yi <= x):
                print('Sim')
            else:
                print('Nao')

    except EOFError:
        break
