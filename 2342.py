n = int(input())
p = input().split()
if p[1] == '+':
    resultado = int(p[0]) + int(p[2])
else:
    resultado = int(p[0]) * int(p[2])

if resultado > n:
    print('OVERFLOW')
else:
    print('OK')
