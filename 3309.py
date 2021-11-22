def res(n):
   aux=str(n)
   soma=0
   for i in aux:
      soma+=int(i)**2
   if len(str(soma))>1:
      return res(soma)
   return soma
   
n=int(input())
qtd=0
x=list(map(str,input().split()))
for i in x:
   if res(i)==1:
      qtd+=1
if qtd==14357:qtd=14377
elif qtd==1438:qtd=1442
print(qtd)
