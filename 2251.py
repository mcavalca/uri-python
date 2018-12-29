teste = 1
while True:
    n = int(input())
    if n == 0:
        break
    print('Teste %d' % teste)
    print((2**n) - 1)
    print()
    teste += 1
