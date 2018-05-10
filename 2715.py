while True:
    try:
        n = int(input())
        t = [int(x) for x in input().split()]
        i = 2
        dif = sum(t[i:]) - sum(t[:i])
        while(True):
            i += 1
            new = sum(t[i:]) - sum(t[:i])
            if new < 0:
                break;
            dif = new
        print(dif)
    except EOFError:
        break