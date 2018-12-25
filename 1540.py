n = int(input())
while n:
    n -= 1
    a, b, c, d = [int(x) for x in input().split()]
    taxa = float((d-b)/(c-a))
    taxa = str('%.3f' % taxa).replace('.', ',')
    taxa = taxa[:len(taxa) - 1]
    print((taxa))
