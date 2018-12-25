from fractions import gcd

while True:
    n, a, b = [int(x) for x in input().split()]
    if n == a == b == 0:
        break

    total = 0
    lcm = (a * b) // gcd(a, b)
    total = n//a + n//b - n//lcm

    print(total)
