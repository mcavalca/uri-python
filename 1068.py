while True:
    try:
        p = input()
        d = 0
        for i in range(len(p)):
            if(p[i]=='('):
                d += 1
            elif(p[i]==')'):
                d -= 1
            if(d < 0):
                break
        if(d != 0):
            print('incorrect')
        else:
            print('correct')
        
    except EOFError:
        break