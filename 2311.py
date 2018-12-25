n = int(input())
while n:
    n -= 1
    nome = input()
    gd = float(input())
    nota = [float(x) for x in input().split()]
    nota = sum(sorted(nota)[1:6]) * gd
    print('%s %.2f' % (nome, nota))
