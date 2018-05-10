while True:
    try:
        n, iden = input().split()
        qt = 0
        n = int(n)
        while n > 0:
            n -= 1
            j, g = input().split()
            if j == iden and g == '0':
                qt += 1
        print(qt)
        
    except EOFError:
        break