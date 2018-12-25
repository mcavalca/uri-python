i = 1
while True:
    a = input()
    if a == '0':
        break
    if i != 1:
        print()
    painel = input()
    print('Instancia %d' % i)
    i += 1
    if a in painel:
        print('verdadeira')
    else:
        print('falsa')
