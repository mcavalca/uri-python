while True:
    try:
        n, m = input().split()
        l = []
        qt = 4
        if n == m == '0':
            break
        for i in range(int(n)):
            l.append([int(x) for x in input().split()])
        # NINGUEM RESOLVEU TODOS OS PROBLEMAS
       # for x in range(int(n)):
        #    if any(y != 1 for y in l[x]):
         #       qt =- 1
          #      break
        # TODO PROBLEMA FOI RESOLVIDO POR PELO MENOS 1 PESSOA
        
        # NENHUM PROBLEMA FOI RESOLVIDO POR TODOS
        for x in range(int(n)):
            if all(l[x] == 0):
                qt =- 1
                print('todos')
                break
        
        # TODOS RESOLVERAM PELO MENOS 1 PROBLEMA
        for x in range(int(n)):
            if all():
                qt =- 1
                break
        
    except EOFError:
        break