from math import sqrt

def precisao(qt, lista, media):
    somatorio = 0
    for caso in range(qt):
        somatorio += (lista[caso] - media)**2
    resultado = sqrt( (somatorio) / (qt - 1) )
    return resultado

while True:
    try:

        h, m = input().split()
        medidas = [float(x) for x in input().split()]
        casos = (int(h) * 60) // int(m)
        media = sum(medidas) / casos
        resultado = precisao(casos, medidas, media)

        print('%.5f' % resultado)

    except EOFError:
        break
