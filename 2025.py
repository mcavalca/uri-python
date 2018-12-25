n = int(input())

while n:
    n -= 1
    texto = input().split()
    
    for palavra in texto:

        if ('oulupukk' in palavra):

            if len(palavra) == 10:
                texto[texto.index(palavra)] = 'Joulupukki'
            if len(palavra) == 11:
                texto[texto.index(palavra)] = 'Joulupukki.'

    texto = ' '.join(texto)
    print(texto)
