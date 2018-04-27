n = int(input())
while(n > 0):
    n -= 1
    l = []
    m = int(input())
    while(m > 0):
        m -= 1
        l.append(input())
    main = l[0]
    for m in l:
        if m != main:
            main = 'ingles'
            break
    print(main)