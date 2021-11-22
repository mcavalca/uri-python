from re import findall,IGNORECASE
for _ in range(int(input())):
    s=input()
    f=sorted(findall(r'[bcdfghjklmnpqrstvwxyz]+',s,IGNORECASE),key=lambda x: len(x),reverse=True)
    print(f'{s} nao eh facil') if len(f[0])>=3 else print(f'{s} eh facil')
