n = int(input())

notas = input().split()
maior = {i:notas.count(i) for i in notas}
sorted(maior, key=maior.get)
print(maior.keys())
