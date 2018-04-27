n = int(input())

while(n > 0):
    n -= 1
    diet = input()
    bre = input()
    din = input()
    diet = sorted(set(diet))
    bre = sorted(set(bre))
    din = sorted(set(din))
    out = ''
    print(bre, din)
    for i in diet:
        if i in bre:
            print(i)
            diet.remove(i)
            bre.remove(i)
        if i in din:
            diet.remove(i)
            din.remove(i)
        if ((i not in bre) and (i not in din)):
            out += i
    
    print(bre, din)
    print(diet)
    if((len(bre) == 0) or (len(din) == 0)):
        out = 'CHEATER'
    print(out)