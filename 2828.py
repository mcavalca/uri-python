from math import factorial

big = 10**9 + 7
palavra = input()

occ = {}
for c in palavra:
    if c in occ:
        occ[c] += 1
    else:
        occ[c] = 1

cima = 0
baixo = 1

for c in occ:
    cima += occ[c]
    baixo *= factorial(occ[c])

resultado = factorial(cima)//baixo
resultado = pow(resultado, 1, big)

print(resultado)
