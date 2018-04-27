n = int(input())
pom = []
for i in range(n):
    pom.append(input())

pom = set(pom)
l = 151 - len(pom)
print('Falta(m) %d pomekon(s).' % l)