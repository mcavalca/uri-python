while True:
    try:
        n, amin, amax = [int(x) for x in input().split()]
        t = 0
        while n:
            n -= 1
            i = int(input())
            if i >= amin and i <= amax:
                t += 1
        print(t)

    except EOFError:
        break
