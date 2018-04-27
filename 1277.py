n = int(input())

while(n > 0):
    n -= 1
    a = int(input())
    l = input().split()
    p = input().split()
    for ind, a in enumerate(p):
        a = a.replace('M', '')
        old = len(a)
        a = a.replace('A', '')
        new = len(a)
        try:
            new /= old
            if(new >= 0.75):
                l[ind] = '-'
        except ZeroDivisionError:
            l[ind] = '-'
            
    l = [a for a in l if a is not '-']
    for ind, a in enumerate(l):
        print(a, end='')
        if(ind != len(l)-1):
            print(' ', end='')
    print()
    