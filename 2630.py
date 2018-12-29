t = int(input())

for i in range(t):
    t -= 1
    conv = input()
    r, g, b = [int(x) for x in input().split()]
    if conv == 'eye':
        p = int(r*0.30 + g*0.59 + b*0.11)
    elif conv == 'mean':
        p = int((r + g + b) / 3)
    elif conv == 'max':
        p = max(r, g, b)
    elif conv == 'min':
        p = min(r, g, b)

    print('Caso #%d: %d' % (i+1, p))
