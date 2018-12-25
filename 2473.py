flavinho = input().split()
sorteado = input().split()
resultado = ['azar', 'azar', 'azar', 'terno', 'quadra', 'quina', 'sena']
print(resultado[len(list(set(flavinho).intersection(sorteado)))])
