participantes,orcamento,hoteis,semanas=map(int,input().split())
s=3000000
for i in range(hoteis):
    precopessoa=int(input())
    camas=sorted(list(map(int,input().split())))
    custo=precopessoa*participantes
    if custo<=orcamento and custo<=s and any(x in camas for x in range(participantes,1000)):s=custo
print('stay home') if s==3000000 else print(s)
