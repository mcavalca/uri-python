from math import sqrt, ceil

a, b, c, d = [int(x) for x in input().split()]

l = int(ceil(sqrt(c)))
n = a
for n in range(a, l, a):
    if (n % b != 0) and (c % n == 0) and (d % n != 0):
        break

if n > c:
    print('-1')
else:
    print(n)
