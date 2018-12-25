n = int(input())
v = input().split()

for i in range(len(v)):
    v[i] = int(v[i])

votos = sum(v)
razao = sorted([x/votos for x in v], reverse=True)

if (razao[0] >= 0.45) or ((razao[0] >= 0.4) and (razao[0] - razao[1] >= 0.1)):
    print(1)
else:
    print(2)
