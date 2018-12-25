n = int(input())
while n:
    n -= 1

    n1, op, n2, lixo, res = input().split()
    n1, n2 = int(n1), int(n2)
    
    if op == '+':
        real = n1 + n2
    elif op == '-':
        real = n1 - n2
    else:
        real = n1 * n2

    rr = 'r' * abs(real - int(res))
    print('E{}ou!'.format(rr))
