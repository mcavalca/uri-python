while True:
    try:
        n = int(input())
        l = [int(x) for x in input().split()]
        c = [int(x) for x in input().split()]
        ult = 0
        '''
        for x in l:
            if l.index(x)-c.index(x) > 0:
                ult += l.index(x)-c.index(x)
        '''
        while len(l) > 0:
            print(l[0], c.index(3))
            ult += abs(l[0]-c.index(l[0]))
            l.pop()
            c.pop(c.index(l[0]))
        print(ult)
        
    except EOFError:
        break