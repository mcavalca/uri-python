n = int(input())
lista = [int(x) for x in input().split()]
total = 1
for x in range(2, n):
    if lista[x] - lista[x-1] != lista[x-1] - lista[x-2]:
        total += 1
print(total)
