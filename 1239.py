while True:
    try:
        ph = input()
        i = 0
        b = 0
        res = ''
        for j in range(len(ph)):
            
            if(ph[j] == '_'):
                if(i == 0):
                    res += '<i>'
                    i = 1
                else:
                    res += '</i>'
                    i = 0
            
            elif(ph[j] == '*'):
                if(b == 0):
                    res += '<b>'
                    b = 1
                else:
                    res += '</b>'
                    b = 0
                    
            else:
                res += ph[j]
                
        print(res)
        
    except EOFError:
        break