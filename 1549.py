t = int(input())
pi = 3.14
while t > 0:
    t -= 1
    n, l = input().split()
    bme, bma, h = input().split()
    bme = int(bme)/2
    bma = int(bma)/2
    print(bme, bma, n)
    # CALCULO DO VOLUME MAXIMO
    v = ((pi*int(h)/3)*(bme**2+bme*bma+bma**2))
    # CALCULO DO VOLUME QUE SOBRA
    n = (int(l)/int(n))-v
    print(n, v)
    h = (3*n)/(pi*(bme**2+bme*bma+bma**2))
    print(h)