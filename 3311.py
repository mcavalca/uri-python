f=[]
for i in range(int(input())):
    f.append(input())
f.sort(key=lambda e: e[0])
print(*f,sep="\n")
