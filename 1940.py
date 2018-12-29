j, r = [int(x) for x in input().split()]
entrada = list(map(int, input().split()))

pontos = [0] * j

for k in range(j):
    pontos[k] = sum(entrada[k::j])

pontos = pontos[::-1]
vencedor = j - pontos.index(max(pontos))
print(vencedor)
