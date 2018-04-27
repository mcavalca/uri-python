n = int(input())
while(n > 0):
    n -= 1
    j1 = input()
    j2 = input()
    if(j1 == 'ataque'):
        if(j2 == 'ataque'):
            print('Aniquilacao mutua')
        else:
            print('Jogador 1 venceu')
    elif(j1 == 'papel'):
        if((j2 == 'ataque') or (j2 == 'pedra')):
            print('Jogador 2 venceu')
        else:
            print('Ambos venceram')
    elif(j1 == 'pedra'):
        if(j2 == 'papel'):
            print('Jogador 1 venceu')
        if(j2 == 'ataque'):
            print('Jogador 2 venceu')
        elif(j2 == 'pedra'):
            print('Sem ganhador')
            