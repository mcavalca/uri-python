def mod(n):
    saida = 0
    tam = len(n)
    for i in range(0, tam):
        saida = (saida * 10 + int(n[i])) % 4
    return saida

t = int(input())
while t:
    t -= 1
    n = mod(input())
    if n == 0:
        print(1)
    elif n == 1:
        print(7)
    elif n == 2:
        print(9)
    else:
        print(3)
