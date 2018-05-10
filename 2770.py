while True:
    try:
        x, y, m = input().split()
        for i in range(int(m)):
            xi, yi = input().split()
            if int(xi)*int(yi) <= int(x)*int(y):
                print('Sim')
            else:
                print('Nao')
        
    except EOFError:
        break