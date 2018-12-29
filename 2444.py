v, t = [int(x) for x in input().split()]
t = input().split()
for a in t:
    v += int(a)
    if v > 100:
        v = 100
    elif v < 0:
        v = 0

print(v)
