while True:
    try:
        s = input()
        t = len(s)
        mi = False
        ma = False
        nu = False
        if((t > 32) or (t < 6)):
            print('Senha invalida.')
        else:
            for i in range(t):
                if(((ord(s[i]))>64) and ((ord(s[i]))<91)):
                    ma = True
                elif(((ord(s[i]))>96) and ((ord(s[i]))<123)):
                    mi = True
                elif(((ord(s[i]))>47) and ((ord(s[i]))<58)):
                    nu = True
                else:
                    ma = False
                    break
                
            if(ma and mi and nu):
                print('Senha valida.')
            else:
                print('Senha invalida.')
        
    except EOFError:
        break