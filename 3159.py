tij={'a':'2',
     'b':'22',
     'c':'222',
     'd':'3',
     'e':'33',
     'f':'333',
     'g':'4',
     'h':'44',
     'i':'444',
     'j':'5',
     'k':'55',
     'l':'555',
     'm':'6',
     'n':'66',
     'o':'666',
     'p':'7',
     'q':'77',
     'r':'777',
     's':'7777',
     't':'8',
     'u':'88',
     'v':'888',
     'w':'9',
     'x':'99',
     'y':'999',
     'z':'9999',
     ' ':'0'}
for _ in range(int(input())):
    s=input()
    f=[]
    aux=False
    i=0
    for c in s:
        tmp=""
        if aux and c.islower() and tij.get(c.lower())[0] == f[i-1][-1]:tmp+='*'
        if c.isupper():tmp+='#'
        tmp+=tij.get(c.lower())
        f.append(tmp)
        aux=True
        i+=1
    print(*f,sep="")
