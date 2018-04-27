import math

def fp(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

while True:
    try:
        n = input()
        prime = fp(int(n))
        
        if prime:
            for i in range(len(n)):
                sup = fp(int(n[i]))
                if sup == False:
                    break
            if sup:
                print('Super')
                
            else:
                print('Primo')
                
        else:
            print('Nada')
    
    except EOFError:
        break