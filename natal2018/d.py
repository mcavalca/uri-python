n = int(input())
pilha = []
menor = [-1]

while n:
    n -= 1
    try:
        acao = input().split()
        acao, v = acao[0], acao[1]
        pilha.append(int(v))
        for i in range(len(menor) + 1):
            if menor[i] < int(v):
                menor.insert(i, int(v))
                break
    except IndexError:
        if len(pilha) > 0:
            if acao[0] == 'MIN':
                print(menor[-2])
            elif acao[0] == 'POP':
                menor.remove(pilha[-1])
                pilha.pop()

        else:
            print('EMPTY')
