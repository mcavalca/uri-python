while True:
    try:
        n = input()
        m = [0] * 10
        for i in n:
            m[int(i)] += 1

        print(9 - m[::-1].index(max(m)))
    except EOFError:
        break
