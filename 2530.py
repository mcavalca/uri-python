while True:
    try:
        n, m = [int(i) for i in input().split()]
        juan = [int(i) for i in input().split()]
        ric = [int(i) for i in input().split()]
        i = j = 0
        colou = 0
        while j < n:
            if juan[j] == ric[i]:
                i += 1
                if i == m:
                    colou = 1
                    break
            j += 1
        if colou:
            print('sim')
        else:
            print('nao')

    except EOFError:
        break
