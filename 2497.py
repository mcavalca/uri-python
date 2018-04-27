n = 1
while(True):
    i = int(input())
    if(i == -1):
        break
    i //= 2
    print('Experiment %d: %d full cycle(s)' % (n, i))
    n += 1