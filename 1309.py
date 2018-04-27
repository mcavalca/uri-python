while True:
    try:
        mon = '$'
        temp = ''
        dolar = input()
        j = 1
        for t, i in enumerate(reversed(dolar)):
            temp += i
            if(((t+1)%3 == 0) and (t != len(dolar)-1)):
                temp += ','
            j += 1
        mon += temp[::-1]
        cent = input()
        if(len(cent) < 2):
            cent += '0'
            cent = cent[::-1]
        mon += '.' + cent
        print(mon)
        
    except EOFError:
        break