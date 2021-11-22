from math import ceil,sqrt
def perf(a, b) :  
    n = ceil(sqrt(a));  
    n2 = n * n;  
    n = (n * 2) + 1;  
    s=0
    while ((n2 >= a and n2 <= b)) : 
        s+=1 
        n2 = n2 + n;  
        n += 2;  
    return s
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(perf(a,b))
