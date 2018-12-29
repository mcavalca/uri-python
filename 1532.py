pontos = [[]] * 31
for i in range(1, 31):
    for j in range(1, i):
        pontos[i].append(i * j)

print(pontos[5])

while True:
    n, v = input().split()
    if n == v == '0':
        break
    for i in range(int(v), 0, -1):
        print('')
