while True:
    s, b = [int(x) for x in input().split()]
    if s == b == 0:
        break
    dir = 0
    esq = s+1
    while b:
        b -= 1
        l, r = [int(i) for i in input().split()]
        l -= 1
        r += 1

        if (dir != '*') and (r > dir):
            dir = r
            if dir > s:
                dir = '*'

        if (esq != '*') and (l < esq):
            esq = l
            if esq < 1:
                esq = '*'

        print(esq, dir)
        '''
        l -= 1
        sold = sold[:l] + [0] * (r - l) + sold[r:]
        while l >= 0 and sold[l] == 0:
            l -= 1
        while  r < s and sold[r] == 0:
            r += 1
        l += 1
        r += 1
        if l <= 0:
            l = '*'
        if r > s:
            r = '*'
        '''
    print('-')
