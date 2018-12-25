from fractions import gcd

n = int(input())
for i in range(1, n + 1):
    s1 = int(input(), 2)
    s2 = int(input(), 2)
    if gcd(s1, s2) != 1:
        s1 = 'All you need is love!'
    else:
        s1 = 'Love is not all you need!'
        
    print('Pair #%d: %s' % (i, s1))
