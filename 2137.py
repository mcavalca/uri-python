while True:
    try:
        n = int(input())
        l = []
        while(n > 0):
            n -= 1
            l.append(input())
        l.sort()
        for n in l:
            print(n)
        
    except EOFError:
        break