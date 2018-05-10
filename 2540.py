while True:
    try:
        n = int(input())
        v = input().split()
        v = v.count('1')
        if v/n >= 2/3:
            print('impeachment')
        else:
            print('acusacao arquivada')
        
    except EOFError:
        break