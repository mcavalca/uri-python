while True:
    try:
        n, m = input().split()
        qt = 0
        for x in range(int(n), int(m)+1):
            if len(set(list(str(x)))) == len(str(x)):
                qt += 1
        print(qt)
                
        
    except EOFError:
        break