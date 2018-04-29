n = int(input())

for i in range(1, n+1):
    m, c = input().split()
    
    if c == 'bin':
        a = int(m, 2)
        b = hex(int(m, 2))
        b = b[2::]
        ca = 'dec'
        cb = 'hex'
    elif c == 'dec':
        a = hex(int(m))
        a = a[2::]
        b = bin(int(m))
        b = b[2::]
        ca = 'hex'
        cb = 'bin'
    elif c == 'hex':
        a = int(m, 16)
        b = bin(int(m, 16))
        b = b[2::]
        ca = 'dec'
        cb = 'bin'
    
    print('Case %s:' % i)
    print('%s %s' % (a, ca))
    print('%s %s' % (b, cb))
    print()