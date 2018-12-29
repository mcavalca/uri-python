n = int(input())
v = input().split()
pontos = 1
seq = 1
for i in range(1, n):
    if v[i] == v[i - 1]:
        seq += 1
    else:
        if seq > pontos:
            pontos = seq
        seq = 1

if seq > pontos:
    pontos = seq
print(pontos)
