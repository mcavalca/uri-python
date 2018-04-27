f = []
par = []
impar = []
n = int(input())

while(n > 0):
    i = int(input())
    if(i % 2 == 0):
        par.append(i)
    else:
        impar.append(i)
    n -= 1

par.sort()
impar.sort(reverse=True)
for i in par:
    f.append(i)
for i in impar:
    f.append(i)
    
for i in f:
    print(i)