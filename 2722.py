n = int(input())
while n:
    n -= 1
    p1 = input()
    p2 = input()
    nome = ''
    for d in range(0, len(p1) - 1, 2):
        nome += p1[d:d+2] + p2[d:d+2]
    print(nome)
