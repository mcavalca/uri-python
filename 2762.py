while True:
    try:
        c = [int (x) for x in input().split('.')]
        c = c[::-1]
        c = '.'.join(str(x) for x in c)
        print(c)
        
    except EOFError:
        break