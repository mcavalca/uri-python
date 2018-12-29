n, w = [int(x) for x in input().split()]
gigantes = []

while n:
    n -= 1
    entrada = input().split()
    if int(entrada[-1]) > w:
        gigantes.append(' '.join(entrada[:-1]))

for g in gigantes:
    print(g)
