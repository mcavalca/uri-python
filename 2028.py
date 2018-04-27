cases = 1
while True:
    try:
        n = int(input())
        f = ['0']
        for i in range(n+1):
            for j in range(i):
                f.append(i)
        print('Caso %d: %d numero'%(cases, len(f)), end ='')
        if(n != 0):
            print('s', end='')
        print()
        for i in range(len(f)):
            print(f[i], end = '')
            if(i != len(f)-1):
                print(' ', end = '')
            else:
                print()
        print()
        cases += 1
        
    except EOFError:
        break