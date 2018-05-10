while True:
    try:
        alf = 'abcdefghijklmnopqrstuvwxyz'
        n = int(input())
        saida = ''
        while n > 0:
            l = input().split()
            pos = len(l[0]) + 3*(len(l)-1)
            saida += alf[pos-1]
            n -= 1
        for n in saida:
            print(n)
    except EOFError:
        break