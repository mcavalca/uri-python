lista = ['GQaku', 'ISblv', 'EOYcmw', 'FPZdnx', 'JTeoy', 'DNXfpz', 'AKUgq', 'CMWhr', 'BLVis', 'HRjt']

n = int(input())

while n:
    n -= 1
    senha = input()
    cripto = ''
    for letra in senha:
        if letra != ' ':
            cripto+= str([i for i, new in enumerate(lista) if letra in new][0])

    print(cripto)
