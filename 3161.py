n,m=map(int,input().split())
vet_n,vet_m=[],[]
for i in range(n):vet_n.append(input().lower())
for i in range(m):vet_m.append(input().lower())
for i in vet_n:
    aux,aux_inv=False,i[::-1] 
    for j in vet_m:
        if i in j or aux_inv in j:
            aux=True
            break
    print("Sheldon come a fruta", i) if aux else print("Sheldon detesta a fruta", i)
