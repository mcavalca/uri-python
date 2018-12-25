a, c, x, y = [int(x) for x in input().split()]
q = c - a - x - y - 1
if q < 0:
    if x > y/2:
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')
else:
    print('Igor feliz!')
