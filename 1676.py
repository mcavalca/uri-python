from math import sqrt

# Crivo de Erastotenes (adaptado) para gerar os primeiros 3000
# primos rapidamente

p = [2, 3]
i = 5
while len(p) < 3000:
    j = 0
    k = sqrt(i)

    while p[j] < k and i % p[j]:
        j += 1

    if p[j] > k:
        p += [i]

    if i % 3 == 2:
        i += 2
    else:
        i += 4

while True:
    n = int(input())
    if n == 0:
        break
    print(p[n - 1])
