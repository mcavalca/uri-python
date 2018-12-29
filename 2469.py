n = int(input())

notas = input().split()
maiscomum = max(set(notas), key=notas.count)

print(maiscomum)
