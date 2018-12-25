from collections import deque

def jos(k, j):
    d = deque(k)
    i = 0
    while len(d) > 1:
        d.rotate(-j[i])
        d.pop()
        i += 1
        if i == len(j):
            i = 0
    return(d.pop())

def gen_prime(n):
    p = [2, 3, 5, 7]
    i = 11
    while len(p) < n:
        for j in p:
            if i % j == 0:
                break
        if j == p[len(p) - 1]:
            p.append(i)
        i += 1
    return p[0:n]


primos = gen_prime(3501)

while True:
    k = int(input())
    if not k:
        break
    k = [x for x in range(1, int(k)+1)]
    resultado = jos(k, primos)
    print(resultado)
