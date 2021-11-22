def filtro(v):
    return [x for x in v if x]
d=dict()
for i in range(int(input())):
    s=input()
    tam=len(s)
    if tam in d.keys():d[tam].append(s)
    else:d[tam]=[s]
d=dict(sorted(d.items(), key=lambda x: x[0]))
v=list(d.values())
while True:
    try:
        tam=len(v)
        if tam==0:break
        a=[]
        for i in range(tam):
            a.append(v[i][0])
            del v[i][0]
        v=filtro(v)
        print(*a,sep=", ")
    except:break
