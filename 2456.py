cartas = [int(x) for x in input().split()]

if cartas == sorted(cartas):
    print('C')
elif cartas == sorted(cartas, reverse=True):
    print('D')
else:
    print('N')
