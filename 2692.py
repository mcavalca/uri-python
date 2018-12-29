n, m = [int(x) for x in input().split()]
troc_e = troc_s = []

while n:
    n -= 1
    e, s = input().split()
    troc_e.append(e)
    troc_s.append(s)

while m:
    m -= 1
    palavra = input()
    for i in range(len(palavra)):
        if palavra[i] in troc_e:
            palavra[i].replace()
