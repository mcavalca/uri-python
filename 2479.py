n = int(input())

lista = []
bom = 0
while n > 0:
    n -= 1
    c, nome = input().split()
    lista.append(nome)
    if c == '+':
        bom += 1
        
lista.sort()
for i in lista:
    print(i)

print('Se comportaram: %d | Nao se comportaram: %d'%(bom, len(lista)-bom))