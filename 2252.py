while True:
    try:
        n = int(input())
        v = input().split()
        r = v.sort()
        print(v)

    except EOFError:
        break
