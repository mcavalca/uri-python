c = int(input())
while c:
    c -= 1
    p = int(input())
    g = b = r = 0
    while p:
        p -= 1
        m, s = input().split()

        # GOLS #
        if m == 'G':
            if s == 'B':
                g += 2
            else:
                g += 1

        elif m == 'B':
            if s == 'R':
                b += 2
            else:
                b += 1

        elif m == 'R':
            if s == 'G':
                r += 2
            else:
                r += 1

        #------#

    if g == b == r:
        print('trempate')
    elif (g > b) and (g > r):
        print('green')
    elif (b > r) and (b > g):
        print('blue')
    elif (r > g) and (r > b):
        print('red')
    elif (g == r) or (r == b) or (b == g):
        print('empate')
