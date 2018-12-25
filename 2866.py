n = int(input())
while n > 0:
    n -= 1
    c = input()
    saida = ''.join(s for s in c if s.islower())
    saida = saida[::-1]
    print(saida)
