entrada = input().split()
inteiro = int(entrada[0])
real = float(entrada[1])
caracter = entrada[2]
frase = ' '.join(entrada[3:])
tudo = ''.join(entrada)
print('%s' % tudo)
print('%d\t%f\t%c\t%s' % (inteiro, real, caracter, frase))
print('%10d%10.6f%10c%10s' % (inteiro, real, caracter, frase))
