import math

while True:
    try:
        w = input()
        n = int(input())
        tot = 0
        check = n
        for i in range(len(w)):
            if w[i] == 'R':
                
                if check == n:
                    tot += 1
                    
                if(check == 0):
                    check = n
                    tot += 1
                    
                check -= 1
            elif w[i] == 'W':
                tot += 1
                check = n
        print(tot)
        
    
    except EOFError:
        break