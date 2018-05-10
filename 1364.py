while True:
    n, m = input().split()
    emote = []
    qt = 0
    if n == '0' and m == '0':
        break
    for i in range(int(n)):
        emote.append(input())
    for i in range(int(m)):
        c = input()
        print(emote)
        print(c)
        for x in emote:
            qt += c.count(x)
            c = c.replace(x, ' ')
    print(qt)