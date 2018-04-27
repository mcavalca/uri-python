while True:
    try:
        v = float(input())
        d = float(input())
        r = d/2
        area = 3.14*r*r
        alt = v/(r*r*3.14)
        print('ALTURA = %.2f' % alt)
        print('AREA = %.2f' % area)
        
    except EOFError:
        break
        