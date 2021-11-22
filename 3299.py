lista = input()
lista1 = int(lista)*10
lista1 = str(lista1)

vetor = list(map(int,lista1))
tam = len(vetor)
esmalas = False
for i in range(tam):
    if(vetor[i] == 1):
        if(vetor[i+1] == 3):
            esmalas = True
print("{} es de Mala Suerte".format(lista)) if esmalas else print("{} NO es de Mala Suerte".format(lista))
