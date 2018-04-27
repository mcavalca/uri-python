while True:
    try:
        n = int(input())
        s = int(n/3)
        e = n-s
        
        # FILL WITH 0
        m = [[0 for i in range(n)] for j in range(n)]
        
        # FILL WITH 2
        for i in range(n):
            m[i][i] = 2
            
        # FILL WITH 3
        j = 0
        for i in range(n-1,-1,-1):
            m[j][i] = 3
            j += 1
            
        # FILL MIDDLE WITH 1
        for i in range(s, e):
            for j in range(s, e):
                m[i][j] = 1
        
        m[int(n/2)][int(n/2)] = 4
        
        for i in range(n):
            for j in range(n):
                print(m[j][i], end='')
            print()
        print()
    
    except EOFError:
        break