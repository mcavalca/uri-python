while True:
    ev1, ev2, at, d = [int(x) for x in input().split()]
    if ev1 == ev2 == at == d == 0:
        break

    # Gambler's Ruin
    # https://en.wikipedia.org/wiki/Gambler's_ruin
    #
    # idk it just works

    c, ev1 = ev1, 0
    while c > 0:
        c -= d
        ev1 += 1

    c, ev2 = ev2, 0
    while c > 0:
        c -= d
        ev2 += 1

    if at == 3:
        ev1 /= (ev1 + ev2)
    else:
        qp = (1 - (6 - at)/ 6)
        qp = (1 - qp) / qp
        ev1 = (1 - qp**ev1) / (1 - qp**(ev1 + ev2))

    print('%.1f' % (ev1 * 100))
