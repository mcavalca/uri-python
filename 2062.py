n = int(input())
w = input().split()

for ind, i in enumerate(w):
    if(i[0:2]=='UR' and len(i)==3):
        w[ind] = 'URI'
    if(i[0:2]=='OB' and len(i)==3):
        w[ind] = 'OBI'
        
i = ' '.join(w)
print(i)