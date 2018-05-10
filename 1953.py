while True:
    try:
        n = int(input())
        epr = 0
        ehd = 0
        intruso = 0
        for i in range(n):
            l, curso = input().split()
            if curso == 'EPR':
                epr += 1
            elif curso == 'EHD':
                ehd += 1
            else:
                intruso += 1
        
        print('EPR: %d' % epr)
        print('EHD: %d' % ehd)
        print('INTRUSOS: %d' % intruso)
        
    except EOFError:
        break