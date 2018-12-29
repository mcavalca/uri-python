n = int(input())
check = 0

while n:
    n -= 1
    m, c = [int(x) for x in input().split()]
    hash = {str(x) : [] for x in range(m)}
    entrada = [int(x) for x in input().split()]

    if check:
        print()

    for i in entrada:
        resto = i % m
        hash[str(resto)].append(int(i))

    for i in hash:
        print('%d -> ' % int(i), end = '')
        for j in hash[i]:
            print('%d -> ' % j, end = '')
        print('\\')

    check = 1
