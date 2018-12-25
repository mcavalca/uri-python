from math import sqrt

peso = int(input())
prim = []

for i in range(peso, 64000):
    p = 1
    for j in range(2, int(sqrt(i)) + 1 ):
        if i % j == 0:
            p = 0
            break
    if p:
        prim.append(i)
    if len(prim) == 10:
        break

kmh = sum(prim)
print(kmh, 'km/h')
h = int(60000000/kmh)
d = int(h/24)
print(h, 'h /', d, 'd')
