n = int(input())
lista = [int(x) for x in input().split()]
lista.sort()
for i in range(len(lista)):
    if lista[i] != (i + 1):
        break
if lista[i] == (i + 1):
    i += 1
print(i + 1)
