p = input()
mensagem = ''
for palavra in p.split():
    for letra in range(1, len(palavra), 2):
        mensagem += palavra[letra]
    mensagem += ' '
print(mensagem[:-1])
