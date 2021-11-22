n=int(input())
f=[]
for i in range(n):
    nome,idade=input().split()
    l=[nome,int(idade)]
    f.append(l)
f=sorted(f,key=lambda x: x[0])
f=sorted(f,key=lambda x: x[1],reverse=True)
time=1
v=int(n/3)
i=0
while True:
    print(f"Time {time}")
    print(f[i][0],f[i][1])
    print(f[i+v][0],f[i+v][1])
    print(f[i+v+v][0],f[i+v+v][1])
    print()
    i+=1
    if time==v:break
    time+=1
