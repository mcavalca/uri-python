while True:
    try:
        c = []
        c = (input().lower()).split()
        t = 0
        y = 0
        for i, j in enumerate(c):
            c[i] = j[0]
            if c[i] == c[i-1] and y == 0:
                y = 1
                t += 1
            elif c[i] != c[i-1]:
                y = 0
                
        print(t)
        
        
    except EOFError:
        break