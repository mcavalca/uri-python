while True:
    try:
        t = int(input())
        n = 0
        c = 0

        for i in range(t):
            m1, m2 = input().split()
            c += int(m2)
            n += int(m1)*int(m2)

        ira = n/(c*100)
        print('%.4f' % ira)
    except EOFError:
        break