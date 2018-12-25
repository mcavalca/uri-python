n = int(input())
palavras = []
while n:
    n -= 1
    palavras.append(input())

palavras = sorted(sorted(palavras), key=str.lower)

for i in palavras:
    print(i)
