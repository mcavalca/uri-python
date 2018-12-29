while True:
    try:
        n, l, c = [int(x) for x in input().split()]
        w = input()
        page = 1
        line = 0
        ch = 0
        tam = len(w)
        i = 0

        while i < tam:
            while w[i] == ' ' and (ch == 0 or ch == c):
                i += 1
            # print(w[i], ' --- ', i, page, line, ch)
            if ch == c:
                line += 1
                ch = 0
            if line == l:
                page += 1
                line = 0
            i += 1
            ch += 1

        print(page)

    except EOFError:
        break
