n = int(input())
duende = input().split()
for x in range(n):
    duende[x] = int(duende[x])
duende.sort()
maior = int(duende[n-1]) + 1
while True:
    for x in range(n):
        if (maior % duende[x]) == 0 and duende[x] != 1:
            maior += 1
            break
    if x == n-1:
        break
print(maior)
