final = 0.0
total = 0
while True:
    w1, w2, r = [int(x) for x in input().split()]
    if w1 == w2 == r == 0:
        break
    media = float(((w1 * (1 + r/30))+(w2 * (1 + r/30))))/2.0
    final += media
    total += 1
    if media < 13:
        print('Nao vai da nao')
    elif media < 14:
        print('E 13')
    elif media < 40:
        print('Bora, hora do show! BIIR!')
    elif media < 60:
        print('Ta saindo da jaula o monstro!')
    else:
        print('AQUI E BODYBUILDER!!')

final = final/float(total)
if final > 40:
    print()
    print('Aqui nois constroi fibra rapaz! Nao e agua com musculo!')
