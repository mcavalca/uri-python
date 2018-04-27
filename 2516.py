while True:
    try:
        s, va, vb = input().split()
        if(int(va) <= int(vb)):
            print('impossivel')
        else:
            t = int(s)/(int(va)-int(vb))
            print('%.2f' % t)
    except EOFError:
        break