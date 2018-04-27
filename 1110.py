while True:
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(n):
        l.append(i+1)
    res = []
    while(len(l) > 1):
        res.append(l[0])
        l.pop(0)
        l.append(l[0])
        l.pop(0)
                
    print('Discarded cards: ', end='')
    for i in range(n-1):
        print(res[i], end='')
        if(i != n-2):
            print(', ', end='')
    print()
    print('Remaining card:', l[0])