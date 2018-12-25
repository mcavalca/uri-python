while True:
    try:
        c, k = [int(x) for x in input().split()]
        comb = [[] * c] 
        print(comb)
        p = []

        for i in range(c):
            p.append(input())
            s = int(input())
            for j in range(s):
                comb[i].append[input()]

        print(p)
        print(comb)

    except EOFError:
        break
