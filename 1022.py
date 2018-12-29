def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

n = int(input())
while n:
    n -= 1
    n1, lixo1, d1, op, n2, lixo2, d2 = input().split()
    n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)

    if op == '+':
        num = (n1 * d2 + n2 * d1)
        den = (d1 * d2)
    elif op == '-':
        num = (n1 * d2 - n2 * d1)
        den = (d1 * d2)
    elif op == '*':
        num = (n1 * n2)
        den = (d1 * d2)
    elif op == '/':
        num = (n1 * d2)
        den = (n2 * d1)

    print('%d/%d = %d/%d' % (num, den, num/gcd(num, den), den/gcd(num, den)))
