r, c = [int(x) for x in input().split()]
caixas = []
linha_index = []
roubadas = 0

for linha in range(r):
    caixas.append([int(x) for x in input().split()])
    roubadas += sum([(x - 1) for x in caixas[linha] if x != 0 and x != 1])
    maior = max(caixas[linha])
    roubadas -= maior
    linha_index.append([x for x, y in enumerate(caixas[linha]) if y == maior])

print(linha_index)

for col in range(c):
    colunas = [x[col] for x in caixas]

print(roubadas)
