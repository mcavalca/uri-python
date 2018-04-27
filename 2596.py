div = []
isok = []

for i in range(1001):
    div.append(0)
    isok.append(0)
    tot = 0
    for j in range(i, 0, -1):
        if(i % j == 0):
            tot += 1
    if(tot % 2 != 0):
        div[i] = 1
    for j in range(i, 0, -1):
        if(div[j] == 0):
            isok[i] += 1

        
n = int(input())
while(n > 0):
    n -= 1
    i = int(input())
    print(isok[i])