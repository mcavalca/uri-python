t = int(input())
while t > 0:
    t -= 1
    d, n = input().split()
    troco = 0.0
    preco = input().split()
    for x in preco:
        if troco < (float(d) % float(x)) and float(x) < float(d):
            troco = (float(d) % float(x))
    print("%.2f" % troco)
