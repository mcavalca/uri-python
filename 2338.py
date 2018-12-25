n = int(input())
morse = ['=.===', '===.=.=.=', '===.=.===.=', '===.=.=', '=', '=.=.===.=', '===.===.=',
              '=.=.=.=', '=.=', '=.===.===.===', '===.=.===', '=.===.=.=', '===.===', '===.=',
              '===.===.===', '=.===.===.=', '===.===.=.===', '=.===.=', '=.=.=', '===', '=.=.===',
              '=.=.=.===', '=.===.===', '===.=.=.===', '===.=.===.===', '===.===.=.=', ' ']

dicionario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

while n:
    n -= 1
    palavra = input()
    palavra = palavra.replace('.....', '1')
    resultado = ''
    print(palavra)
    for letra in palavra:
        letra = letra.split('...')
        for i in letra:
            resultado += dicionario[morse.index(i)]
    print(resultado)
