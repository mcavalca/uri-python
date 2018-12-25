from math import sqrt
n = int(input())

while n:
    n -= 1
    m = int(input())
    m = int((sqrt(1 + 8*m) - 1) / 2)
    print(m)
