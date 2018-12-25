t = int(input())
while t:
    t -= 1
    b = int(input())
    ad, dd, ld = [int(x) for x in input().split()]
    ag, dg, lg = [int(x) for x in input().split()]
    golped = (ad + dd)/2.0
    golpeg = (ag + dg)/2.0
    if ld % 2 == 0:
        golped += b
    if lg % 2 == 0:
        golpeg += b

    if golped > golpeg:
        print('Dabriel')
    elif golpeg > golped:
        print('Guarte')
    else:
        print('Empate')
