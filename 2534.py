while True:
    try:
        n, q = [int(x) for x in input().split()]
        cid = []
        while n:
            n -= 1
            cid.append(int(input()))
        cid.sort(reverse=True)
        while q:
            q -= 1
            p = input()
            print(cid[int(p) - 1])


    except EOFError:
        break
