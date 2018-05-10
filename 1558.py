import math
    
while True:
    try:
        n = int(input())
        s = 'NO'
        x = 0
        '''
        if n > 0:
            x = int(math.sqrt(n))+1
        '''
        if n < 3:
            s = 'YES'
        elif n % 4 == 1:
            s = 'YES'
        '''
        for i in range(0, x):
            for j in range(0, int(math.sqrt(n-x+1))+1):
                if n == i**2 + j**2:
                    s = 'YES'
                    break
        '''
        print(s)
        
    except EOFError:
        break