n = int(input())
while n > 0:
    n -= 1
    l = int(input())
    vagao = input().split()

    swap = 0
    for i in range(l):
        for j in range(i + 1, l):
            if (int(vagao[i]) > int(vagao[j])):
                vagao[i], vagao[j] = vagao[j], vagao[i]
                swap += 1

    print('Optimal train swapping takes %d swaps.' % swap)
