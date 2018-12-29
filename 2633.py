while True:
    try:
        n = int(input())
        total = {}
        while n:
            n -= 1
            peca = input().split()
            total[peca[0]] = int(peca[1])

        # ordenar o dicionario
        total = {k: v for k, v in sorted(total.items(), key=lambda x: x[1])}
        
        for peca in total:
            print(peca)

    except EOFError:
        break
