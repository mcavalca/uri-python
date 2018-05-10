while True:
    try:
        n = input()
        c = ''
        b1 = 0
        b2 = 0
        for i in range(9):
            if i%3 == 0 and i > 0:
                c += '.'
            c += n[i]
            b1 += int(n[i]) * (i+1)
            b2 += int(n[i]) * (9-i)
        c += '-'
        b1 = b1 % 11
        b2 = b2 % 11
        if b1 == 10:
            b1 = 0
        if b2 == 10:
            b2 = 0
            
        c += str(b1) + str(b2)
        
        print(c)
            
        
    except EOFError:
        break