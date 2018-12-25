
while True:
    try:
        n = int(input())
        filhotes = 0
        while n > 0:
            n -= 1
            especie = input()
            raca = input()
            nome = input().split()
            input()
            if (len(nome) > 1) and (especie == 'cachorro'):
                for i in nome:
                    if i[0] == raca[0]:
                        filhotes +=1
                        break

        print(filhotes)

    except EOFError:
        break
