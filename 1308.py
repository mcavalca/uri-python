import math
n = int(input())
while n > 0:
    n -= 1
    m = int(input())
    if(n%2 == 0):
        i = int((-1+math.sqrt(4+8*m))/2)
    else:
        i = int((-1+math.sqrt(13+8*m))/2)
    print(i)