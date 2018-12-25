n = int(input())

while n:
    n -= 1
    dieta = input()
    cafe = input()
    almoco = input()
    almoco += cafe
    for letra in range(len(almoco)):
        if almoco[letra] not in dieta:
            dieta = 'CHEATER'
            break
        else:
            dieta = dieta.replace(almoco[letra], '')

    if dieta != 'CHEATER':
        dieta = ''.join(sorted(dieta))
    print(dieta)
