c = {'suco de laranja':120, 'morango fresco':85, 'mamao':85, 'goiaba vermelha':70, 'manga': 56, 'laranja':50, 'brocolis':34}

while True:
    n = int(input())
    if n == 0:
        break
    vitamina = 0
    for i in range(n):
        w = input().split()
        qt = int(w[0])
        fruta = ' '.join(w[1:])
        vitamina += c[fruta]*qt
    if vitamina < 110:
        print('Mais %d mg' % (110-vitamina))
    elif vitamina > 130:
        print('Menos %d mg' % (vitamina-130))
    else:
        print('%d mg' % (vitamina))