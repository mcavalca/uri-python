while True:
    try:
        n = int(input())
        caneta = [i for i in range(1, n+1)]
        print(caneta)
        for i in range(1, n):
            entrada = input()
            caneta.remove(int(entrada))
        print(caneta)

    except EOFError:
        break
