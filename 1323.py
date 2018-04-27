sq = [0]
for i in range(1, 101):
    sq.append(i*i+sq[i-1])
    
while(True):
    n = int(input())
    if(n == 0):
        break
    print(sq[n])
    