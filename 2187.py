teste = 1
while True:
    v = int(input())
    if v == 0:
        break
    bits = ['0'] * 4
    if v >= 50:
        bits[0] = str(v // 50)
        v = v % 50
    if v >= 10:
        bits[1] = str(v // 10)
        v = v % 10
    if v >= 5:
        bits[2] = str(v // 5)
        v = v % 5
    bits[3] = str(v)
    print('Teste %d' % teste)
    print(' '.join(bits))
    print()
    teste += 1
