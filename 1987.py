while True:
    try:
        n, m = input().split()
        r = 0
        for i in range(len(m)):
            r += int(m[i])
        m = str(r)
        print(m, end=' ')
        if int(m) % 3 == 0:
            print('sim')
        else:
            print('nao')
        
    except EOFError:
        break