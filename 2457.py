letra = input()
palavra = input().split()
total = 0.0
for l in palavra:
    if letra in l:
        total += 1

total /= len(palavra)/100

print('%.1f' % total)
