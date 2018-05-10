while True:
    a, b = input().split()
    if a == b == '0':
        break
    fa = [int(x) for x in input().split()]
    fb = [int(x) for x in input().split()]
    a = set(fa)
    b = set(fb)
    c = b
    f = 0
    if len(a) < len(b):
        c = a
        a = b
    c = [x for x in c if x not in a]
    print(len(c))