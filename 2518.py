import math
while True:
    try:
        deg = int(input())
        h, c, l = input().split()

        hip = math.sqrt((int(c)**2)+(int(h)**2))
        hip *= (int(l)/100*int(deg))/100
        print('%.4f'%hip)

    except EOFError:
        break